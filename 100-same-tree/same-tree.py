# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):

        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool

        Understand
            Input:
                -p: root node of the first binary tree
                -q: root node of the second binary tree

            Output:
                -True if the trees are the same
                -False otherwise
                
            Constraints:
                -Node values are integers.
                -Nodes can be null (i.e., leafless branches).

            Edge Cases:
                -Both trees are None → return True
                -One tree is None, the other is not → return False
                -Trees with same structure but different values → return False

        Match: Tree traversal

        Plan:
            -We will write a recursive function:
            -Base case 1: if both p and q are None, return True
            -Base case 2: if one is None and the other isn’t, return False
            -If p.val != q.val, return False
            -Recursively compare:
            -p.left with q.left
            -p.right with q.right
            -Return the result of those two recursive calls combined with and        


        Implement

        """

        def balanced(p ,q):   

            if not p and not q:
                return True     ## check if we have the tree nodes

            if (p and not q) or (q and not p):
                return False    ## check if we have both of the trees

            if p.val != q.val:
                return False    ## check if the node value is the same for both trees 

            ## check if the trees are balanced on both left and right sides
            return balanced(p.left, q.left) and balanced(p.right, q.right)

        return balanced(p,q)    
            