# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool

Understand:
    Input:root node
    Ouput: Bool
    Constraints: time/space complexity
    Edge case: not root (return true)

Match: Binary search trees(DFS)

Plan:
 
     -Define a helper function isSameTree(p, q):
    -If both are None, return True.
    -If one is None and the other isn’t, return False.
    -If values differ, return False.
    -Recursively check left and right subtrees.
    -Traverse the root tree:
    -At each node, check if the subtree starting here matches subRoot using isSameTree.
            -If match found, return True.
            -Otherwise, check in left and right children
            -If we reach the end without finding a match, return False.

Implement:

        """
        def sameTree(p,q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree (p.right, q.right)

        def has_subtree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True

            return has_subtree (root.left) or has_subtree(root.right)
        return has_subtree(root)    

## time complexity: O(m*n)
##space:O(n)