# Leetcode125_validPalindrome.py

import re

def isPalindrome(s):
    """
    :param s: str
    :return: bool
    """
    # Solution 1: use regular expression to remove non alphanumeric characters.
    s = s.lower()
    r = re.sub(r'[^a-zA-Z0-9]','', s)

    return r == r[::-1]

print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome("0P") == False)
print(isPalindrome('') == True)
print(isPalindrome('09dfSSZ098') == False)
print(isPalindrome('a090090a') == True)
