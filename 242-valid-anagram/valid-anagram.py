from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Understand:
                -Input: string (s)
                -Output: bool (true/false)
                -Constraints: -s and t consist of lowercase English letters.
                              -time and space complexity 
                -Edge cases: empty string

        Plan:
            - we need to check it s and t are of same length
            -we need to check if char in s is also in t
            - We can import counter collections to make a dictionary for us and 
            check if the key value pairs are the same and found in both dict
            -if both dict are the same , then its true. 

        Implement:

        """
        if len(s) != len(t):
            return False

        s_dict = Counter (s)  
        t_dict = Counter (t)  

        return s_dict == t_dict

        ##Time O(n)
        ##Space O(1)
