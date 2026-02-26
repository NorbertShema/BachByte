class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Understand:
                input : int(nums) and int(target)
                output: the indices of the two numbers that adds up to a target
                constraints exactly one solution, and you may not use the same element twice.

            
Time O(n)
Space O(n) because we are using a dict

        """
    
        seen = {}

        for i, num in enumerate(nums):
            x = target - num
            
            if x in seen:
                return [ seen[x], i]

            seen [num] = i    
            
