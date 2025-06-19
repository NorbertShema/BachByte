class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        Map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in Map:
                return [Map[diff], i]
                
            Map[n] = i