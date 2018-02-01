#!/usr/bin/python
from distutils.core import setup

setup(
  name='coinone.py',
  version='0.1.0',
  description='Simple coinone api wrapper',
  license='Apache License 2.0',
  packages=[
    'coinone',
    'coinone.api',
    'coinone.api.v1',
    'coinone.api.v2',
  ],
  install_requires=['requests']
)
