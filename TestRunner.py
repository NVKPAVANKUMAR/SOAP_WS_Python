import unittest
import HtmlTestRunner
import Arithmetic_SOAP_WS

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Arithmetic_SOAP_WS))

runner = HtmlTestRunner.HTMLTestRunner(output="example_dir", verbosity=2)
runner.run(suite)
