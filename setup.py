#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from os.path import join, dirname

from setuptools import setup

with open(join(dirname(__file__), 'pygraphy', '__init__.py'), 'r') as f:
    version = re.match(r".*__version__ = '(.*?)'", f.read(), re.S).group(1)

install_requires = [
    "GraphQL-core-next>=1.1.0,<1.2.0"
]

dev_requires = [
    "flake8>=3.7.7",
    "pytest>=5.0.0",
]


setup(
    name="pygraphy",
    version=version,
    description="A modern pythonic implementation of GraphQL.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="python graphql",
    author="Tzu-sing Gwo",
    author_email="zi-xing.guo@ubisoft.com",
    url="https://github.com/ethe/pygraphy",
    license="MIT",
    packages=['pygraphy'],
    include_package_data=True,
    install_requires=install_requires,
    tests_require=dev_requires,
    python_requires=">=3.7,<4",
    extras_require={
        "dev": dev_requires,
        "web": ["starlette>=0.12.1,<0.13.0"]
    },
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
