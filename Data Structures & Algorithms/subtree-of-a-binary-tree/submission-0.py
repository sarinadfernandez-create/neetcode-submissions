# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #how would I check if I could only check one node at a time and wanted to be efficient?
        # if a subtree of root is not in subroot, no tree containing that subtree can be subroot
        # let me simplify, how do I just compare two trees for similarity.
        # always return early if nodeA != nodeB
            # check root node first
            # then check left and right nodes
        if not root:
            return False
        
        def sameTree(root1, root2):
            if not root1 and root2: return False
            if not root2 and root1: return False
            if not root1 and not root2: return True
            # they are both roots, will see if above is necessary
            if root1.val!=root2.val:
                return False
            left, right = sameTree(root1.left,root2.left), sameTree(root1.right, root2.right)
            if left and right:
                return True
            else:
                return False

        if sameTree(root, subRoot):
            return True
        else:
            if self.isSubtree(root.left, subRoot) or  self.isSubtree(root.right, subRoot):
                return True
        
        return False




        
