class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Understand:Here we will do a normal binary search, instead of returning -1 if not found, we will
        check to see where would the target be compared to the mid.

        

        Plan:

        Implement:


        """
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left +right)//2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid +1

            else:
                right = mid -1

        if nums [mid]< target:
            return mid +1

        else: 
            return mid                