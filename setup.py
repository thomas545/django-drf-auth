#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


setup(
    name='django-drf-auth',
    version='0.1',
    packages=find_packages(),
    description='REST API endpoints for Authentication and Registration',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Thomas Adel',
    author_email='thomas.adel31@gmail.com',
    url='https://github.com/thomas545/django-drf-auth/',
    keywords='django drf auth rest-framework-authentication api',
    zip_safe=False,
    license='MIT',
    install_requires=[
        'Django>=2.0',
        'djangorestframework>=3.1.3',
        'six>=1.9.0',
        'django-allauth>=0.34.0',
        'django-rest-auth>=0.9.2',
        'djangorestframework-jwt==1.11.0',
        'celery>=4.0',
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)