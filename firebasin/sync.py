'''
Synchronous implementation of the Firebase API. This provides the basic 
building blocks.
'''

# 'request' module
import requests
# 'json' module
import json
# 'time' functions
from time import time

# 'Firebase_sync' class
class Firebase_sync:
    'Parent Class for Firebase Objects. Its methods are synchronous.'
    
    # Constructor
    def __init__(self, url, auth=None):
        # Ensuring that the URL is Valid
        self.__url = url                     # firebase url
        self.__auth = auth                # firebase credentials
        self.__attr = {
            "time": time(),
            "url": self.__url,
            "token": self.__auth
        }
        
    # Returns a Dictionary with the attributes of the Firebase
    def attr(self):
        return self.__attr['time'], self.__attr['url'],  self.__attr['token']
    
    # Getting Root URL of the Firebase. E.g. if the URL of a firebase is
    # "https://my_firebase.firebaseio.com/users" then its root is "https://my_firebase.firebaseio.com"
    def root(self):
        # Looping till we find '.com'
        i = self.__url.find('.com') + 4   # index after '.com'
        return self.__url[:i]               # Root URL of Firebase
    
    # Getting name of Firebase. E.g. if a firebase instance points to 
    # "https://my_firebase.firebaseio.com/users" its name would be "users"
    def name(self):
        i = self.__url.rfind('/')     # Getting index of the last '/'
        # Exception that the Firebase points to the root. E.g. "https://my_firebase.firebaseio.com/" 
        # We can figure this out but by looking for ":" 2 indices before the "/"
        if self.__url[i-2] == ':':
            return "/"              # "/" as root :-)
        return self.__url[i+1:]    # return the name
    
    # Converting the URL of the firebase to a string and returning it
    def toString(self):
        return str(self.__url)    # Converting to String
    
    # Url correction: This involves Concatenation with required fields in the URL as per the
    # REST API. E.g. "https://my_firebase.firebaseio.com/users" + "/john_doe" + "?format=export"
    def url_correct(self, point, auth=None, export=None):
        newUrl = self.__url + point + '.json' # Basic url
        if auth != None:                           # Checking if auth is required
            newUrl += ("?auth=" + auth)     # Appending Credential
        if export != None:                        # Checking if it is an Export
            newUrl += "?format=export"    # Appending Query
        return newUrl                            # Returning the corrected url to be sent as Request
       
    # File Reading: This aids in reading a ".json" file from which one (or more) json objects
    # could be passed as Data to Requests
    @staticmethod
    def __read(path):
        mine = open(path, 'r')                  # Opening file in Read mode
        data = mine.read()                       # Reading Data in file to a variable
        objs = []                                      # Array to hold Json Objects
        i = 0                                            # Index of Character where cursor is while Reading
        match = [0, None]                       # tracing the '{'s and matching '}'s
        while i < len(data):                     # Looping thru string
            if match[1] is None and data[i] == '{':     # Getting '{'
                match[1] = i                                         # Saving The Starting Index of the Object
            elif data[i] == '}' and match[0] == 0:      # Getting the matching '}'
                objs.append(data[match[1]:i + 1])         # Pushing the Object as String to Array
                match = [0, None]                               # Resetting Array
            # Handling Inner Objects in the a Object
            elif data[i] == '{':
                match[0] += 1
            elif data[i] == '}':
                match[0] -= 1
            i += 1                                      # Incrementing the Index
        return objs                               # Returning the Array
        
        
    # File Writing: This function is used to write to Files JSON objects
    @staticmethod
    def __write(path, data, mode="w"):
        if data[0] == '"' or data[0] == "'":         # Removing Preceding '"'
            data = data[1:]                                 # From 2nd Index to Last
        last = len(data) -1                                # Last Index
        if data[last] == '"' or data[last] == "'": # Removing Trailing '"'
            data = data[:last]                             # From Beginning to Second Last Index
        data =  str(data).replace("\\", "")          # Backslash Removal
        out = open(path, mode)                       # Opening/Creating file. Default: 'overwrite' mode
        out.write(str(data))                              # Writing Data
        out.close()                                           # Closing file
        return data                                         # Returning the Data just for convenience
    
    # Requiring Arguments: Some functions may not work without some arguments being present
    # the name(s) of the arguments are passed in a tuple along with the arguments recieved in the call
    def amust(self, args, argv):
        for arg in args:                                                            # Looping through the Tuple with the argument names
            if str(arg) not in argv:                                             # The name is not used as a keyword in the argv dict
                raise KeyError("ArgMissing: " + str(arg) + " not passed") # Raising Exception and stopping Execution
            
     # Catching error responses
    @staticmethod
    def catch_error(response):
        status = response.status_code               # Status Code
        if  status == 401 or status == 403:         # Security Rules Violation
            raise EnvironmentError("Forbidden")
        elif status == 417 or status == 404:       # Firebase NOT Found
            raise EnvironmentError("NotFound")
     
     # GET: getting data from the Firebase.
    def get_sync(self, **kwargs):
        self.amust(("point",), kwargs) # Ensuring Point is Provided
        # Sending the 'GET' request
        response = requests.get(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth)))
        self.catch_error(response)
        return response.content
        
    # PUT: putting 'data' at a location in the Firebase
    def put_sync(self, **kwargs):
        self.amust(("point","data"), kwargs) # Ensuring Point and Data is Provided
        # Sending the 'PUT' request
        response = requests.put(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth)), data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content
    
    # POST: posting data to the Firebase. 
    # Note: Firebase will give it a randomized "key" and the data will be the "value". Thus a key-value pair
    def post_sync(self, **kwargs):
        self.amust(("point", "data"), kwargs) # Ensuring Point and Data is Provided
        # Sending the 'POST' request
        response = requests.post(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth)), data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content

    # UPDATE
    def update_sync(self, **kwargs):
        self.amust(("point", "data"), kwargs) # Ensuring Point and Data is Provided
        # Sending the 'PATCH' request
        response = requests.patch(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth)), data=json.dumps(kwargs["data"]))
        self.catch_error(response)
        return response.content

    # DELETE: removes data at the location requested
    def delete_sync(self, **kwargs):
        self.amust(("point",), kwargs) # Ensuring Point is Provided
        # Sending the 'DELETE' request
        response = requests.delete(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth)))
        self.catch_error(response)
        return response.content
        
    # EXPORT: Data at the provided location will be written into a file at the location and with the filename
    # provided in the 'path' parameter. If the path is NOT given, the data retrieved is simply returned. NO file write.
    def export_sync(self, **kwargs):
        self.amust(("point",), kwargs) # Ensuring Point is Provided
        response = requests.get(self.url_correct(kwargs["point"], kwargs.get("auth", self.__auth), True));
        self.catch_error(response)
        # If path is provided
        path = kwargs.get("path", None) 
        if path != None:
            self.__write(path, response.content, kwargs.get("mode", "w"))
        # Returning response 
        return response.content

