# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'


from ppytools.csv_helper import write, getIdNameDict

import logging
import os
import unittest

logger = logging.getLogger(__name__)


class TestCSVHelperCase(unittest.TestCase):
    """TestCSVHelperCase
    """

    @classmethod
    def setUpClass(cls):
        work_dir = os.path.dirname(os.path.realpath(__file__))
        cls.path = os.path.join(work_dir, 'id_name.csv')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.path)

    def test_a_Write(self):
        data = [[0, '中国'], [1, 'Python'], [2, 'Java'], [3, 'Go'], [4, 'Ruby'], [5, 'C'], [6, 'C#']]
        logger.info('CSV data: ')
        for row in data:
            logger.info('id: %s, name: %s', row[0], row[1])
        write(self.path, None, data)

        self.assertGreaterEqual(os.path.getsize(self.path), 0)

    def test_b_GetIdNameDict(self):
        id_name_dict = getIdNameDict(self.path)

        self.assertEquals(len(id_name_dict), 7)
        ''' TODO
        why there dict not support use 0 as key value???
        '''
        self.assertEquals(id_name_dict.get(id_name_dict.keys()[0]), '中国')
        self.assertEquals(id_name_dict.get('1'), 'Python')
