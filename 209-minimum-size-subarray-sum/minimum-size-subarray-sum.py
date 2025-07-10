class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int

        understand
            -Output :int
            -Input: int
            -Constraints: time and space complexity
            -Edge cases: empty array
        plan
            - Use sliding windows to track the size of subarray

        """
        min_length = float('inf') ## initialize the min length to infinity
        summ = 0                  ## initialize the sum to keep track of the current window sum
        left = 0                     ## initialize the left pointer

        for right in range (len(nums)):
            summ += nums [right]
            ## while we have a valid window, meaning sum is great/equal to the target
            while summ >= target:  
            ## compares the min length and the current lenght and returns the min between them.
                min_length = min(min_length, right-left+1) 
                ## adjust the sum to decrease the window by subracting l from the window,
                summ -= nums[left]  
                left +=1           ## move the pointer down

        return min_length if min_length < float('inf') else 0        


