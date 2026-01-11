# Problem Statement


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

def check_anagram(t:str,s:str)->bool:

    if len(t) != len(s):
        return False

    freq = {}

    for i in t:
        freq[i] = freq.get(i, 0) + 1


    for i in s :
        if i not in freq:
            return False

        freq[i] -= 1
        if freq[i] < 0:
            return False

    return True


print(check_anagram("sand","sand"))

