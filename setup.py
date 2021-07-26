#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import admin_model_list_order

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = admin_model_list_order.__version__

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-admin-model-list-order',
    version=version,
    description="""Custom ordering for models in the admin app.""",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author='Vikrant Arya',
    author_email='vikrantarya21@gmail.com',
    url='https://github.com/Vikrant-Arya/django-admin-model-list-order',
    packages=[
        'admin_model_list_order',
    ],
    include_package_data=True,
    install_requires=[
        'django'
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-admin-model-list-order',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
