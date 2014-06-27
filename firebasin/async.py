# Asynchronous Implementation of the Firebase API

# 'threading' module
from threading import Thread
# 'sync' module - holds the 'firebase' class and its methods
from sync import Firebase_sync
# 'sleep' function
from time import sleep
from general import valid_url

# Async Class: This class implements threading of requests made and the particular execution of followup functions
class async:
    'Class for Aynchronous calls to the Firebase API'
   
   # Constructor for a Request-Callback Thread
    def __init__(self, type, request, **kwargs):
        self._watch = {}
        callback = kwargs.get("callback", None)   # Getting the 'callback' variable. Defaults to 'None'
        error = kwargs.get("error", None)             # Getting the 'error' variable. Defaults to 'None'
        kwargs.pop("callback", None)                  # Removing the Callback argument
        kwargs.pop("error", None)                       # Removing the Callback argument
        # Creating a Thread for the Request & Callback & Error and Starting it Immediately
        if type == "once": self.request = Thread(target=self.thread, args=(request, kwargs, callback, error)).start()
        # Creating a Thread for the Watch & Callback & Error and starting it Immediately
        if type == "watch": self.request = Thread(target=self.watch, args=(request, kwargs, callback, error)).start()
        
    # Wrapper Function for the Thread
    def thread(self, request, argv, callback, error):
            response = None                               # Will hold the response
            try:                                                   # trying to execute the query
                response = request(**argv)            # Executing Request
                if callback != None and response != None: callback(response)  # Executing Callback If Data is received
            except Exception, err:                     # Query failed or Error Occurred
                if error != None: error(err)               # Executing Error If Request failed

    # Watch Thread: this will be used to watch for changes
    def watch(self, request, argv, callback, error):
        frequency = argv.get("frequency", 10)   # After how long the thread will check for changes
        argv.pop("frequency", None)                # Removing the frequency parameter
        ignore_error = argv.get("ignore_error", True) # Whether to keep going in case of Error. Default = True
        argv.pop("ignore_error", None)            # Removing the ignore_error parameter
        self._watch = True                               # Marker to keep the watch going. Enables stopping
        newData = None                                 # Will hold new data as it arrives
        oldData = None                                   # Will hold the previous data as new data arrives
        while self._watch == True:                 # Loop to continouosly check remote
            try:
                newData = request(**argv)              # Making the Request
                if newData != oldData and callback != None and newData != None:  # Testing for New Data
                    callback(newData)                       # Executing callback; passing the new data to it
                    oldData = newData                      # Now updating the previous data to match the new data
            except Exception, err:
                if ignore_error != True: self._watch = False # Knowing if we are to stop or keep going
                if error != None: error(err)              # Executing Error function If Request failed
            sleep(frequency)                                # Sleep (wait) for time specified. Default = 10 seconds
            
    # Stop Watch: This will kill the Watch associated with this Instance
    def stop(self, timeout=0):
        sleep(timeout)             # Sleep (wait) for the time specified before killing the Watch. Default = 0 seconds
        self._watch = False     # This will cause the Loop in the watch to stop
          
# Sync Class for Firebase Methods
class Firebase(Firebase_sync):

    # Constructor
    def __init__(self, url, **kwargs):
        try:
            url = valid_url(url)
            Firebase_sync.__init__(self, url, kwargs.get("auth", None))  # Instantiating the firebase-sync class
        except Exception, err:
            error = kwargs.get("error", None)
            if error != None: error(err)
   
    # Creating Parents
    def parent(self, **kwargs):
        # Getting the last '/'
        i  = self.url.rfind('/')
        # Slicing the url
        url = self.url[:i]
        # Ensuring it is not the 'https:/' portion
        if url == "https:/": return None    # Firebase is already parent
        return Firebase(url,  kwargs.get("auth", None))             # A parent Firebase Instance    
    
    # Creating Children
    def child(self, **kwargs):
        # Ensuring Point is Provided
        if not self.amust(("point",), kwargs): return
        # Using the Parent URL
        return Firebase(self.url + '/' + kwargs["point"], kwargs.get("auth", None))    # A Child firebase instance
        
    # GET
    def get(self, **kwargs):
        async("once", self.get_sync, **kwargs)
    # PUT
    def put(self, **kwargs):
        async("once", self.put_sync, **kwargs)
    # POST
    def post(self, **kwargs):
        async("once", self.post_sync, **kwargs)
    # UPDATE
    def update(self, **kwargs):
        async("once", self.update_sync, **kwargs)
    # DELETE
    def delete(self, **kwargs):
        async("once", self.delete_sync, **kwargs)
    # EXPORT
    def export(self, **kwargs):
        async("once", self.export_sync, **kwargs)
    # ON
    def onChange(self, **kwargs):
        return async("watch", self.get_sync, **kwargs) # There's need to return the Instance to allow stopping it
    
