# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.lang.timer_helper import timeMeter
from pyhive import hive

import logging

logger = logging.getLogger(__name__)


class HiveClient(object):
    """HiveClient

        Use Thrift server connect Hive server and execute any action.
    Attributes:
        host: hive server hostname or IP address
        port: hive server connect port
        user: hive server login user
        db:   hive server operate database name
        conn: hive server connect instance
    """
    def __init__(self, host, port, user=None, db='default'):
        self.host = host
        self.port = port
        self.user = user
        self.db   = db
        self.conn = None
        self.getConn()

    def getConn(self):
        if self.conn is None:
            conn_args = {'host': self.host, 'port': self.port, 'username': self.user, 'database': self.db}
            try:
                self.conn = hive.connect(**conn_args)
            except Exception, e:
                raise Exception('Get Hive server connect failed!!!', e)

        return self.conn

    def closeConn(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def closeCursor(self, cur):
        try:
            cur
        except Exception as e:
            logger.error('Hive server connect is not ready!!! Err: {}'.format(str(e)))
        else:
            cur.close()

    @timeMeter()
    def execQuery(self, sql):
        result = []
        try:
            cur = self.getConn().cursor()
            cur.execute(sql)
            for row in cur.fetchall():
                result.append(
                    [cell.decode('UTF-8') if cell is not None and isinstance(cell, str) else cell for cell in row])
        except Exception, e:
            raise Exception('Execute hive client query failed!!!, Case: {}'.format(str(e)))
        finally:
            self.closeCursor(cur)
            records = len(result)

        logger.info('Hive client query completed. Records found: %d', records)

        return result, records

    @timeMeter()
    def execUpdate(self, sql):
        try:
            cur = self.getConn().cursor()
            cur.execute(sql)
        except Exception, e:
            raise Exception("Execute hive client update failed!!! Case: {}".format(str(e)))
        finally:
            self.closeCursor(cur)

        logger.info('Hive client update complete.')

    @timeMeter()
    def execCount(self, sql):
        try:
            cur = self.getConn().cursor()
            cur.execute(sql)
            count = cur.fetchone()
        except Exception, e:
            raise Exception("Execute hive client count failed. Case: %s" % str(e))
        finally:
            self.closeCursor(cur)

        logger.info('Hive client count completed, Found %d items.', count[0])

        return count[0]
