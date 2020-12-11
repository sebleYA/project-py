# palindrome.py
#
# Demonstrates the use of the string character manipulation and
# the 'isalpha' and 'lower' methods.

# CSC 110
# Sp'12


# Tests to see if a word or phrase is a palindrome, ignoring case
# and all non-letters.  For example, is_palindrome("Madam I'm Adam") -> True
def is_palindrome(text):
    text = strip_and_adjust(text) # work with letters only, all in lower-case
    return text == reverse(text)  # the basic definition of a palindrome

# Returns a new string with the characters of 's' in reverse order
def reverse(s):
    result = ''  # initialize accumulator to the empty string
    for ch in s:
        result = ch + result  # PREpend the character!
    return result

# Returns a new string with all non-letters removed and all letters
# converted to lower case.
def strip_and_adjust(s):
    s = s.lower() # change all upper-case letters to lower-case
    result = ''  # initialize accumulator to the empty string
    for ch in s:
        if ch.isalpha():
            result += ch
    return result


# ALTERNATIVE approach: Uses a loop and two pointers (variables that
# hold index values) to move through the string from both ends at the
# same time.  Stops when they cross.  This is more efficient.
# This is an example of a CSC 142-level function :-)
def is_palindrome_alt_method(text):
    text = text.lower() # change all upper-case letters to lower-case
    left = 0  # left pointer starts at lowest legal index
    right = len(text) - 1  # right pointer starts at highest legal index
    good = True  # assume the string is a palindrome until proven otherwise
    while left < right and good:
        # adjust left pointer to bypass any non-letters
        while left < len(text) and not text[left].isalpha():
            left += 1
        # adjust right pointer to bypass any non-letters
        while right >= 0 and not text[right].isalpha():
            right -= 1
        if left < right and text[left] != text[right]:
            good = False
        left += 1
        right -= 1
    return good
        

def main():
    # Test is_palindrome
    s1 = 'Madam I\'m Adam'
    print(s1, '--', is_palindrome(s1))
    s1 = 'This is a test'
    print(s1, '--', is_palindrome(s1))
    s1 = 'Ada'
    print(s1, '--', is_palindrome(s1))
    s1 = 'go'
    print(s1, '--', is_palindrome(s1))
    s1 = 'gogo'
    print(s1, '--', is_palindrome(s1))
    s1 = 'A'
    print(s1, '--', is_palindrome(s1))
    s1 = 'Aa'
    print(s1, '--', is_palindrome(s1))
    s1 = ''
    print(s1, '--', is_palindrome(s1))
    s1 = 'Do geese see God?'
    print(s1, '--', is_palindrome(s1))
    s1 = 'Was it Eliot\'s toilet I saw?'
    print(s1, '--', is_palindrome(s1))
    s1 = 'A Toyota! Race fast... safe car: a Toyota'
    print(s1, '--', is_palindrome(s1))
    s1 = 'Are we not drawn onward, we few, drawn onward to new era?'
    print(s1, '--', is_palindrome(s1))
    print('\n')
    
    # Test is_palindrome_alt_method
    s1 = 'Madam I\'m Adam'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'This is a test'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'Ada'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'go'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'gogo'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'A'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'Aa'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = ''
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'Do geese see God?'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'Was it Eliot\'s toilet I saw?'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'A Toyota! Race fast... safe car: a Toyota'
    print(s1, '--', is_palindrome_alt_method(s1))
    s1 = 'Are we not drawn onward, we few, drawn onward to new era?'
    print(s1, '--', is_palindrome_alt_method(s1))
 

main()
