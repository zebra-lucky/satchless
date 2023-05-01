#! /usr/bin/env python
from setuptools import setup, find_packages


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules']

setup(
    name='satchless',
    author='Mirumee Software',
    author_email='hello@mirumee.com',
    description='An e-commerce framework',
    license='BSD',
    version='1.1.3.1',
    url='http://satchless.com/',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    platforms=['any'],
    install_requires=['prices>=0.5,<1.0.0'],
    include_package_data=True,
    zip_safe=True)
