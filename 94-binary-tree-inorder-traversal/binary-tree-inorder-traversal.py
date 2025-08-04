# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        Understand
            Input:
                - root: root node of a binary tree

            Output:
                - List of integers representing inorder traversal of the tree
                  (Left → Node → Right)

            Constraints:
                - Tree node values are integers
                - Tree may be empty or unbalanced

            Edge Cases:
                - If root is None → return []
                - Tree with a single node → return [root.val]
                - Skewed trees (only left or right children)

        Match: Binary Tree + Inorder Traversal

        Plan:
            - Initialize an empty result list
            - Define a helper function `inorder(node)`:
                - If node is None, return
                - Recursively call left subtree
                - Append current node’s value to result
                - Recursively call right subtree
            - Call helper on root
            - Return the result list

        Implement
        """
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
