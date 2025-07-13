class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Understand:
                -Input: list of nums (int)
                -Output: num (int)
                -Constraints: all nums are unique and range [0,n]
                -Edge case: empty array

        Plan:
            - use the formula sum of {nth = n * (n + 1) // 2}

        Implementation:

        """

        n = len(nums)

        expected_sum = n * (n + 1) // 2  ## This is a standard formula in math.
                                        #to calculate the sum of the first n natural numbers 0 included.
        actual_sum = sum(nums)
        return expected_sum - actual_sum

        
 ## Time complexity O(n) because Python’s sum() function iterates through the entire nums list once to add all values together
 ## Space complexity O(1)