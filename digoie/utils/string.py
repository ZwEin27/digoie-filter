import re

def hasNumbers(inputString):
    # return any(char.isdigit() for char in inputString)
    return bool(re.search(r'\d', inputString))


def hasUnicode(s):
    # if isinstance(s, unicode):
    #     return True
    if '\u' in s:
        return True

    return False


def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"


print hasUnicode(u'\u2113')