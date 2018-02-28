# -*- coding: utf-8 -*-
# __author__ = 'elkan1788@gmail.com'

from setuptools import setup, find_packages
from pip.req import parse_requirements

INSTALL_REQ = parse_requirements('requirements.txt', session='hack')
REQUIRES = [str(ir.req) for ir in INSTALL_REQ]

"""
PPyTools setup scripts.
"""
setup(
    name='ppytools2',
    version='1.1.0',
    author='elkan1788',
    author_email='elkan1788@gmail.com',
    description='A common library utility that in Python project.',
    long_description=open("README.rst").read(),
    license='Apache License V2.0',
    url='https://github.com/elkan1788/ppytools',
    install_requires=REQUIRES,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries'
    ]
)
