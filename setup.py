from setuptools import setup, find_packages

from pixo import __version__

setup(
    name='pixo',
    version=__version__,
    description='Draw tags over your photos',
    author='@leocamelo',
    author_email='leonardocamelo.nave@gmail.com',
    url='https://github.com/leocamelo/pixo',
    packages=find_packages()
)
