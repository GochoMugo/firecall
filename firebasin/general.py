# General Methods

# regular expression module
import re

# Valid Firebase Url
def valid_url(name):
    # Not Blank
    # Valid characters: a-z 0-9 -
    if name != '' and re.search(r'[^a-zA-Z0-9\-]', name) == None: return name 
    raise Exception("Invalid URL for a Firebase: " + name)
    return True
    
# Getting Optional Arguments: These arguments are optional and their abscence in the received 
# argv dictionary returns 'False'. Otherwise it returns the value passed
def get_arg(name, argv):
    if name in argv: return argv[name]   # If key is in Dictionary, return the value. 
    return None                                      # Else 'None' is returned
