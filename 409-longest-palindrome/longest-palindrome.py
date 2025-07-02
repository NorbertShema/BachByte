from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        length = 0
        odd_found = False

        for char_count in count.values():
            if char_count % 2 == 0:
                length += char_count
            else:
                length += char_count - 1
                odd_found = True

        return length + 1 if odd_found else length