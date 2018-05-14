# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from unittest import TestSuite

import HTMLTestRunner
import logging
import os
import unittest

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] {%(name)-10s} - %(message)s')


if __name__ == '__main__':

    suite = TestSuite()
    suites = unittest.defaultTestLoader.discover('./', pattern='test_*')
    for test_suite in suites:
        suite.addTests(test_suite)

    work_dir = os.path.dirname(os.path.realpath(__file__))
    report_html = os.path.join(work_dir, 'reports/ppytools_test_report.html')

    with open(report_html, 'wb') as html:
        runner = HTMLTestRunner.HTMLTestRunner(stream=html, title='PPyTools Test Report')
        runner.run(suite)


