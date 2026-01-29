class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Understand:
                input : int(nums) and int(target)
                output: the indices of the two numbers
                constraints exactly one solution, and you may not use the same element twice.
        """
    
        lookup = {}

        for i, num in enumerate(nums):
            x = target - num
            
            if x in lookup:  # Check if complement exists
                return [lookup[x], i]  # Return stored index and current index
            
            lookup[num] = i  # Store number -> index mapping
            