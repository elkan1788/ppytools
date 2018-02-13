# coding: utf-8
# __author__ = 'elkan1788@gmail.com'

from ppytools.conf_reader import ConfReader

import unittest
import logging
import os

logger = logging.getLogger(__name__)
WORK_DIR = os.path.dirname(os.path.realpath(__file__))


class TestConfReaderCase(unittest.TestCase):

    name_conf = os.path.join(WORK_DIR, 'conf/name_config.ini')
    author_conf = os.path.join(WORK_DIR, 'conf/author_config.ini')
    cr = ConfReader(author_conf, name_conf)
    logger.info(cr.get_all_values())

    def test_sections(self):
        sections = TestConfReaderCase.cr.sections()
        self.assertIsNotNone(sections)
        self.assertEqual(2, len(sections))

    def test_get_keys(self):
        keys = TestConfReaderCase.cr.get_keys('PPyTools')
        self.assertIsNotNone(keys)
        self.assertIs(True, 'name' in keys)

    def test_get_all_values(self):
        all_values = TestConfReaderCase.cr.get_all_values()
        self.assertIsNotNone(all_values)
        self.assertEqual('1.0.1', all_values['PPyTools']['ver'])

    def test_get_values(self):
        values = TestConfReaderCase.cr.get_values('Author')
        self.assertIsNotNone(values)
        self.assertEqual('凡梦星尘', values.get('committer'))

    def test_get_value(self):
        value = TestConfReaderCase.cr.get_value('Author', 'owner')
        self.assertIsNotNone(value)
        self.assertEqual('elkan1788', value)

    def test_get_tuple(self):
        tuple_obj = TestConfReaderCase.cr.get_tuple('PPyTools')
        self.assertIsNotNone(tuple_obj)
        self.assertEqual('2018-01', tuple_obj.since)

