#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='bro-log-parser',
    version='1.0.0',
    url='https://github.com/elnappo/bro-log-parser',
    license='MIT',
    author='Fabian Weisshaar',
    author_email='elnappo@nerdpol.io',
    description='Simple logfile parser for Bro IDS',
    keywords='logfile parser',
    platforms='any',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    py_modules=['brologparse'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
