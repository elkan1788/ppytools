# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.hive_client import HiveClient

import logging
import mock
import unittest

logger = logging.getLogger(__name__)

@unittest.skip('There not found a suite method mock hive connect')
class TestHiveClientCase(unittest.TestCase):
    """TestHiveClientCase
    """


    @mock.patch('ppytools.hive_client.hive.connect')
    def testExecCount(self, mock_hive_conn):
        mock_hive_conn.return_value = mock.Mock()
        hc = HiveClient('127.0.0', '10000', 'hive')
        result , size = hc.execQuery('SELECT 1')


if __name__ == '__main__':
    unittest.main()