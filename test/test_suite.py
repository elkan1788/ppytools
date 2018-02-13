# coding: utf-8
# __author__ = 'elkan1788@gmail.com'

from test.test_conf_reader import TestConfReaderCase

from test.HTMLTestRunner import HTMLTestRunner
import logging
import os
import unittest

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] {%(name)-10s} - %(message)s')

if __name__ == '__main__':
    cr_test = unittest.TestLoader().loadTestsFromTestCase(TestConfReaderCase)
    suite = unittest.TestSuite([cr_test])

    work_dir = os.path.dirname(os.path.realpath(__file__))
    report_html = os.path.join(work_dir, 'reports/ppytools_test_report.html')

    with open(report_html, 'wb') as html:
        runner = HTMLTestRunner(stream=html, title='PPyTools Test Report')
        runner.run(suite)
