# Firebasin

A Python Library for the [Firebase](https://firebaseio.com/) API

## Quick Stats

|Topic                        | Details                |
|----------------- |---------------|
|Version                    | 0.1.0                   |
|Python                     | 2.7                      |
|Development Status | 3 - Alpha            |
|Last Updated            | 27th June, 2014    |

> The Development Status of this Library warrants me to say that this API will keep growing. That's a good thing, right?

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
    
While creating the Firebase instance, you might pass an access token to `auth` argument like shown below. The access token will persist across all transactions with the Firebase, unless you explicitly pass another access token to a method.

```python
my_firebase = firebasin.Firebase("https://my_firebase_name.firebaseio.com", auth="access_token_here")
# Ensure that you have defined the function you pass to "error=".
```

Firebase is now ready to be used. It's time to conquer the World.

### Basic Methods

These are the basic methods available to any Firebase

`.root()`

Get a Firebase reference to the root of the Firebase. 

* Requires No arguments.
* Returns a String

Example:

```python
print my_firebase.root()
```

`.name()`

Get the last token of this location's URL.

* Requires No arguments
* Returns a String

Example:

```python
print my_firebase.name()
```
`.parent()`

Get a Firebase instance with the parent Location as its URL

* Requires No arguments
* Returns a new Firebase Instance

Example:

```python
new_parent = my_firebase.parent()
```

`.child(**kwargs)`

Get a Firebase instance with a child location as its URL

* Requires:
    * point="relative_URL_to_child"
* Returns a Firebase Instance

Example:

```python
new_child = my_firebase.child(point="/child")
```

### Asynchronous Methods

A Firebase instance has different methods that let you transact with it. The methods shown below are **Asynchronous**. This means that:
    
* Python won't wait for the response, it will continue executing following lines of code
* You should NOT assign return value to a variable. Doing this will always assign `None`
* You will have to use a callback to manipulate returned data from a request

**Note:** There are also **Synchronous** methods you can use. Read along to see how to use them.

`.get(**kwargs)`

Get data a particular location on your Firebase

* Requires:
    * point="location_to_read"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
    * error=name_of_a_function (Optional)
* Returns `None`. Data fetched is passed to the callback function, if specified.

Example:

```python
# Callback function definition
def hello(data):
    print data
    
# Making a 'GET' request
my_firebase.get(point="/child", auth="Ja2f29f4Gsk2d3bhxW2d8vDlK", callback=hello)
```

`.put(**kwargs)`

Write data into your Firebase

* Requires:
    * point="location_to_read"
    * data="data_to_put"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
    * error=name_of_a_function (Optional)
* Returns `None`. Data you just put is passed to the callback function, if specified.

`.delete(**kwargs)`

Delete data from your Firebase

* Requires:
    * point="location_to_delete"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
    * error=name_of_a_function (Optional)
* Returns `None`. A string saying `null` is passed to the callback function, if specified.

`.export(**kwargs)`

Export data from a location on your Firebase

* Requires:
    * point="location_to_read"
    * auth="access_token" (Optional)
    * path="UNIX_path_to_file_to_write_to" (Optional)
    * callback=name_of_a_function (Optional)
    * error=name_of_a_function (Optional)
* Returns `None`. Data you just exported is passed to the callback function, if specified.

**Note:** if the `path` argument is not given, this will behave similar to `.get(**kwargs)`

`onChange(**kwargs)`

Poll for changes at a Location on your Firebase.

* Requires:
    * point="location_to_read"
    * auth="access_token" (Optional)
    * callback=name_of_a_function (Optional)
    * error=name_of_a_function (Optional)
    * ignore_error=True (Optional) - Whether to keep watching incase of an error or make it Stop
* Returns an Object representing the Watch. This object has one method:
    *   _.stop(number_of_seconds)_ - Passing an integer or float will cause the watch to be stopped after the specified number of seconds. If no number is passed, the watch will be stopped as soon as Possible.

```python
watch = my_firebase.onChange(point="/watch_here", callback=keep_printing) # Creates a watch Object
watch.stop(20) # The Watch will be stopped after 20 seconds
```

**Note:** 
* there's **No** synchronous flavor of this method. For obvious reasons.
* the stopping of a watch may take longer or shorter time for the action to kick in. This depends on your System.


### Synchronous Methods

The asynchronous methods are also available in synchronous flavor. To get a method work synchronously, append "_sync" to the name of the method.

Example:

```python
user = my_firebase.get_sync("/user")
# Python will wait for the response before executing the next line of code
# Callback arguments passed will be ignored
```

### Callbacks and Errors

In all the asynchronous methods, a **Callback** can be assigned. The callback will be executed once response is received. In the case of `.onChange()` method, the callback will be inserted every time data changes at the point specified. 

Functions assigned to **error** are executed when an error occurs while executing the action. The following errors may be caught:

1. `EnvironmentError`: This is caused by Trying to access a non-existant Firebase or Security Rules violation while trying to execute a query
2. `KeyError`: This is caused when you do **not** pass a required argument to any function
3. `ConnectionError`: This will occur mostly due to Network problems

If you wanted to catch errors according to this classes, you could do:

```python
def caught_an_error(err):
    if err.__class__.__name__ == "KeyError":
        print("KeyError: " + str(err))
    elif err.__class__.__name__ == "EnvironmentError":
        print("EnvironmentError: " + str(err))
    elif err.__class__.__name__ == "ConnectionError":
        print("ConnectionError: " + str(err))
    else:
        print(err.__class__.__name__ + str(err))
```

**Note:** All callbacks and error handling functions should be defined before assigning them to a method. Or else you love Bugs. 

## Issues

Incase you encounter a bug, even if you could fix it yourself, please share with your fellow Pythonista :-) at the [Issues page](https://github.com/GochoMugo/firebasin/issues)

**Conquer the World with Python**
