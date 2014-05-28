# Importing setup() function
from distutils.core import setup
# Calling the setup() function
setup(
    name = "firebasin",
    packages = ["firebasin"],
    version = "0.0.0",
    author = "Gocho Mugo I",
    author_email = "gochomugo.developer@gmail.com",
    url = "https://gochomugo.github.io/firebasin/",
    description = "Python library for Firebase API",
    long_description = "A Python Implementation of the Firebase API. http://firebase.com/",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
