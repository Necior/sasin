#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    author="Adrian Sadłocha",
    author_email="adrian@sadlocha.eu",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="A one way PLN → sasin converter",
    install_requires=[],
    license="MIT license",
    include_package_data=True,
    keywords="sasin",
    long_description=open("./README.md").read(),
    long_description_content_type='text/markdown',
    name="sasin",
    py_modules=["sasin"],
    setup_requires=[
        "pytest-runner",
    ],
    test_suite="tests",
    tests_require=[
        "pytest>=3",
    ],
    url="https://github.com/Necior/sasin",
    version="1.0.0",
    zip_safe=False,
)
