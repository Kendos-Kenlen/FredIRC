#! /usr/bin/env python
#
# Copyright (c) 2013 Tobias Marquardt
#
# Distributed under terms of the (2-clause) BSD  license.


import sys

if sys.version < '3.3':
    print('ERROR: At least python version 3.3 is required!')
    sys.exit(1)

import os
from setuptools import setup

if sys.version_info[0:2] == (3,3):
    dependencies = ['asyncio']
else:
    dependencies = []

def read(file):
    """ Utility function to the the README file. """
    return open(os.path.join(os.path.dirname(__file__), file)).read()

setup(
    name='FredIRC',
    version='0.1',
    author='Tobias Marquardt',
    author_email='tm@tobix.eu',
    description=('An easy-to-use event driven IRC client library well-suited '
                    'for the development of bots.'),
    packages=['fredirc', 'tests'],
    install_requires=dependencies,
    license='BSD',
    keywords='irc client library bot',
    url='http://fredirc.tobix.eu',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    )
