class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left ,right = 0, len(nums)-1
        while left <= right:
            mid = (left + right )//2
            
            if target == nums[mid]:
                return mid

            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid +1

        return -1

nums = [-1,0,3,5,9,12]
target = 9 

index = Solution()
print(index.search(nums, target))