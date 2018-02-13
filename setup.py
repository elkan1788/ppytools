# coding: utf-8
# __author__ = 'elkan1788@gmail.com'

from setuptools import setup, find_packages
from pip.req import parse_requirements

INSTALL_REQ = parse_requirements('requirements.txt', session='hack')
REQUIRES = [str(ir.req) for ir in INSTALL_REQ]

"""
PPyTools setup scripts.
"""
setup(
    name='ppytools',
    version='1.0.1',
    description='utility that in **Python** project.',
    author='elkan1788',
    author_email='elkan1788@gmail.com',
    license='MIT',
    install_requires=REQUIRES,
    packages=find_packages()
)
