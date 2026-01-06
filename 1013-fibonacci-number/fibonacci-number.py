class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int


        Understand: Create a F numbers such that each number is the sum of two prev number.
            Input: int (n)

            Output: the sum at int (n)

            Constraints :
                -0 <= n <= 30

            Edge cases: These are the base case give when F(0) = 0, F(1) = 1

        Plan: Use recursion to call the stack function for n
            -Perform the edge cases
                -F(0) = 0, F(1) = 1
            - recursion part
                - F(n>1)

           -We can also use Dynamic programming 
            -   Top down memerazation
            _Bottom up tablation   
            -Botton up no tabluation( this is the most optimal way)

        Implement:  

        """
        if n== 0:
            return 0
        if n==1:
            return 1 
        
        if n>1:
            return self.fib(n-1) + self.fib(n-2)

