from setuptools import setup, find_packages

from pyxo import __version__


setup(
    name='pyxo',
    version=__version__,
    description='Draw tags over your photos',
    license='MIT',
    author='@leocamelo',
    author_email='leonardocamelo.nave@gmail.com',
    url='https://github.com/leocamelo/pyxo',
    packages=find_packages()
)
