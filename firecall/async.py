'''
Asynchronous Implementation of the Firebase API. This is built on top of
the Synchronous implementation (sync.py)
'''


from .general import valid_url
from .sync import Firebase_sync
from threading import Thread, Event
from time import sleep


# Async Class: This class implements threading of requests made
# and the particular execution of followup functions
class async:
    'Class for Thread creation for aynchronous calls to a Firebase'

    def __init__(self, type, request, **kwargs):
        callback = kwargs.get("callback", None)
        # Allowing multiple callbacks
        callbacks = kwargs.get("callbacks", [])
        if callback not in callbacks:
            callbacks.append(callback)
        error = kwargs.get("error", None)
        kwargs.pop("callback", None)
        kwargs.pop("callbacks", None)
        kwargs.pop("error", None)
        # Creating a Thread for the Request & Callback & Error
        # and Starting it Immediately
        if type == "once":
            self.__request = Thread(target=self.__thread,
                                    args=(request, kwargs, callbacks, error,))
            self.__request.start()
        if type == "watch":
            self.__watch = None
            self.__event = Event()
            self.__request = Thread(target=self.watch,
                                    args=(request, kwargs, callbacks, error,))
            self.__request.start()

    # Wrapper Function for the Thread
    def __thread(self, request, argv, callbacks, error):
            response = None
            try:
                response = request(**argv)
                if callbacks and response:
                    for callback in callbacks:
                        callback(response)
            except Exception as err:
                if error:
                    error(err)

    # Watch Thread: this will be used to watch for changes
    def watch(self, request, argv, callbacks, error):
        fetches = argv.get("fetches", -1)
        frequency = argv.get("frequency", 10)
        ignore_error = argv.get("ignore_error", True)
        argv.pop("fetches", None)
        argv.pop("frequency", None)
        argv.pop("ignore_error", None)
        self.__watch = True
        newData = None
        oldData = None
        while self.__watch is True and fetches != 0:
            try:
                newData = request(**argv)
                if newData != oldData and callbacks and newData:
                    for callback in callbacks:
                        callback(newData)
                    oldData = newData
            except Exception as err:
                if ignore_error is False:
                    self.__event.set()
                    break
                if error is not None:
                    error(err)
            fetches -= 1
            if fetches == 0:
                self.__event.set()
                break
            sleep(frequency)

    # Stop Watch: This will kill the Watch associated with this Instance
    def stop(self, timeout=0):
        self.stopwatch = Thread(target=self.__stopper, args=(timeout,)).start()

    # The Stopper
    def __stopper(self, timeout):
        self.__event.wait(timeout)
        self.__watch = False


# Async Class for Firebase Methods
class Firebase(Firebase_sync):
    'Firebase class. Contains methods to be used by the programmer'

    # Constructor
    def __init__(self, url, **kwargs):
        try:
            self.__url = valid_url(url)
            Firebase_sync.__init__(self, url, kwargs.get("auth", None))
        except Exception as err:
            error = kwargs.get("error", None)
            if error is not None:
                error(err)

    def get(self, **kwargs):
        async("once", self.get_sync, **kwargs)

    def put(self, **kwargs):
        async("once", self.put_sync, **kwargs)

    def post(self, **kwargs):
        async("once", self.post_sync, **kwargs)

    def update(self, **kwargs):
        async("once", self.update_sync, **kwargs)

    def delete(self, **kwargs):
        async("once", self.delete_sync, **kwargs)

    def export(self, **kwargs):
        async("once", self.export_sync, **kwargs)

    # There's need to return the Instance to allow stopping it
    def onChange(self, **kwargs):
        return async("watch", self.get_sync, **kwargs)

    def parent(self, **kwargs):
        i = self.__url.rfind('/')
        url = self.__url[:i]
        if url == "https:/":
            # Firebase is already parent
            return None
        return Firebase(url,  auth=kwargs.get("auth", None))

    def child(self, **kwargs):
        if not self.amust(("point",), kwargs):
            pass
        return Firebase(self.__url + kwargs["point"],
                        auth=kwargs.get("auth", None))
