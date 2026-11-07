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
            l = height(node.left) # returns + 1 for eith4er of them but not both per turn, basically traverses, which is ohw you trqaverse each only one and know it is a path.
            r = height(node.right)
            self.best = max(self.best, l+r) # set best to whatever l + r is but you arent adding here since this is the path length at current node 
            return 1 + max(l, r) # You are looking at the next node so it is plus 1.
        
        height(root)
        return self.best
        
        
        
   # left, right = self.maxDepth(root.left)+1, self.maxDepth(root.right)+1
    #    return max(left, right)