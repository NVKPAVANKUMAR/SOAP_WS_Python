from zeep import Client
import unittest
import HtmlTestRunner


def do_arithmetic(client, operation, num1, num2):
    if operation == "Add":
        return client.service.Add(num1, num2)
    elif operation == "Subtract":
        return client.service.Subtract(num1, num2)
    elif operation == "Multiply":
        return client.service.Multiply(num1, num2)
    elif operation == "Divide":
        return client.service.Divide(num1, num2)


def assert_result(actual_result, expected_result):
    assert actual_result == expected_result


class Calculator_WS(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global client
        client = ''
        cls.base_uri = 'http://www.dneonline.com/calculator.asmx?WSDL'
        client = Client(cls.base_uri)

    @staticmethod
    def test_01addition():
        actual_result = do_arithmetic(client, "Add", 5, 5)
        assert_result(actual_result, 10)

    @staticmethod
    def test_02subtraction():
        actual_result = do_arithmetic(client, "Subtract", 20, 10)
        assert_result(actual_result, 10)

    @staticmethod
    def test_03multiplication():
        actual_result = do_arithmetic(client, "Multiply", 20, 80)
        assert_result(actual_result, 1600)

    @staticmethod
    def test_04divide():
        actual_result = do_arithmetic(client, "Divide", 200, 10)
        assert_result(actual_result, 20)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
