# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        
        def height(node):
            if not node: return 0
            l = height(node.left)
            r = height(node.right)
            self.best = max(self.best, l+r)
            return 1+ max(l, r)
        
        height(root)
        return self.best
        
        
        
   # left, right = self.maxDepth(root.left)+1, self.maxDepth(root.right)+1
    #    return max(left, right)