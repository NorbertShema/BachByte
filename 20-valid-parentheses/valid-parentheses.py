class Solution(object):
    def isValid(self, s):
        """
        : type s: str
        :rtype: bool

        Understand:
                -Input: string of parentheses (s)
                -Output: bool (true/false)
                -constraints:
                            -s consists of parentheses only '()[]{}'.
                            -time/space complexity
                -edge cases: empty string
                
         Match: Stacks       

        Plan: use a stack for a valid parentheses checker

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
                    # Edge case: if the stack is empty, there's no opening bracket to match
                if not stack:
                    return False
                        # Pop the last opening bracket and check if it matches the current closing one
                popped = stack.pop()
                if popped != parentheses[char]:
                    return False  # Mismatched pair

        # If the stack is empty, all brackets are matched; otherwise, some were left unclosed
        return not stack


        ##Time O(n)
        ## Space O(n)





        
