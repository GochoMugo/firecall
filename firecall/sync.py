'''
Synchronous implementation of the Firebase API. This provides the basic
building blocks.
Please Note: Network requests using this methods is Blocking.
'''

import json
import requests
from time import time


# 'Firebase_sync' class
class Firebase_sync:
    'Parent Class for Firebase Objects. Its methods are synchronous.'

    # Constructor
    def __init__(self, url, auth=None):
        '''
        url - (String) a valid Firebase URL
        auth - (String) a Firebase authentication token
        '''
        self.__url = url
        self.__auth = auth
        self.__attr = {
            "time": time(),
            "url": self.__url,
            "token": self.__auth
        }

    def attr(self):
        'Returns a Tuple with the Attributes of the Firebase'
        return self.__attr['time'], self.__attr['url'],  self.__attr['token']

    def root(self):
        '''
        Returns the Root URL of the Firebase. E.g. a Firebase at
        'https://my_firebase.firebaseio.com/users' has its root at
        'https://my_firebase.firebaseio.com'
        '''
        i = self.__url.find('.com') + 4
        return self.__url[:i]

    # Exception that the Firebase points to the root.
    # E.g. "https://my_firebase.firebaseio.com/"
    def name(self):
        '''
        Returns the name of the Firebase. If a Firebase instance points to
        'https://my_firebase.firebaseio.com/users' its name would be 'users'
        '''
        i = self.__url.rfind('/')
        if self.__url[:i] == 'https:/':
            return "/"
        return self.__url[i+1:]

    def toString(self):
        'Returns a String representing the Firebase URL'
        return str(self.__url)

    def url_correct(self, point, auth=None, export=None):
        '''
        Returns a Corrected URL to be used for a Request
        as per the REST API.
        '''
        newUrl = self.__url + point + '.json'
        if auth or export:
            newUrl += "?"
        if auth:
            newUrl += ("auth=" + auth)
        if export:
            if not newUrl.endswith('?'):
                newUrl += "&"
            newUrl += "format=export"
        return newUrl

    @staticmethod
    def __read(path):
        '''
        Reads a File with contents in correct JSON format.
        Returns the data as Python objects.
        path - (string) path to the file
        '''
        try:
            with open(path, 'r') as data_file:
                data = data_file.read()
                data = json.loads(data)
                return data
        except IOError as err:
            pass
        except Exception as err:
            # Invalid JSON formatted files
            pass

    @staticmethod
    def __write(path, data, mode="w"):
        '''
        Writes to a File. Returns the data written.
        path - (string) path to the file to write to.
        data - (json) data from a request.
        mode - (string) mode to open the file in. Default to 'w'. Overwrites.
        '''
        with open(path, mode) as data_file:
            data = json.dumps(data, indent=4)
            data_file.write(data)
            return data

    def amust(self, args, argv):
        '''
        Requires the User to provide a certain parameter
        for the method to function properly.
        Else, an Exception is raised.
        args - (tuple) arguments you are looking for.
        argv - (dict) arguments you have received and want to inspect.
        '''
        for arg in args:
            if str(arg) not in argv:
                raise KeyError("ArgMissing: " + str(arg) + " not passed")

    @staticmethod
    def catch_error(response):
        '''
        Checks for Errors in a Response.
        401 or 403 - Security Rules Violation.
        404 or 417 - Firebase NOT Found.
        response - (Request.Response) - response from a request.
        '''
        status = response.status_code
        if status == 401 or status == 403:
            raise EnvironmentError("Forbidden")
        elif status == 417 or status == 404:
            raise EnvironmentError("NotFound")

    def get_sync(self, **kwargs):
        '''
        GET:  gets data from the Firebase.
        Requires the 'point' parameter as a keyworded argument.
        '''
        self.amust(("point",), kwargs)
        response = requests.get(self.url_correct(kwargs["point"],
                                kwargs.get("auth", self.__auth)))
        self.catch_error(response)
        return response.content

    # PUT: putting 'data' at a location in the Firebase
    def put_sync(self, **kwargs):
        '''
        PUT:  puts data into the Firebase.
        Requires the 'point' parameter as a keyworded argument.
        '''
        self.amust(("point", "data"), kwargs)
        response = requests.put(self.url_correct(kwargs["point"],
                                kwargs.get("auth", self.__auth)),
                                data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content

    def post_sync(self, **kwargs):
        '''
        POST:  post data to a Firebase.
        Requires the 'point' parameter as a keyworded argument.
        Note: Firebase will give it a randomized "key"
        and the data will be the "value". Thus a key-value pair
        '''
        self.amust(("point", "data"), kwargs)
        response = requests.post(self.url_correct(
            kwargs["point"],
            kwargs.get("auth", self.__auth)),
            data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content

    # UPDATE
    def update_sync(self, **kwargs):
        '''
        UPDATE: updates data in the Firebase.
        Requires the 'point' parameter as a keyworded argument.
        '''
        self.amust(("point", "data"), kwargs)
        # Sending the 'PATCH' request
        response = requests.patch(self.url_correct(
            kwargs["point"],
            kwargs.get("auth", self.__auth)),
            data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content

    def delete_sync(self, **kwargs):
        '''
        DELETE: delete data in the Firebase.
        Requires the 'point' parameter as a keyworded argument.
        '''
        self.amust(("point",), kwargs)
        response = requests.delete(self.url_correct(
            kwargs["point"],
            kwargs.get("auth", self.__auth)))
        self.catch_error(response)
        return response.content

    def export_sync(self, **kwargs):
        '''
        EXPORT: exports data from the Firebase into a File, if given.
        Requires the 'point' parameter as a keyworded argument.
        '''
        self.amust(("point",), kwargs)
        response = requests.get(self.url_correct(kwargs["point"],
                                kwargs.get("auth", self.__auth), True))
        self.catch_error(response)
        path = kwargs.get("path", None)
        if path:
            self.__write(path, response.content, kwargs.get("mode", "w"))
        return response.content
