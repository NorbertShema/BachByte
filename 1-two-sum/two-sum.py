class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Understand:

            -Input: list (int) and a target (int)
            -Output: list of indices
            -Constraint: 
                    -only one solution 
                    - not using the same element twice
            -Edge cases: empty array  


         Plan:
                -Use a hash map to store key:value pairs as (num:index)      
                -since we are guaranteed a solution, we can search for (x = target - num)
                -if found, then return the two indices, otherwise add it to the dictionary
                - no return needed. 


        implement:
                       
        """

        lookup = {}

        for i, num in enumerate(nums):       # Iterate through the list with index and value
            x = target - num                 # two numbers that adds up to the target ( we know num and we know the target)

            if x in lookup:                   # Check if the complement is already in the dictionary
                return [lookup[x], i]         # If found, return the indices of the two numbers
                
            lookup[num] = i                   # Otherwise, store the current number with its index in the dictionary



# Time Complexity: O(n)
# Space Complexity: O(n)
