class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ## initialize the pointers
        l = 0
        r = len(s)-1

        while l<r:
            if not s[l].isalnum(): ## we make sure its alpha num
                l = l + 1
                continue

            if not s[r].isalnum():
                r = r - 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l = l + 1
            r = r - 1

        return True         


        