# Asynchronous Implementation of the Firebase API

# 'threading' module
from threading import Thread
# 'sync' module - holds the 'firebase' class and its methods
from sync import Firebase_sync
# 'get_arg' function
from general import get_arg

# Async Class: This class implements threading of requests made and the particular execution of followup functions
class async:
    'Class for Aynchronous calls to the Firebase API'
   
   # Constructor for a Request-Callback Thread
    def __init__(self, request, **kwargs):
        callback = get_arg("callback", kwargs)   # Getting the 'callback' variable. Defaults to 'None'
        error = get_arg("error", kwargs)             # Getting the 'error' variable. Defaults to 'None'
        kwargs.pop("callback", None)                # Removing the Callback argument
        kwargs.pop("error", None)                     # Removing the Callback argument
        # Creating a Thread for the Request & Callback & Error and Starting it Immediately
        self.request = Thread(target=self.thread, args=(request, kwargs, callback, error)).start()
        
    # Wrapper Function for the Thread
    def thread(self, request, argv, callback, error):
          result = request(**argv)                                                       # Executing Request
          if callback != None and result != None: callback(result)      # Executing Callback If Data is received
          if error != None and result == None: error()                        # Executing Error If Request failed
          
# Sync Class for Firebase Methods
class Firebase(Firebase_sync):

    # Constructor
    def __init__(self, url, auth=None):
        Firebase_sync.__init__(self, url, auth)  # Instantiating the firebase-sync class
   
    # Creating Parents
    def parent(self, **kwargs):
        # Getting the last '/'
        i  = self.url.rfind('/')
        # Slicing the url
        url = self.url[:i]
        # Ensuring it is not the 'https:/' portion
        if url == "https:/": return None    # Firebase is already parent
        return Firebase(url,  self.get_arg("auth", kwargs))             # A parent Firebase Instance    
    
    # Creating Children
    def child(self, **kwargs):
        # Ensuring Point is Provided
        if not self.amust(("point",), kwargs): return
        # Using the Parent URL
        return Firebase(self.url + '/' + kwargs["point"], self.get_arg("auth", kwargs))    # A Child firebase instances)
        
    # GET
    def get(self, **kwargs):
        async(self.get_sync, **kwargs)
    # PUT
    def put(self, **kwargs):
        async(self.put_sync, **kwargs)
    # POST
    def post(self, **kwargs):
        async(self.post_sync, **kwargs)
    # UPDATE
    def update(self, **kwargs):
        async(self.update_sync, **kwargs)
    # DELETE
    def delete(self, **kwargs):
        async(self.delete_sync, **kwargs)
    # EXPORT
    def export(self, **kwargs):
        async(self.export_sync, **kwargs)
        
