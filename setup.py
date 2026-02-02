from setuptools import setup
from setuptools import find_packages

long_description = '''
Longue description de transcine
'''
required = []

setup(
    name ='transcine',
    version = '0.0.1',
    description='A pyhton package for video transcription.',
    long_description=long_description,
    author='Paul Conan',
    author_email='pconan1@gmail.com',
    url='https://github.com/Paul-Conan/transcine',
    install_requires = required,
    packages= find_packages()
)