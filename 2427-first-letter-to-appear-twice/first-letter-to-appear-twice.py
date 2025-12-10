class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str

        Understand:
            Input: string (s) lower case english letters
            Output: string: the first letter appears twice
            Constraints: 
                -s has at least one repeatd letter( so guaranteed solution)
                -s consists of lowercase english letters
            Edge:
                empty string. ( not applicable here)

        Plan: we need to return the string that appears twice
            -initialize a list to store the letter
            - loop through the string
                -if string in s:
                    -        

we only use a list and not a hashmap because we only have 26 lowercase letters so this is
a fast look up.
        """
        
        Seen_letters = []

        for string in s:
            if string in Seen_letters:
                return string  

            else:
                Seen_letters.append(string)         

