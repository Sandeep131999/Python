# 🔹 Problem Statement
#
# Given a string s, return True if any permutation of the string can form a palindrome.
# Otherwise, return False.
# Example 1
# Input:  "code"
# Output: False
# Explanation: No permutation of "code" is a palindrome.
#
# Example 2
# Input: "aab"
# Output: True
# Explanation: "aba" is a palindrome.
#
# Example 3
# Input: "carerac"
# Output: True
# Explanation: "racecar" is a palindrome.
#
# Constraints
# 1 ≤ s.length ≤ 10⁵
# s consists of lowercase English letters

def check_permutations(input_text:str)-> bool :

    freq = {}

    #Store in to hashmap
    for i in input_text.lower():
        freq[i] = freq.get(i, 0) + 1

    print(freq.items())

    for key, value in freq.items():
        if value > 1:
            return True
    return  False


print(check_permutations("code"))