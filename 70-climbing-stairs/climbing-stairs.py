class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        Understand
            Input: Int (number of steps n)
            Output: Int (number of distinct ways to climb to the top)
            Constraints: 
                - At each step, you can either climb 1 or 2 steps
                - n >= 1
            Edge cases:
                - n = 1 → only 1 way
                - n = 2 → two ways: (1+1) or (2)

        Plan:
            - This is a Fibonacci-like problem
            - Ways to reach step n = ways to reach (n-1) + ways to reach (n-2)
            - Use dynamic programming / iterative approach to avoid recursion overhead
            - Keep track of only the last two results to save memory

        Implement:
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two steps
        one_step_before = 2  # ways to reach step 2
        two_steps_before = 1  # ways to reach step 1
        
        # Variable to store the current number of ways
        all_ways = 0

        # Build up the number of ways from step 3 to step n
        for i in range(3, n + 1):
            all_ways = one_step_before + two_steps_before  # recurrence relation
            two_steps_before = one_step_before  # shift window
            one_step_before = all_ways  # update
        
        return all_ways

    # Time: O(n) → we compute each step once
    # Space: O(1) → only store a few variables instead of full DP array
