#!/usr/bin/env python3
"""Book Manager

flask-smorest example
"""

from setuptools import setup, find_packages

setup(
    name='book-manager',
    version='1.0',
    description='book Manager',
    # url='',
    # author='',
    # author_email='',
    # license='',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Framework:: Flask'
    ],
    keywords=[
    ],
    packages=find_packages(),
    install_requires=[
        'flask>=1.0.0',
        'python-dotenv>=0.9.0',
        'flask-smorest>=0.22.0',
        'marshmallow>=3.0.0',
        'sqlalchemy>=1.2.5',
        'sqlalchemy-utils>=0.32.21',
        'flask-sqlalchemy>=2.3.2',
        'marshmallow_sqlalchemy>=0.23.1',
        'Flask-Marshmallow>=0.13.0',
        'flask-jwt-extended>=3.24.1',
        'Flask-WTF==0.14.3'
    ],
    extras_require={
        'testing': [
            'pytest==5.4.3',
            'coverage==5.2.1',
            'pylint==2.5.3',
            'pytest-cov==2.10.0'
        ]}
)
