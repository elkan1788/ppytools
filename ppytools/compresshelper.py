# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

import logging
import os
import tarfile
import zipfile

logger = logging.getLogger(__name__)


def zipFile(source):
    """Compress file under zip mode
        when compress failed with return source path
    :param source: source file path
    :return: zip file path
    """
    source = source.decode('UTF-8')
    target = source[0:source.rindex(".")] + '.zip'
    try:
        with zipfile.ZipFile(target, 'w') as zip_file:
            zip_file.write(source, source[source.rindex('/'):], zipfile.ZIP_DEFLATED)
            zip_file.close()
            __cps_rate__(source, target)
    except IOError, e:
        logger.error('Compress file[%s] with zip mode failed. Case: %s', source, str(e))
        target = source

    return target


def tarFile(source):
    """Compress file under tar mode
        which type more popular use in Unix operating system
        when compress failed with return source path
    :param source: source file path
    :return: zip file path
    """
    source = source.decode('UTF-8')
    target = source[0:source.rindex('.')] + '.tar.gz'

    try:
        with tarfile.open(target, "w:gz") as tar_file:
            tar_file.add(source, arcname=source[source.rindex("/"):])
            __cps_rate__(source, target)
    except IOError, e:
        logger.error('Compress file[%s] with zip mode failed. Case: %s', source, str(e))
        target = source

    return target


def __cps_rate__(source, target):
    """Calculate file compress rate

    :param source: source file path
    :param target: target file path
    """
    source_file_size = os.path.getsize(source)
    target_file_size = os.path.getsize(target)
    cmp_rate = (source_file_size - target_file_size) / float(source_file_size)
    cmp_rate = round(cmp_rate, 4)
    logger.info('File\'s [%s] compress rate is %s%%.', os.path.basename(source), cmp_rate * 100)