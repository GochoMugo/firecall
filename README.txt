Firebasin
========
A Python Implementation of the Firebase API

Prerequisites
=============

"requests" Library

This library depends on the `requests` library. If you have **NOT** installed the **requests** library yet
            sudo pip install requests 

Installation
=========
To Install this library into your machine:
            sudo pip install firebasin

Getting Started
============
1.  Import the "firebasin" library
            import firebasin

2.  Create a Firebase instance
            my_firebase = firebasin.Firebase("https://my_firebase_name.firebaseio.com")

Firebase is now ready to be used. It's time to conquer the World.

Methods
=======
I have tried as much as possible to mimic the Javascript API. Thus the following methods:

1.  .root()
    -------
    Get a Firebase reference to the root of the Firebase
        Example:
            >>>print my_firebase.root()
            my_firebase_name.firebaseio.com
