'''
General Methods that may be required all over the Library
and are not specific to a specific Firebase
'''

import re


def valid_url(name):
    '''
    Validates a Firebase URL. A valid URL must exhibit:
    - Protocol must be HTTPS
    - Domain Must be firebaseio.com
    - firebasename can only contain:
          - hyphen, small and capital letters
    - firebasename can not have leading and trailing hyphens
    - childnames can not contain:
        - period, dollar sign, square brackets, pound
        - ASCII Control Chars from \x00 - \x1F and \x7F
    '''

    try:
        pattern = r'^https://([a-zA-Z0-9][a-zA-Z0-9\-]+[a-zA-Z0-9]).firebaseio.com(/[^\#\$\[\]\.\x00-\x1F\x7F]*)'
        result = re.search(pattern, name + '/').group()
        result = result[:len(result) - 1]
        if result == name:
            return name
        else:
            raise ValueError("InvalidURL")
    except:
        raise ValueError("InvalidURL")
