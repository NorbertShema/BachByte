 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]

        Understand
            Input:
                - root: the root node of a binary search tree (BST)
                - val: integer value to insert into the tree

            Output:
                - Return the root of the BST after inserting val

            Constraints:
                - The BST must remain valid after insertion
                - Duplicates are not allowed in BST
                - The tree can be empty (root is None)

            Edge Cases:
                - root is None → create and return new TreeNode(val)
                - val is smaller than current node → go left
                - val is greater than current node → go right

        Match: Binary Search Tree property

        Plan:
            - If root is None, return new TreeNode(val)
            - If val < root.val:
                - Recur on root.left and assign result to root.left
            - If val > root.val:
                - Recur on root.right and assign result to root.right
            - Return root at the end

        Implement
        """
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:  # since duplicates are not allowed, val > root.val
            root.right = self.insertIntoBST(root.right, val)

        return root
