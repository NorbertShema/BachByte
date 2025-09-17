class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Understand:
            - Input: list of integers (nums) and a target integer (target)
            - Output: list containing the indices of the two numbers that add up to target
            - Constraints: 
                - Exactly one valid solution exists
                - Cannot use the same element twice
            - Edge cases: empty array (though not applicable here since a solution is guaranteed)

        Match:
            - Use a hash map (dictionary) to store numbers and their indices
            - This allows O(1) average lookup to check for complements

        Plan:
            - Initialize an empty hash map (lookup)
            - Iterate through nums with index and value
            - For each number, compute complement = target - num
            - If complement exists in lookup, return [lookup[complement], i]
            - Otherwise, store num with its index in lookup

        Implement:
    

        Complexity:
            - Time Complexity: O(n)
                We loop through nums once (O(n)), and each dictionary operation
                (lookup and insertion) is O(1) average → total O(n).
            - Space Complexity: O(n)
                In the worst case, we store all n elements in the dictionary.
        """

        lookup = {}

        for i, num in enumerate(nums):       # Iterate with index and value
            x = target - num                 # Complement needed to reach target

            if x in lookup:                  # If complement is already in dictionary
                return [lookup[x], i]        # Return indices of both numbers

            lookup[num] = i                  # Store current number with its index




# Time Complexity: O(n) 
# Space Complexity: O(n)