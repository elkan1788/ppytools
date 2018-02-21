# coding: utf-8
# __author__ = 'elkan1788@gmail.com'
from unittest import TestSuite

from test.HTMLTestRunner import HTMLTestRunner
import logging
import os
import unittest

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] {%(name)-10s} - %(message)s')


if __name__ == '__main__':

    suite = TestSuite()
    suites = unittest.defaultTestLoader.discover('./')
    for all_test_suite in suites:
        for test_suite in all_test_suite:
            suite.addTests(test_suite)

    work_dir = os.path.dirname(os.path.realpath(__file__))
    report_html = os.path.join(work_dir, 'reports/ppytools_test_report.html')

    with open(report_html, 'wb') as html:
        runner = HTMLTestRunner(stream=html, title='PPyTools Test Report')
        runner.run(suite)


