class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Understand:
                Input:
                    -A sorted list of integers nums
                    -An integer target

        Output: a list of indices

        Constraints:
                    -Time complexity must be O(log n) → requires binary search
                    -Array can be empty
                    -Duplicates are allowed
                    -Return [-1, -1] if target not found

        Edge Cases:
                -Empty array 
                -target not in the array
                -Only one element in array
                -All elements are the same
                -target appears at the beginning or end of the array

        Plan:
            -Use binary search to find the first index of target:
            -If found, store the index and move left to search earlier occurrences.
            -Use binary search again to find the last index of target:
            -If found, store the index and move right to search later occurrences.
            -Return [first_index, last_index].

        Implement    
        """

    
        def find_first(nums, target):
            l, r = 0, len(nums) - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        def find_last(nums, target):
            l, r = 0, len(nums) - 1
            index = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        return [find_first(nums, target), find_last(nums, target)]          
            