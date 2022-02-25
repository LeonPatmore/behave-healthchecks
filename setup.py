import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='behave-healthchecks',
    long_description=README,
    version='0.0.2',
    install_requires=['behave', 'healthchecks-io'],
    tests_require=[],
    packages=["behave_healthchecks"],
    author='Leon Patmore',
    description=''
)
