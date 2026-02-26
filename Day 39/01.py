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
def clean_text(s):
    """ Used isalnum builtin function to remove the special characters  """
    result = ""
    for ch in s:
        if ch.isalnum():
            result += ch.lower()
    return result

def check_palindrome(input_text):
    """ Time Complexity   every builtin function  O(n) + O(n) + O(n) + O(n) + O(n) = O(n)
        O(n) Linear time — execution time increases proportionally with the input size.  """
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

def max_profit(prices) -> int:
    min_price = float('inf')
    # inf - means infinity
    max_profits = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profits = max(max_profits, price - min_price)
    return max_profits

# print(max_profit([7,1,5,8,9,6]))


def is_palindrome(s: str) -> bool:
    clean_inp = []
    reverse_inp = ""
    for char in s:
        if char.isalnum():
            clean_inp.append(char.lower())
    reverse_inp = clean_inp[::-1]
    if clean_inp == reverse_inp:
        return True
    else:
        return False


print(is_palindrome("0P"))






