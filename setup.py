#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='bro-log-parser',
    version='0.1.0',
    packages=[''],
    url='https://github.com/elnappo/bro-log-parser',
    license='MIT',
    author='Fabian Weisshaar',
    author_email='elnappo@nerdpol.io',
    description='Simple logfile parser for Bro IDS',
    keywords='logfile parser',
    platforms='any',
    py_modules=['brologparse'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
    ],
)
