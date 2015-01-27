---
layout: default
permalink: /sync/
---


# Synchronous Methods

The asynchronous methods are also available in synchronous flavor. To get a method work synchronously, append "_sync" to the name of the method.

Example:

```python
user = my\_firebase.get\_sync("/user")
\# Python will wait for the response before executing the next line of code
\# Callback arguments passed will be ignored
```
