#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys

from setuptools import setup


name = 'drf_fields_permissions'
package = 'fields_permissions'
description = 'Permissions for django-rest fields'
url = 'https://github.com/BohdanYatsyna/drf_fields_permissions'
author = 'starnavi.io'
author_email = 'hello@starnavi.io'
license = 'BSD'


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version(package)


# # setup for manual publishing to PyPI
# if sys.argv[-1] == 'publish':
#     if os.system("pip freeze | grep wheel"):
#         print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
#         sys.exit()
#     os.system("python setup.py sdist upload")
#     os.system("python setup.py bdist_wheel upload")
#     print("You probably want to also tag the version now:")
#     print("  git tag -a {0} -m 'version {0}'".format(version))
#     print("  git push --tags")
#     sys.exit()


with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=[
        'Django>=4.0,<5.0',
        'djangorestframework>=3.13,<3.15',
        'pytz>=2022.6',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
