'''
firebasin
=======
A Python Implementation of the
`Firebase REST API <https://www.firebase.com/docs/rest-api.html>`_.

A complete and updated documentation of this Module may be found at
`firebasin's github project page
 <https://gochomugo.github.io/GochoMugo/firebasin>`_.

Source code is licensed under the MIT License.
 Copyright (c) 2014 GOCHO MUGO
'''

from distutils.core import setup


setup(
    name="firebasin",
    packages=["firebasin"],
    version="0.1.2",
    author="Gocho Mugo I",
    author_email="gochomugo.developer@gmail.com",
    url="https://gochomugo.github.io/firebasin/",
    download_url="https://github.com/GochoMugo/firebasin/zipball/master",
    description="Python library for Firebase API",
    keywords=["firebase", "firebasin", "REST", "API"],
    long_description=__doc__,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    install_requires=["requests"]
)
