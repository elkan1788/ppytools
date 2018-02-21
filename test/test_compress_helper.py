# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.compress_helper import zipFile, tarFile

import unittest
import logging
import os

logger = logging.getLogger(__name__)


class TestCompressHelperCase(unittest.TestCase):
    """TestCompressHelperCase
    """

    @classmethod
    def setUpClass(cls):
        work_dir = os.path.dirname(os.path.realpath(__file__))
        cls.large_file = os.path.join(work_dir, 'large_file.txt')
        with open(cls.large_file, 'wb') as tmp:
            tmp.seek(5 * 1024 * 1024)
            tmp.write(b'\x00')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.large_file)
        pref_path = cls.large_file[0:cls.large_file.rindex('.')]
        os.remove(pref_path+'.zip')
        os.remove(pref_path+'.tar.gz')

    def testZipFile(self):
        old_size = os.path.getsize(self.large_file)
        zip_file = zipFile(self.large_file)
        cps_size = os.path.getsize(zip_file)

        self.assertGreaterEqual(old_size, cps_size)
        self.assertGreaterEqual((old_size - cps_size), 0)

    def testTarFile(self):
        old_size = os.path.getsize(self.large_file)
        tar_file = tarFile(self.large_file)
        cps_size = os.path.getsize(tar_file)

        self.assertGreaterEqual(old_size, cps_size)
        self.assertGreaterEqual((old_size - cps_size), 0)
