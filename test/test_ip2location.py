# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.ip2location import IP2Location

import logging
import unittest

logger = logging.getLogger(__name__)


class TestIP2LocationCase(unittest.TestCase):
    """TestIP2LocationCase
    """

    @classmethod
    def setUpClass(cls):
        cls.ipSearcher = IP2Location()
        cls.ip = '112.65.18.58'

    @classmethod
    def tearDownClass(cls):
        cls.ipSearcher.close()

    def testMemorySearch(self):
        loc = self.ipSearcher.memorySearch(self.ip)
        logger.info('%s: %d, %s, %s, %s, %s, %s', self.ip, loc.id, loc.country, loc.region, loc.province, loc.city, loc.op)
        self.assertIsNotNone(loc)
        self.assertEquals(loc.id, 995)
        self.assertEquals(loc.country, '中国')
        self.assertEquals(loc.region, '华东')
        self.assertEquals(loc.province, '上海市')
        self.assertEquals(loc.city, '上海市')
        self.assertEquals(loc.op, '联通')

    

