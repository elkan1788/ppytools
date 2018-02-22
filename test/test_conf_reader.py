# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.conf_reader import ConfReader

import unittest
import logging
import os

logger = logging.getLogger(__name__)


class TestConfReaderCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        work_dir = os.path.dirname(os.path.realpath(__file__))
        name_conf = os.path.join(work_dir, 'conf/name_config.ini')
        author_conf = os.path.join(work_dir, 'conf/author_config.ini')
        cls.cr = ConfReader(author_conf, name_conf)
        logger.info('Configure file info: ')
        for (k, v) in cls.cr.getAllValues().items():
            logger.info('%s: ', k)
            if isinstance(v, dict):
                for (ck, cv) in v.items():
                    logger.info('%s: %s', ck, cv)


    @classmethod
    def tearDownClass(cls):
        cls.cr.getAllValues().clear()

    def testGetSections(self):
        sections = self.cr.getSections()
        self.assertIsNotNone(sections)
        self.assertEqual(2, len(sections))

    def testGetKeys(self):
        keys = self.cr.getKeys('PPyTools')
        self.assertIsNotNone(keys)
        self.assertIs(True, 'name' in keys)

    def testGetAllValues(self):
        all_values = self.cr.getAllValues()
        self.assertIsNotNone(all_values)
        self.assertEqual('1.0.1', all_values['PPyTools']['ver'])

    def testGetValues(self):
        values = self.cr.getValues('Author')
        self.assertIsNotNone(values)
        self.assertEqual('凡梦星尘', values.get('committer'))

    def testGetValue(self):
        value = self.cr.getValue('Author', 'owner')
        self.assertIsNotNone(value)
        self.assertEqual('elkan1788', value)

    def testGetAsTuple(self):
        tuple_obj = self.cr.getAsTuple('PPyTools')
        self.assertIsNotNone(tuple_obj)
        self.assertEqual('2018-01', tuple_obj.since)

