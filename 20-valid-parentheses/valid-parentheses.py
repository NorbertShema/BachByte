class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Understand:
                -Input: string of parantheses (s)
                -Output: bool (true/false)
                -constraints:
                            -s consists of parentheses only '()[]{}'.
                            -time/space complexity
                -edge cases: empty string

        Plan: use stack for a valid parantheses checker

        Implement:

        """
       
        stack = []
        # Use the closing parentheses as keys because they trigger the matching check
        parentheses = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's an opening bracket, push to stack
            if char not in parentheses:
                stack.append(char)
            else:
                    # Edge case: if stack is empty, there's no opening bracket to match
                if not stack:
                    return False
                        # Pop the last opening bracket and check if it matches the current closing one
                popped = stack.pop()
                if popped != parentheses[char]:
                    return False  # Mismatched pair

        # If stack is empty, all brackets matched; otherwise, some were left unclosed
        return not stack


        ##Time O(n)
        ## Space O(n)





        
