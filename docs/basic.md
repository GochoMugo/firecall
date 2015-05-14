---
layout: default
permalink: /basic/
---


# Getting Started

Import the `firecall` library

  <pre><code class="language-python">import firecall</code></pre>

Create a Firebase instance

  <pre><code class="language-python">my_firebase = firecall.Firebase("https://my-firebase_name.firebaseio.com")</code></pre>

While creating the Firebase instance, you might pass an access token to `auth` argument like shown below. The access token will persist across all transactions with the Firebase, unless you explicitly pass another access token to a method.

<pre><code class="language-python">my_firebase = firecall.Firebase("https://my-firebase_name.firebaseio.com", auth="access_token_here")
# Ensure that you have defined the function you pass to "error=".
</code></pre>

Firebase is now ready to be used. It's time to conquer the World.


# Basic Methods

These are the basic methods available to any Firebase

## .root()

Get a Firebase reference to the root of the Firebase. 

* Requires No arguments.
* Returns a String

Example:

<pre><code class="language-python">print(my_firebase.root())</code></pre>

<hr>


## .name()

Get the last token of this location's URL.

* Requires No arguments
* Returns a String

Example:

<pre><code class="language-python">print(my_firebase.name())</code></pre>

<hr>


## .attr()

Returns a tuple containing some details of the Firebase.

* Requires No arguments
* Returns a tuple e.g (time\_of\_creation, url\_of\_firebase, auth\_token)

<pre><code class="language-python">print(my_firebase.attr())</code></pre>

<hr>


## .parent()

Get a Firebase instance with the parent Location as its URL

* Requires No arguments
* Returns a new Firebase Instance

Example:

<pre><code class="language-python">new_parent = my_firebase.parent()</code></pre>


<hr>


## .child(**kwargs)

Get a Firebase instance with a child location as its URL

* Requires:
    * point="relative\_URL\_to\_child"
* Returns a Firebase Instance

Example:

<pre><code class="language-python">new_child = my_firebase.child(point="/child")</code></pre>

