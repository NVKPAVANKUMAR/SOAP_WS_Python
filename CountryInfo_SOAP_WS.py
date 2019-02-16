import unittest

import HtmlTestRunner
from openpyxl import load_workbook
from zeep import Client


def parse_excel(file_path):
    rows = []
    wb = load_workbook(file_path)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, min_col=1, max_row=5, max_col=4):
        rows.append(row)
    return rows


class Country_WS_Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global client
        client = ''
        cls.base_uri = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
        client = Client(cls.base_uri)

    def test_ListOfContinentsByNameSoapRequest(self):
        result = client.service.ListOfContinentsByName()
        print result

    def test_02(self):
        client = Client(self.base_uri)
        result = client.service.CapitalCity("IN")
        print result

    def test_03(self):
        out = parse_excel("data/TestData.xlsx")
        print out[0][0].value

    def test_04(self):
        for i in range(0, 4):
            for j in range(0, 4):
                print i, j


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
