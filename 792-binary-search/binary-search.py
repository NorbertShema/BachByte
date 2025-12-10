class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Understand:
            Input: - List [nums]: an array on integers sorted in asc order
                   - int[target]: an integer target 

            Output: int[index]: the index of the target in the array[nums]

            Constraints:
                    -time complexity: o(log n)
                    -All the integers in nums are unique.
                    -nums is sorted in ascending order.

            Edge cases:
                -Empty array

        Match:
            -Binary search 0(log n )

        Plan:
            -intilize the points to the first and last index in the array
        -while left <= right:
            -find the mid = (left+right)//2
            - if nums[mid] == target:
                - return mid

            -if nums[mid] < target:
                -left = mid +1
            -else:
                - right = mid -1 

        return -1 


        Implement:
        """
        left = 0
        right =len(nums)-1

        while left <= right:
            mid = (left + right )//2
            
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid -1
            else:
                left = mid +1

        return -1
