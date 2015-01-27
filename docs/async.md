---
layout: default
permalink: /async/
---


# Asynchronous Methods

A Firebase instance has different methods that let you transact with it. The methods shown below are **Asynchronous**. This means that:

* Python won't wait for the response, it will continue executing following lines of code
* You should NOT assign return value to a variable. Doing this will always assign `None`
* You will have to use a callback to manipulate returned data from a request

**Note:** There are also **Synchronous** methods you can use. Read along to see how to use them.


## .get(**kwargs)

Get data a particular location on your Firebase

* Requires:
    * point="location\_to\_read"
    * auth="access\_token" (Optional)
    * callback=name\_of\_a\_function (Optional)
    * callbacks=\[list\_of\_callbacks\] (Optional)
    * error=name\_of\_a\_function (Optional)
* Returns `None`. Data fetched is passed to the callback function, if specified.

Example:

<pre><code class="language-python"># Callback function definition
def hello(data):
    print(data)

# Another Callback
def world(data):
    with open('/home/user/.firebase-data', 'w') as data_file:
        data_file.write(data)

# Making a 'GET' request
my_firebase.get(point="/child", auth="Ja2f29f4Gsk2d3bhxW2d8vDlK", callback=hello)

# A Request with multiple callbacks
my_firebase,get(point="/child", auth="Ja2f29f4Gsk2d3bhxW2d8vDlK", callbacks=[hello, world])
</code></pre>
<div class="spacefix"></div>
<hr>


## .put(**kwargs)

Write data into your Firebase

* Requires:
    * point="location\_to\_read"
    * data="data\_to\_put"
    * auth="access\_token" (Optional)
    * callback=name\_of\_a\_function (Optional)
    * callbacks=\[list\_of\_callbacks\] (Optional)
    * error=name\_of\_a\_function (Optional)
* Returns `None`. Data you just put is passed to the callback function, if specified.

<hr>


## .delete(**kwargs)

Delete data from your Firebase

* Requires:
    * point="location\_to\_delete"
    * auth="access_token" (Optional)
    * callback=name\_of\_a\_function (Optional)
    * callbacks=\[list\_of\_callbacks\] (Optional)
    * error=name\_of\_a\_function (Optional)
* Returns `None`. A string saying `null` is passed to the callback function, if specified.

<hr>


## .export(**kwargs)

Export data from a location on your Firebase

* Requires:
    * point="location\_to\_read"
    * auth="access\_token" (Optional)
    * path="UNIX\_path\_to\_file\_to\_write\_to" (Optional)
    * callback=name\_of\_a\_function (Optional)
    * callbacks=\[list\_of\_callbacks\] (Optional)
    * error=name\_of\_a\_function (Optional)
* Returns `None`. Data you just exported is passed to the callback function, if specified.

**Note:** if the `path` argument is not given, this will behave similar to `get()` method of the Firebase instance.

<hr>


## .onChange(**kwargs)

Poll for changes at a Location on your Firebase.

* Requires:
    * point="location\_to\_read"
    * auth="access\_token" (Optional)
    * callback=name\_of\_a\_function (Optional)
    * callbacks=\[list\_of\_callbacks\] (Optional)
    * error=name\_of\_a\_function (Optional)
    * ignore\_error=True (Optional) - Whether to keep watching incase of an error or make it Stop
    * frequency=10 (Optional) - The number of seconds between checks on the Firebase
    * fetches=-1 (Optional) - The number of times to look at the Firebase before automatically stopping. It is a _positive_ integer. Giving a negative integer makes it be ignored. 
* Returns an Object representing the Watch. This object has one method:
    *   _.stop(number\_of\_seconds)_ - Passing an integer will cause the watch to be stopped after the specified number of seconds. If no number is passed, the watch will be stopped as soon as Possible.

<pre><code class="language-python">def keep_printing(data):
    print(data)

# Creates a watch Object
watch = my_firebase.onChange(point="/watch_here", callback=keep_printing) 
watch.stop(20) # The Watch will be stopped after 20 seconds
</code></pre>

**Note:** 

* there's **No** synchronous flavor of this method. For obvious reasons.
* the stopping of a watch may take longer or shorter time for the action to kick in. This depends on your System.


# Callbacks and Errors

In all the **asynchronous** methods, a **Callback** can be assigned. The callback will be executed once response is received. In the case of `.onChange()` method, the callback will be called every time data changes at the point specified.

Since version 0.1.2, multiple callbacks may be assigned using the **callbacks** parameter. The methods/functions, placed in a list and passed to the Firebase methods, will be executed sequentially as ordered in the particular list.

Functions assigned to **error** are executed when an error occurs while executing the action. The following errors may be caught:

1. `EnvironmentError`: This is caused by Trying to access a non-existant Firebase or Security Rules violation while trying to execute a query
2. `KeyError`: This is caused when you do **not** pass a required argument to any function
3. `ConnectionError`: This will occur mostly due to Network problems

If you wanted to catch errors according to this classes, you could do:

<pre><code class="language-python">def caught_an_error(err):
    if err.__class__.__name__ == "KeyError":
        print("KeyError: " + str(err))
    elif err.__class__.__name__ == "EnvironmentError":
        print("EnvironmentError: " + str(err))
    elif err.__class__.__name__ == "ConnectionError":
        print("ConnectionError: " + str(err))
    else:
        print(err.__class__.__name__ + str(err))
</code></pre>

**Note:** All callbacks and error handling functions should be defined before assigning them to a method.
