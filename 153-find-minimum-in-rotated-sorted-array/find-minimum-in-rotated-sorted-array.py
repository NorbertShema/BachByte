class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid +1

            else:
                right = mid ## here the mid could also be the min.

        return nums[left] ## here since left = right, we can return which ever              



