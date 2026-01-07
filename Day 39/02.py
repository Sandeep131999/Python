"""Problem Statement:

Given an integer x, determine whether it is a palindrome.
A number is a palindrome if it reads the same forward and backward.

Input:An integer x
Output:Return true if x is a palindrome, otherwise return false.

Examples:
Input: 121 → Output: true
Input: -121 → Output: false
Input: 10 → Output: false

Constraints:
-2³¹ ≤ x ≤ 2³¹ − 1

Note / Follow-up: Solve the problem without converting the number into a string.

Algorithm (Without String Conversion):
If x is negative, return false.
Initialize original = x and reverse = 0.
While x > 0:
Extract the last digit using x % 10.
Update reverse = reverse * 10 + digit.
Remove the last digit from x using integer division.
Compare original with reverse.
If both are equal, return true; otherwise, return false.

Time Complexity: O(n), where n is the number of digits in the number.
Space Complexity: O(1), constant extra space.
"""

def reverse_number (num:int):
    """This method is used to reverse the number without converting them to string using mathematical way """
    if num == 0:
        return 0
    rev = 0
    while num > 0:
        di = num % 10
        rev = rev * 10 + di
        # // is called floor division and it was used to remove the decimal
        num //= 10
    return rev

def check_palindrome_number(number:int):
    re = reverse_number(number)
    if number == re:
        print("Its a palindrome")
    else :
        print("Its not a palindrome ")

print(check_palindrome_number(121))
