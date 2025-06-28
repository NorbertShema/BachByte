'''
Question description

Given a string s, return True if every character in the string is unique.
Return False if any characters in s are repeated.

Example 1
Input: s = "abcdef"
Expected Output: True

Example 2
Input: s = "aabbcc"
Output: False


Example 3
Example Input: s = ""
Expected Output: True

'''


def has_all_unique_charachers(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
    
    seen.add(char)

    return True

s = "abcfef"

print(has_all_unique_charachers(s))