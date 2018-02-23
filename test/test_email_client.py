# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.conf_reader import ConfReader
from ppytools.email_client import EmailClient

import os
import logging
import unittest

logger = logging.getLogger(__name__)


class TestEmailClientCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        work_dir = os.path.dirname(os.path.realpath(__file__))
        email_conf = os.path.join(work_dir, 'conf/email_config.ini')
        cls.cr = ConfReader(email_conf)

        cls.to = ['elkan1788@gmail.com']
        cls.cc = ['2292706174@qq.com']

        smtp_conf = cls.cr.getValues('EmailServer')
        cls.ec = EmailClient(**smtp_conf)
        cls.email_att = []
        small_att = os.path.join(work_dir, 'small_email_att.txt')
        large_att = os.path.join(work_dir, '大文件.txt')
        with open(small_att, 'wb') as att:
            att.seek(2 * 1024 * 1024)
            att.write(b'\x00')
        with open(large_att, 'wb') as att:
            att.seek(5 * 1024 * 1024)
            att.write(b'\x00')
        cls.email_att.append(small_att)
        cls.email_att.append(large_att)

    @classmethod
    def tearDownClass(cls):
        cls.ec.quit()

    def testSendUseChineseWithoutAtt(self):
        subject = '中文测试'
        body = '<p><span style="font-size:18px;color:#ff0000;font-weight:bold;">PPyTools</span>是个非常有用的工具类，' \
               '欢迎多多提意见！</p>'
        self.ec.send(self.to, self.cc, subject, body)

    def testSendWithAtt(self):
        subject = 'Test email client with Python.'
        body = '<p><span style="font-size:18px;color:#ff0000;font-weight:bold;">PPyTools</span>' \
               ' is a very useful tools classes in Python.</p> <p>With attachment file.</p>'
        self.ec.send(self.to, self.cc, subject, body, self.email_att, True)

