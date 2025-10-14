# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool

        Understand:
            Input: root of a binary tree, and an integer targetSum
            Output: True if any root-to-leaf path adds up to targetSum.

        Match: Tree, DFS

        Plan:
            - If the node is None, return False.
            - If it's a leaf and value equals targetSum → return True.
            - Recursively check left and right subtrees with updated targetSum.
            - Return True if either path returns True.

        Implement:
        """

        def dfs(node, remaining):
            if not node:
                return False

            if not node.left and not node.right:  # the leaf node
                return node.val == remaining

            remaining -= node.val

            return dfs(node.left, remaining) or dfs(node.right, remaining)

        return dfs(root, targetSum)
