import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name='bagelchat',
    version='0.1',
    author='Kendrick Tan',
    author_email='kendricktan0814@gmail.com',
    description=('Simply CLI based serverless lan chat with encryption'),
    keywords='lan chat secure',
    url='http://kendricktan.com',
    packages=['bagelchat'],
    long_description=read('README.txt'),    
)