# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='Practica 3',
    version='0.1.0',
    description='Practica 3',
    long_description=readme,
    author='Antonio Muñoz, David Ayuso, Alejando Frutos, Enrique Checa',
    url='',
    packages=find_packages(exclude=('tests', 'docs'))
)
