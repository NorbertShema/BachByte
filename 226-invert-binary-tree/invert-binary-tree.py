# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]

        Understand:Given the root of a binary tree, invert the tree, and return its root.

            -Input: root (node for a binary tree)
            -Output:root (for the inverted binary tree)
            -Constraints: Time/space complexity
            -Edge cases: Empty root : return None

        Match:DFS

        Plan:
            - check if not root: return None
            - invert the left and right and swipe them
            -invert it recursively 
            -return the root

        Implement:
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

##Time: O(n)
##Time :O(h) (height of the tree) or just 0(n)
        
