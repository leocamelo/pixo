import json
from setuptools import setup, find_packages


with open('package.json') as f:
    package = json.load(f)

setup(
    name=package['name'],
    version=package['version'],
    description=package['description'],
    author='@leocamelo',
    author_email='leonardocamelo.nave@gmail.com',
    url='https://github.com/leocamelo/pixo',
    packages=find_packages()
)
