from distutils.core import setup
import firecall


setup(
    name="firecall",
    packages=["firecall"],
    version="1.0.1",
    author="Gocho Mugo I",
    author_email="mugo@forfuture.co.ke",
    url="https://gochomugo.github.io/firecall/",
    download_url="https://github.com/GochoMugo/firecall/zipball/master",
    description="Python helper library for Firebase <https://firebase.com>",
    keywords=["firebase", "firebasin", "REST", "API", "firecall"],
    long_description=firecall.__doc__,
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
