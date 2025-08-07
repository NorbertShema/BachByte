# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int

        Understand:
            Input: Binary tree
            Output: number of nodes(int)
            Constraints: time/space complexity
            Edge cases: not node( no tree) return 0 as the depth

        Match:
            -DFS (binary search trees)

        Plan:
            -Check to see if we have a root ( return 0 if no root (tree))
            -Otherwise: check the left and right side of the root to check for depth
            -return the max depth

        Implement:
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+ max(left, right)

        ## time complexity O(n)
        ## space complexity O(h)