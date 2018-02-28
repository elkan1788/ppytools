# -*- -*- coding: utf-8 -*- -*-
# __author__ = 'elkan1788@gmail.com'

from ppytools.lang.timerhelper import timeMeter

import codecs
import csv
import logging

logger = logging.getLogger(__name__)

BOM_FORMAT = codecs.BOM_UTF8

@timeMeter()
def write(path, head, data):
    try:
        with open(unicode(path, 'UTF-8'), 'wb') as csv_file:
            csv_file.write(BOM_FORMAT)
            writer = csv.writer(csv_file)

            if head is not None:
                writer.writerow(head)

            for row in data:
                writer.writerow(row)

            logger.info('Write a CSV file successful. --> %s', path)
    except Exception, e:
        raise Exception("Write a CSV file failed!!! --> %s, Case: %s" % (path, str(e)))

@timeMeter()
def getIdNameDict(path):
    id_name_dict = dict()
    try:
        with open(path, 'rb') as tmp:
            reader = csv.reader(tmp)
            for line in reader:
                id_name_dict[line[0]] = line[1]
    except Exception, e:
        raise Exception("Read CSV file was failed!!! --> %s Case: %s" % (path, str(e)))
    return id_name_dict
