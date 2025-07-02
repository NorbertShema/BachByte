'''
2. Needle in Haystack Correct
Question description

Given two strings needle and haystack , return the index of the first occurrence of needle in haystack,
 or -1 if needle is not part of haystack .

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs twice, starting at indices 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Example 3:
Input: haystack = "mad" needle = "madden"
Needle is longer than haystack, so we return -1.

'''

# Complete the 'find_needle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. STRING haystack
# 2. STRING needle
#

def find_needle(haystack, needle):

# Edge case: empty needle always matches at index 0
    if needle == "":
       return 0
# Loop through haystack to check for match
    for i in range(len(haystack) - len(needle) + 1):
       if haystack[i:i+len(needle)] == needle:
         return i
    return -1

haystack = "sadbutsad"
needle = "sad"
print(find_needle(haystack, needle))