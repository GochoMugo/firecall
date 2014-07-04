'''
General Methods that may be required all over the Library and are not specific 
to a Firebase
'''

# regular expression module
import re

# Valid Firebase Url
# - Protocol must be HTTPS
# - Domain Must be firebaseio.com
# - firebasename can only contain:
#       - hyphen , small and capitall letters and hyphen
# - firebasename can not have leading and trailing hyphens
# - childnames can not contain:
#       - period, dollar sign, square brackets, pound, ASCII Control Chars from \x00 - \x1F and \x7F
def valid_url(name):
    try:
        result = re.search(r'^https://([a-zA-Z0-9][a-zA-Z0-9\-]+[a-zA-Z0-9]).firebaseio.com(/[^\#\$\[\]\.\x00-\x1F\x7F]*)', name + '/').group()
        result = result[:len(result) -1]
        if result == name:
            return name
        else:
            raise ValueError("InvalidURL")
    except:
        raise ValueError("InvalidURL")
        
