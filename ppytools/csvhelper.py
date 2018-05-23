# -*- -*- coding: utf-8 -*- -*-
# __author__ = 'elkan1788@gmail.com'

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from ppytools.lang.timerhelper import timemeter

import csv
import logging

logger = logging.getLogger(__name__)


@timemeter()
def write(path, head, data):
    try:
        with open(path, 'w', newline='', encoding='UTF-8-sig') as csv_file:
            writer = csv.writer(csv_file)
            if head is not None:
                writer.writerow(head)
            writer.writerows(data)
            logger.info('Write a CSV file successful. --> %s', path)
    except Exception as e:
        raise Exception("Write a CSV file failed!!! --> %s, Case: %s" % (path, str(e)))


@timemeter()
def getIdNameDict(path):
    id_name_dict = dict()
    try:
        with open(path, 'r', encoding='UTF-8-sig') as tmp:
            reader = csv.reader(tmp)
            for line in reader:
                id_name_dict[line[0]] = line[1]
    except Exception as e:
        raise Exception("Read CSV file was failed!!! --> %s Case: %s" % (path, str(e)))
    return id_name_dict
