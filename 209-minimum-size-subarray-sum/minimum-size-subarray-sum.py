class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int

        plan
            - Use sliding windows to track the size of subarray
        """
        min_length = float('inf')
        summ = 0
        l = 0 ## length

        for r in range (len(nums)):
            summ += nums [r]

            while summ >= target:
                min_length = min(min_length, r-l+1)
                summ -= nums [l]
                l +=1

        return min_length if min_length < float('inf') else 0        


