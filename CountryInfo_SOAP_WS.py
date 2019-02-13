from zeep import Client
import unittest
import HtmlTestRunner


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
        result = client.service.ListOfContinentsByNameSoapRequest()
        print result


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
