# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

import django-link-utils

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django-link-utils.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-link-utils',
    version=version,
    description='Your project description goes here',
    long_description=readme + '\n\n' + history,
    author='Raphi Gaziano',
    author_email='r.gaziano@gail.com  ',
    url='https://github.com/raphigaziano/django-link-utils',
    packages=[
        'django-link-utils',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-link-utils',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)