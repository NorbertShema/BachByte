class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Understand:
                -Input: list (int)
                -Output: bool (true/false)
                -Constraints: time/space complexity, 
                -Edge cases: empty list

        plan:
            -Use set to avoid duplicates  
            -Make an iteration to check if the num is in the set, 
            if not add it. other keep moving until we reach the end of the list
            -if the list is empty , then return true since we have no dups


        Implement:
          

        """
        seen = set ()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False   


        ##Time O(n)   
        ##Space O(1)



        