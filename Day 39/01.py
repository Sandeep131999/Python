"""
===========================================
String Related Problems
===========================================

1. Check if a String is a Palindrome
------------------------------------

Problem Description:
A string is considered a palindrome if, after:
    - Converting all uppercase letters to lowercase
    - Removing all non-alphanumeric characters

it reads the same forward and backward.

Alphanumeric characters include:
    - Letters (a–z, A–Z)
    - Numbers (0–9)

Given a string `s`, return True if it is a palindrome, otherwise return False.

------------------------------------
Examples:
------------------------------------

Example 1:
Input:
    s = "A man, a plan, a canal: Panama"
Output:
    True
Explanation:
    After cleaning the string:
    "amanaplanacanalpanama"
    It reads the same forward and backward.

------------------------------------

Example 2:
Input:
    s = "race a car"
Output:
    False
Explanation:
    After cleaning the string:
    "raceacar"
    It does not read the same forward and backward.

------------------------------------

Example 3:
Input:
    s = " "
Output:
    True
Explanation:
    After removing non-alphanumeric characters, the string becomes:
    ""
    An empty string is considered a palindrome.

"""

import string

def clean_text(s):
    result = ""
    for ch in s:
        if ch.isalnum():
            result += ch.lower()
    return result

def check_palindrome(input_text):
    # '','',it indicates delete string and string.punctuation it removes this !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # cleaned = input_text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    cleaned = clean_text(input_text)

    rev = ""
    left, right = 0, len(cleaned) - 1

    while left < right:
        rev += (cleaned[right])
        if cleaned[left] != cleaned[right]:
            print("Not a Palindrome")
            return
        left += 1
        right -= 1

    print(f"{rev}  Palindrome")
check_palindrome("A man, a plan, a canal: Panama")

# Time Complexity
    # every built in function  O(n) + O(n) + O(n) + O(n) + O(n) = O(n)
    #O(n)
    # Linear time — execution time increases proportionally with the input size.





