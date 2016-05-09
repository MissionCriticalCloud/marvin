import unittest
import os
import sys
import logging
from functools import partial


class TestCaseExecuteEngine(object):

    def __init__(self, testclient, config, tc_logger=None,
                 debug_stream=sys.stdout):
        """
        Initialize the testcase execution engine
        """
        self.__testClient = testclient
        self.__parsedConfig = config
        self.__tcRunLogger = tc_logger
        self.__debugStream = debug_stream
        self.__loader = unittest.loader.TestLoader()
        self.__suite = None

    def loadTestsFromDir(self, test_directory):
        """ Load the test suites from a package with multiple test files """
        self.__suite = self.__loader.discover(test_directory)
        self.injectTestCase(self.__suite)

    def loadTestsFromFile(self, file_name):
        """ Load the tests from a single script/module """
        if os.path.isfile(file_name):
            self.__suite = self.__loader.discover(os.path.dirname(file_name),
                                                  os.path.basename(file_name))
            self.injectTestCase(self.__suite)

    def injectTestCase(self, test_suites):
        for test in test_suites:
            if isinstance(test, unittest.BaseTestSuite):
                self.injectTestCase(test)
            else:
                # inject testclient and logger into each unittest
                setattr(test, "debug", self.__tcRunLogger.debug)
                setattr(test, "info", self.__tcRunLogger.info)
                setattr(test, "warn", self.__tcRunLogger.warning)
                setattr(test, "error", self.__tcRunLogger.error)
                setattr(test, "clstestclient", self.__testClient)
                setattr(test, "testClient", self.__testClient)
                setattr(test, "config", self.__parsedConfig)
                if hasattr(test, "user"):
                    # when the class-level attr applied. all test runs as
                    # 'user'
                    self.__testClient.getUserApiClient(test.UserName,
                                                       test.DomainName,
                                                       test.AcctType)

    def run(self):
        if self.__suite:
            print "\n==== Test Suite :%s Started ====" % (str(self.__suite))
            unittest.TextTestRunner(stream=self.__debugStream,
                                    verbosity=2).run(self.__suite)
            print "\n==== Test Suite :%s Finished ====" % (str(self.__suite))
