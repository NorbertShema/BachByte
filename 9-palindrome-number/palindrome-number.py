class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        Understand:
            Input: int
            Output: Boolean ( true/false)
            Constraint: Time/space complexity
            Edge case: ,,,,

        plan:
            -Convert the (int) into a (str) for easy index reference
            - Use two pointers to compare the string a the indices.

        Implement        
        """

        string = str (x)
        left ,right = 0 , len(string)-1

        while left < right:
            if string [left] != string[right]:
                return False
            left += 1
            right -= 1

        return True        