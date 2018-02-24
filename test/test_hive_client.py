# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from mock import patch
from ppytools.hive_client import HiveClient

import logging
import mock
import unittest

logger = logging.getLogger(__name__)

MOCK_SQL = 'SELECT 1'

class TestHiveClientCase(unittest.TestCase):
    """TestHiveClientCase
    """
    @classmethod
    @patch('ppytools.hive_client.hive.connect')
    def setUpClass(cls, mock_hive_conn):
        mock_hive_conn.return_value = mock.Mock(autospec=True)
        cls.hc = HiveClient('127.0.0.1', 10000, 'hive', 'default')
        mock_hive_conn.assert_called_with(database='default', host='127.0.0.1', port=10000, username='hive')
        cls.mock_obj = cls.hc.conn = mock_hive_conn

    @classmethod
    def tearDownClass(cls):
        cls.hc.closeConn()

    def testExecQuery(self):
        result, size = self.hc.execQuery(MOCK_SQL)
        logger.info('mock hive query result: %s', result)
        self.assertIsNotNone(result)
        self.assertEquals(size, 0)

    def testExecCount(self):
        count = self.hc.execCount(MOCK_SQL)
        logger.info('mock hive count result: %d', count)
        self.assertIsNotNone(count)