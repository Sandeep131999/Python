# 🔹 LeetCode #344 — Reverse String
#
# You are given a list of characters s.
# Your task is to reverse the list in-place.
#
# You must do this by modifying the input list directly, not by returning a new list.
#
# Function Signature
# def reverseString(s: list[str]) -> None:
#
# Example 1
# Input:  s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2
# Input:  s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints
#
# 1 ≤ s.length ≤ 10⁵
#
# s[i] is a printable ASCII character
from typing import List


def reverseString(S :list[str]) -> list[str]:

    rev_list = []
    for i in range(len(S)-1,-1,-1):
        rev_list.append(S[i])

    return  rev_list

print(reverseString(S=["h","e","l","l","o"]))