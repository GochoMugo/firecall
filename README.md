# Firebasin

A Python Library for the [Firebase](https://firebaseio.com/) API.

View Full documentation  [here][documentation] in a better and clean page.

## Quick Stats

[![Build Status](https://travis-ci.org/GochoMugo/firebasin.svg?branch=master)](https://travis-ci.org/GochoMugo/firebasin)

|Topic                        | Details                |
|----------------- |---------------:|
|Version                    | 0.1.2                   |
|Python                     | 2.6, 2.7, 3.2, 3.3, 3.4 |
|Development Status | Stable            |
|Last Updated            | 18th July, 2014    |

## Prerequisites

**requests** Library

This library depends on the `requests` library. If you have **NOT** installed the [requests](docs.python-requests.org/ "Requests Home Page") library yet

`sudo pip install requests` 

## Installation

To Install this library into your machine:

`sudo pip install firebasin`

## Getting Started

Get started in **two** steps.

```python
# First Step: Import the Library/Module
import firebasin

# Create a Firebase instance
my_firebase = firebasin.Firebase("https://my-firebase.firebaseio.com")

# Now you are ready to use Firebase
# For Example: (getting data from a Firebase)
def print_for_me(data):
    print("Just got this data: " + data)
my_firebase.get(point="/" callback=print_for_me)
```

## Available Methods

1. .root()
* .name()
* attr()
* parent()
* child()
* .get()
* .put()
* .delete()
* .export()
* .onChange()

# Asynchronous vs Synchronous

The methods above _(from `.get()` downwards)_ are **asynchronous**. But if you wanted to use them synchronously, just appending *_sync* to the method name. E.g. `.get_sync`

## Callbacks and Errors

Asynchronous methods allow passing a callback, an error handler or even a list of callbacks.

Data from the Firebase is passed to the callbacks. Errors are also passed to the Error handler function.

Find more information on callbacks and errors using the [Full documentation][documentation].

## Contributions and Issues

If you wanted to add a feature to the next version, you could [Fork](https://github.com/GochoMugo/firebasin/fork "Fork Me Please!!!") the repo, hack it and send a Pull Request. Lets work make this thing work for us. :-)

Incase you encounter a bug, even if you could fix it yourself, please share with your fellow Pythonista :-) at the [Issues page](https://github.com/GochoMugo/firebasin/issues "Create an issue here")

## License

Source code for **firebasin** is issued and licensed under the [MIT License](http://opensource.org/licenses/MIT "OSI Page for MIT License").

**Conquer the World with Python**

[documentation]:https://gochomugo.github.io/firebasin/ "Full Documentation on firebasin"
