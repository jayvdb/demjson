# Python package setup script        -*- coding: utf-8 -*-
from setuptools import setup

name = 'demjson'
version = '2.2.4'

setup( name=name,
       version=version,
       py_modules=[name],
       scripts=['jsonlint'],
       author='Deron Meranda',
       author_email='deron.meranda@gmail.com',
       url='http://deron.meranda.us/python/%s/'%name,
       download_url='http://deron.meranda.us/python/%(name)s/dist/%(name)s-%(version)s.tar.gz'\
           % {'name':name, 'version':version},
       description='encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159',
       long_description="""
The "demjson" module, and the included "jsonlint" script, provide methods
for encoding and decoding JSON formatted data, as well as checking JSON
data for errors and/or portability issues.  The jsonlint command/script
can be used from the command line without needing any programming.

Although the standard Python library now includes basic JSON support
(which it did not when demjson was first written), this module
provides a much more comprehensive implementation with many features
not found elsewhere.  It is especially useful for error checking or
for parsing JavaScript data which may not strictly be valid JSON data.

""".strip(),
       license='GNU LGPL 3.0',
       keywords=['JSON','jsonlint','JavaScript','UTF-32'],
       platforms=[],
       classifiers=["Development Status :: 5 - Production/Stable",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                    "Operating System :: OS Independent",
                    "Programming Language :: Python :: 2",
                    "Programming Language :: Python :: 3",
                    "Topic :: Software Development :: Libraries :: Python Modules",
                    "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
                    ],
       use_2to3=True,
       test_suite="test.test_demjson",
       )

