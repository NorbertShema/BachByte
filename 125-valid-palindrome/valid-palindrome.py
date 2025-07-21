class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Undertstand: given a phrase(s) check if its alphanum is a palindrome
                -Input: string (s): a phrase
                -Output: Bool(true/false)
                -Constraints: 
                        -s consists only of printable chars
                        -must be converted to alphanum
                        -time/space complexity
                Edge cases:Empty string is a palindrome



        Match: Two pointers

        Plan:

            -Initialize two pointers left and right.
            -While left < right
            -Skip non-alphanumeric characters using .isalnum().
            -Compare lowercase of characters at left and right.
            -If not equal, return False.
            -Move both pointers inward if characters match
            -If loop completes, return True.

        Implement:        
        """
        l, r = 0, len(s) -1

        while l < r:
            if not s[l].isalnum():
                l +=1
                continue

            if not s[r].isalnum():
                r -=1 
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

        ##Time O(n)
        ## Space O(1)








