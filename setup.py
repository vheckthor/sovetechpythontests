# -*- coding: utf-8 -*-
"""setup.py"""

from setuptools import setup
from setuptools import find_packages


requires = []
with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

setup(
    name='sovtech-swapi-python-test',
    version='1.0.0',
    url='',
    author='victor',
    author_email='adebayovicktor@gmail.com',
    description='Test for sovtech-swapi-python',
    packages=find_packages(),
    install_requires=requires,
)
