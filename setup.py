#!/usr/bin/env python3
"""Book Manager

flask-smorest example
"""

from setuptools import setup, find_packages

setup(
    name='book-manager',
    version='1.1.0',
    description='Book Manager',
    # url='',
    # author='',
    # author_email='',
    # license='',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
        'Framework:: Flask'
    ],
    keywords=[
    ],
    packages=find_packages(),
    install_requires=[
        'flask>=3.1',
        'python-dotenv>=1.0',
        'flask-smorest>=0.46',
        'marshmallow>=4.0',
        'sqlalchemy>=2.0',
        'sqlalchemy-utils>=0.42',
        'flask-sqlalchemy>=3.1',
        'flask-jwt-extended>=4.7',
        'Flask-WTF>=1.2'
    ],
    extras_require={
        'dev': [
            'pytest>=8.2',
            'pytest-cov>=5.0',
            'ruff>=0.5',
            'pre-commit>=3.7'
        ]
    }
)
