import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''

import tracking

setup(name='trackingcorreoschile',
      version=tracking.__version__,
      description=tracking.__doc__,
      author=tracking.__author__,
      author_email='raulsetron@gmail.com',
      packages=find_packages(),
      url='https://github.com/rulz/trackingcorreoschile',
      platforms=['all'],
      classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],
      tests_require=['nose>=1.0', 'coverage'],
      install_requires=[
        'BeautifulSoup==3.2.1',
    ],)