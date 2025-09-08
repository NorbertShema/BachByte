class Solution(object):
    def isPalindrome(self, s):
        """
        Understand:
            - Input: string s (a phrase)
            - Output: Boolean (True if palindrome, False otherwise)
            - Only alphanumeric characters matter
            - Case-insensitive
            - Edge case: empty string is considered a palindrome
            - Time/Space constraints: O(n) time, O(1) space

        Match:
            - Two pointers (left and right) approach

        Plan:
            1. Initialize left at 0, right at len(s) - 1
            2. While left < right:
                a. Skip non-alphanumeric characters on both sides
                b. Compare lowercase of left and right characters
                c. If mismatch, return False
                d. Otherwise, move pointers inward
            3. If loop completes, return True

        Implement:
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            if not s[left].isalnum():
                left += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters in lowercase
            if s[left].lower() != s[right].lower():
                return False  # Mismatch found

            # Move pointers inward
            left += 1
            right -= 1

        return True  # All characters matched, it's a palindrome

        # Time Complexity: O(n)
        # Space Complexity: O(1)
