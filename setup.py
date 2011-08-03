from setuptools import setup, find_packages

install_requires = []

# Test if we have built-in JSON - Python 2.6+, 3.0+.
try:
  import json
except ImportError:
  

version = __import__('pyplacefinder').get_version()

setup(name='pyplacefinder',
  version=version,
  description='Python wrapper for the Yahoo! PlaceFinder API',
  author='Aaron Wallis',
  author_email='aaron.wallis@lexer.com.au',
  url='http://github.com/d2kagw/pyplacefinder',
  download_url='http://github.com/d2kagw/pyplacefinder',
  packages=find_packages(),
  install_requires=install_requires,
  keywords='geocode geocoding gis geographical maps earth distance yahoo placefinder place finder',
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Software Development :: Libraries :: Python Modules"
  ],
)