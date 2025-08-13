# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        # Map from node value to its index in inorder traversal for O(1) lookups
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Use a pointer for preorder list
        self.pre_index = 0
        
        def array_to_tree(left, right):
            # If there are no elements to construct subtree
            if left > right:
                return None
            
            # Pick current root from preorder traversal
            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)
            
            # Move to next preorder index
            self.pre_index += 1
            
            # Build left and right subtrees
            root.left = array_to_tree(left, inorder_index_map[root_val] - 1)
            root.right = array_to_tree(inorder_index_map[root_val] + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)
