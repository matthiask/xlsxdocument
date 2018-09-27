#!/usr/bin/env python
import os
from setuptools import setup

setup(
    name="xlsxdocument",
    version=__import__("xlsxdocument").__version__,
    description="Easily create XLSX documents with Django",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    author="Matthias Kestenholz",
    author_email="mk@feinheit.ch",
    url="https://github.com/matthiask/xlsxdocument/",
    packages=["xlsxdocument"],
    install_requires=["openpyxl"],
)
