class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Understand:
            Input: array (nums) and int(target)
            Output: index of the target: nums[target]
            Constraints: 
                -Time complexity of o(log n)
                -nums is sorted so we perform binary search
                - all integers in nums are unique.
                
            Edge cases:
                -Empty array(nums): Here I would return -1
                -no target found: return -1

        Plan: The goal is to search in the nums, and return the index of the target if found, otherwise return -1

            -initilize the points to the first and last index in the array
            -while left <= right:
                -find the mid = (left+right)//2
                - if nums[mid] == target:
                    - return mid

                -if nums[mid] < target:
                    -left = mid +1
                -else:
                    - right = mid -1 

            return -1 


        """
        
        left = 0
        right = len(nums)-1

        while left <= right: 
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid+1

            else:
                right = mid -1

        return -1         


