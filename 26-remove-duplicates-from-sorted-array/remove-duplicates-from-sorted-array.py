class Solution(object):
    def removeDuplicates(self, nums):

      
        i = 0  # Pointer to the last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1  # Because 'i' is index-based


        
        