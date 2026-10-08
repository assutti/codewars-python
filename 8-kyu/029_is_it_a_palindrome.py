# Return True if the given string is a palindrome, ignoring letter case.
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]