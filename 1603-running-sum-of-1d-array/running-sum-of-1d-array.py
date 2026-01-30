class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        Sum = 0
        Running_Sum = []

        for num in nums:
            Sum+= num
            Running_Sum.append(Sum)   

        return Running_Sum    

