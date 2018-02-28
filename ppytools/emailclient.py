# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from excepts.emailexcept import *
from lang import strings
from ppytools.compresshelper import zipFile
from ppytools.lang.timerhelper import timeMeter

import email.MIMEBase
import email.MIMEMultipart
import email.MIMEText
import logging
import os
import smtplib
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

logger = logging.getLogger(__name__)

'''When attach file size grate then 4MB will compress
'''
MAX_ATT_FILE_SIZE = 4 * 1024 * 1024
CHARSET_ENCODING = 'UTF-8'


class EmailClient(object):
    """EmailClient

        A email client utility that in send monitor message, daily report or others way.
        Remember that quit SMTP server connect after send email.
    Attributes:
        _del_files: attachment files list
        smtp_server: Email SMTP server host name
        smtp_port: Email SMTP protocol port
        smtp_user: Email SMTP access user
        smtp_pswd: Email SMTP access password
        smtp_mode: Email SMTP protocol encryption: PUB, TLS, SSL
    """

    _del_files = []

    def __init__(self, server, port, user, passwd, mode='PUB'):
        self.smtp_server = server
        self.smtp_port   = int(port)
        self.smtp_user   = user
        self.smtp_pswd   = passwd
        self.smtp_mode   = mode
        self.smtp_conn   = None
        self.__login__()

    def __login__(self):
        """Login email SMTP server under different mode

        :return: SMTP server connect
        """
        if self.smtp_conn is None:
            if strings.equalsignore(self.smtp_mode, 'TLS'):
                logger.debug('Email SMTP server used TLS mode protocol.')
                self.smtp_conn = smtplib.SMTP(self.smtp_server, self.smtp_port)
                self.smtp_conn.starttls()
            elif strings.equalsignore(self.smtp_mode, 'SSL'):
                logger.debug('Email SMTP server used SSL mode protocol.')
                self.smtp_conn = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            else:
                logger.debug('Email SMTP server used PUBLIC mode protocol.')
                self.smtp_conn = smtplib.SMTP(self.smtp_server, self.smtp_port)
                self.smtp_conn.ehlo()
            self.smtp_conn.ehlo()
            self.smtp_conn.login(self.smtp_user, self.smtp_pswd)

        logger.info('Email SMTP server connect ready.')
        return self.smtp_conn

    def __add_att__(self, email_cnt, att, delete):
        """Add attachments into email content

        :param att: attachments
        :return: None
        """
        content_type = 'application/octet-stream'
        maintype, subtype = content_type.split('/', 1)
        if att:
            for att_path in att:
                att_file_size = os.path.getsize(att_path)
                if att_file_size > MAX_ATT_FILE_SIZE:
                    att_path = zipFile(att_path)
                    '''add compress into remove list
                    '''
                    self._del_files.append(att_path)

                with open(att_path, 'rb') as att_tmp:
                    try:
                        att_file = email.MIMEBase.MIMEBase(maintype, subtype)
                        att_file.set_payload(att_tmp.read())
                        email.Encoders.encode_base64(att_file)
                        att_file.add_header('Content-Disposition', 'attachment',
                                            filename=os.path.basename(att_path).encode('UTF-8'))
                        email_cnt.attach(att_file)
                    except Exception, e:
                        raise AppendEmailAttException('Append email attach[%s] failed!!! Case: %s', att_path, str(e))

            self._del_files.extend(att)
            if delete:
                for path in self._del_files:
                    try:
                        os.remove(path.decode('UTF-8'))
                    except IOError, e:
                        raise DeleteEmailAttException('Delete email attach[%s] failed!!! Case: %s', path, str(e))
                '''flush memory
                '''
                self._del_files[:] = []

    @timeMeter()
    def send(self, to, cc, subject, body, atts=None, delete=False):
        """Send an email action.

        :param to: receivers list
        :param cc: copy user list
        :param subject: email title
        :param body: email content body
        :param atts: email attachments
        :param delete: whether delete att
        :return: True or False
        """
        email_cnt = email.MIMEMultipart.MIMEMultipart()
        email_cnt['From'] = self.smtp_user
        email_cnt['To'] = ';'.join(to)
        email_cnt['Cc'] = ';'.join(cc)
        email_cnt['Subject'] = subject.encode(CHARSET_ENCODING)
        email_cnt['Date'] = email.Utils.formatdate()
        body_html = email.MIMEText.MIMEText(body.encode(CHARSET_ENCODING), _subtype='html', _charset=CHARSET_ENCODING)
        email_cnt.attach(body_html)

        self.__add_att__(email_cnt, atts, delete)

        try:
            self.smtp_conn.sendmail(self.smtp_user, to+cc, email_cnt.as_string())

            with_att_msg = 'Empty'
            if atts:
                for i,att  in enumerate(atts):
                    atts[i] = att[att.rindex('/')+1:]

                with_att_msg = ','.join(atts)
                '''Flush memory
                '''
                atts[:] = []

            logger.info('Send email[%s] success.', subject)
            logger.info('To users: %s.', ','.join(to+cc))
            logger.info('With attachments: %s.', with_att_msg)
        except Exception, e:
            raise SendEmailException("Send email[%s] failed!!! Case: %s" % (subject, str(e)))

    def quit(self):
        """Quit SMTP server

        :return: None
        """
        if self.smtp_conn:
            self.smtp_conn.quit()


