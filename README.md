
# :fire: Firecall

A Python Helper Library for [Firebase](https://firebase.com/).

View Full documentation [here][documentation].

> __Firecall__ was previously named __Firebasin__. The change of name
> was motivated by name clashes with other Firebase helper libraries.


## Quick Stats

[![Build Status](https://travis-ci.org/GochoMugo/firecall.svg?branch=master)](https://travis-ci.org/GochoMugo/firecall)

| Topic | Details |
|--------|--------:|
| Version | 1.0.1 |
| Python | 2.6, 2.7, 3.2, 3.3, 3.4 |
| Development Status | Stable |
| Last Updated | 30th May, 2015 |


## Installation

To Install this library, you have the following options:

1. Using [pip](https://pip.pypa.io/):

  ```bash
  ⇒ pip install firecall
  ```

1. Cloning the Github repo:

  ```bash
  ⇒ git clone https://github.com/GochoMugo/firecall
  ⇒ cd firecall
  ⇒ python setup.py install
  ```

> :information_source: If a `Permission denied` error occurs, you simply need to use `sudo`


## Getting Started

Get started is easy:

```python
# Import firecall
import firecall

# Create a firebase instance
my_firebase = firecall.Firebase("https://my-firebase.firebaseio.com")

# Now you are ready to use Firebase
# For example: (getting data from a Firebase)
def print_for_me(data):
    print("Just got this data: " + data)

my_firebase.get(point="/" callback=print_for_me)
```


## Available Methods

1. firebase#root()
1. firebase#name()
1. firebase#attr()
1. firebase#parent()
1. firebase#child()
1. firebase#get()
1. firebase#put()
1. firebase#delete()
1. firebase#export()
1. firebase#onChange()


# Asynchronous vs Synchronous

The methods above _(from `.get()` downwards)_ are **asynchronous**. But if you wanted to use them synchronously, just appending *_sync* to the method name. E.g. `.get_sync`

**Asynchronousity** is at the heart of the Implementation.


## Callbacks and Errors

Asynchronous methods allow passing a callback, an error handler or even a list of callbacks. Data from the Firebase is passed to the callbacks. Errors are also passed to the Error handler function.

Find more information on callbacks and errors using the [Full documentation][documentation].


## Contributions and Issues

If you wanted to add a feature to the next version, you could [Fork](https://github.com/GochoMugo/firecall/fork "Fork Me Please!!!") the repo, hack it and send a Pull Request.

Incase you encounter a bug, even if you could fix it yourself, please share at the [Issues page](https://github.com/GochoMugo/firecall/issues "Create an issue here")


## License

__The MIT License (MIT)__

Copyright (c) 2014-2015 Gocho Mugo <mugo@forfuture.co.ke>


**Conquer the World with Python**


[documentation]:https://gochomugo.github.io/firecall/ "Full Documentation on Firecall"
