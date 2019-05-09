#!/usr/bin/python2
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(
	name='Python video annotator - module - create paths',
	version="0.3",
	description="""""",
	author=['Ricardo Ribeiro'],
	author_email='ricardojvr@gmail.com',
	url='https://bitbucket.org/fchampalimaud/pythonvideoannotator-module-createpaths',
	long_description = long_description,
    long_description_content_type = 'text/markdown',
	packages=find_packages(),	
)
