# Problem Statement:
from xmlrpc.client import boolean


# Given two strings s and t, return true if t is an anagram of s, and return false otherwise.
# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all
# the original letters exactly once.

# Example 1:
# Input:
# s = "anagram"
# t = "nagaram"
# Output:
# true


# Example 2:
# Input:
# s = "rat"
# t = "car"
# Output:
# false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters

def check_anagram(s:str,t:str)->bool:
    enum_i = []
    for i in s :
        enum_i.append(i)


    return True

