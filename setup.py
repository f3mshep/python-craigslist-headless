#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('VERSION.txt', 'r') as v:
    version = v.read().strip()

with open('REQUIREMENTS.txt', 'r') as r:
    requires = r.read().split()

with open('README.rst', 'r') as r:
    readme = r.read()

setup(
    name='python-craigslist_headless',
    packages=['craigslist_headless'],
    version=version,
    description=('Simple Craigslist wrapper.'),
    long_description=readme,
    author='Julio M Alegria, Alexandra Wright',
    author_email='superbiscuit@gmail.com',
    url='https://github.com/f3mshep/python-craigslist-headless',
    install_requires=requires,
    license='MIT-Zero'
)
