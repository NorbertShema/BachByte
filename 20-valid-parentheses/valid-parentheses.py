class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        Understand:
            - Input: string of parentheses (s)
            - Output: bool (True/False)
            
        Constraints:
                - s consists of parentheses only: '()[]{}'
                - Time/Space complexity should be optimal
                
        Edge cases:
                - Empty string → return True (nothing invalid)
        
        Match:
            - Stack problem: use LIFO to track opening brackets
        
        Plan:
            - Use a stack to store opening brackets
            - Use a dictionary to map closing brackets to their matching opening ones
            - When encountering a closing bracket:
                - If stack is empty → invalid
                - Pop from stack and check if it matches
            - At the end, stack must be empty for validity
        """

        stack = []
        # Closing bracket → Opening bracket mapping
        parentheses = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's an opening bracket, push onto stack
            if char not in parentheses:
                stack.append(char)
            else:
                # If stack is empty, there's no opening bracket to match
                if not stack:
                    return False
                
                # Pop the last opening bracket and check match
                popped = stack.pop()
                if popped != parentheses[char]:
                    return False  # Mismatch found

        # Valid if no unmatched opening brackets remain
        return not stack

        # Time Complexity: O(n) → each character processed once
        # Space Complexity: O(n) → stack can store all opening brackets
