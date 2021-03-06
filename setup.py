import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "nsnitro",
    version = "0.0.1",
    author = "Vladimir Lazarenko",
    author_email = "vllazarenko@ebay.com",
    description = ("A simple library to control Citrix Netscaler 9.2+ with NITRO API."),
    license = "GPL",
    keywords = "citrix netscaler nitro api",
    url = "http://packages.python.org/nsnitro",
    py_modules=['nsnitro', 'nsresources'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL License",
    ],
    install_requires=[
        "httplib2",
        "argparse",
    ],
    data_files=[
        ('/usr/bin', ['contrib/nsnitrocmd.py'])
    ],
)
