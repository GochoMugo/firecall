# Firebasin

A Python Library for the [Firebase](https://firebaseio.com/) API

## Quick Stats

|Topic                         | Details               |
|------------------|---------------|
|Version                    | 0.0.0                  |
|Development Status | 3 - Alpha**        |
|Last Updated            | 28th May, 2014   |

## Prerequisites

**requests** Library

This library depends on the `requests` library. If you have **NOT** installed the **requests** library yet

`sudo pip install requests` 

## Installation

To Install this library into your machine:

`sudo pip install firebasin`

## Getting Started

1.  Import the `firebasin` library

    `import firebasin`

2.  Create a Firebase instance

    `my_firebase = firebasin.Firebase("https://my_firebase_name.firebaseio.com")`

Firebase is now ready to be used. It's time to conquer the World.

### Methods

A Firebase instance has different methods that let you transact with it. The methods shown below are **Synchronous**. This means that:
    
* Python won't wait for the response, it will continue executing following lines of code
* You should NOT assign return value to a variable. Doing this will always assign `None`
* You will have to use a callback to manipulate returned data from a request

**Note:** There are also **Asynchronous** methods you can use. Read along to see how to use them.
    
I have tried as much as possible to mimic the Javascript API. Thus the following methods:

_.root()_

    Get a Firebase reference to the root of the Firebase. 

* Requires No arguments.
* Returns a String

Example:

```python
print my_firebase.root()
```

_.name()_

Get the last token of this location's URL.

* Requires No arguments
* Returns a String

Example:

```python
print my_firebase.name()
```
_.parent()_

Get a Firebase instance with the parent Location as its URL

* Requires No arguments
* Returns a new Firebase Instance

Example:

```python
new_parent = my_firebase.parent()
```

_.child(**kwargs)_

Get a Firebase instance with a child location as its URL

* Requires:
    * point="relative_URL_to_child"
* Returns a Firebase Instance

Example:

```python
new_child = my_firebase.child(point="/child")
```

_.get(**kwargs)_

Get data a particular location on your Firebase

* Requires:
    * point="location_to_read"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
* Returns a String containing the Data

Example:

```python
# Callback function definition
def hello(data):
    print data
    
# Making a 'GET' request
my_firebase.get(point="/child", auth="Ja2f29f4Gsk2d3bhxW2d8vDlK", callback=hello)
```

_.put(**kwargs)_

Write data into your Firebase

* Requires:
    * point="location_to_read"
    * data="data_to_put"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
* Returns a String containing the Data you just put

_.delete(**kwargs)_

Delete data from your Firebase

* Requires:
    * point="location_to_delete"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
* Returns string saying `null`

_export(**kwargs)_

Export data from a location on your Firebase

* Requires:
    * point="location_to_read"
    * auth="access_token" (Optional)
    * path="UNIX_path_to_file_to_write_to" (Optional)
    * callback=name_of_a_function (Optional)
* Returns a String containing the Data exported

**Note:** if the `path` argument is not given, this will behave similar to `.get(**kwargs)`

### Asynchronous Methods

The methods are also available in asynchronous flavor. To get a method work synchronously, append "_sync" to the name of the method.

Example:

```python
user = my_firebase.get_sync("/user")
# Python will wait for the response before executing the next line of code
# Callback arguments passed will be ignored
```
