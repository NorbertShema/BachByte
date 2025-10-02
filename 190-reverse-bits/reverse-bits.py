class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int

        Understand:
            - Input: a 32-bit unsigned integer (n)
            - Output: the integer obtained by reversing the binary representation of n
            - Constraints:
                - Input is always a 32-bit integer
                - Must reverse all 32 bits, not just until the first 1
            - Edge cases:
                - n = 0 (output should also be 0)
                - n = all 1s (output remains all 1s)

        Match:
            - Use bit manipulation to extract bits and build the reversed result
            - Shift result left and add the current least significant bit from n
            - Continue until all 32 bits are processed

        Plan:
            - Initialize result = 0
            - Loop 32 times (for each bit in a 32-bit integer):
                - Left-shift result by 1 (make space for the next bit)
                - Add the last bit of n to result (n & 1)
                - Right-shift n by 1 (move to the next bit)
            - Return result

        Implement:
            - Use a for loop that iterates exactly 32 times
            - Update result and n in each iteration
            - Return the final result

        Complexity:
            - Time Complexity: O(32) → O(1)
                Always 32 iterations regardless of input size
            - Space Complexity: O(1)
                Only uses a few integer variables
        """

        result = 0
        for _ in range(32):                        # Process exactly 32 bits
            result = (result << 1) | (n & 1)       # Shift result left and add last bit of n
            n >>= 1                                # Shift n right to move to the next bit
        return result


# Time Complexity: O(1)   (32 fixed operations)
# Space Complexity: O(1)
