class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        listsOfNodes = defaultdict(list)
        
        def oneDepth(root, depth):
            if not root:
                return []
            listsOfNodes[depth].append(root.val)
            oneDepth(root.left, depth + 1); 
            oneDepth(root.right, depth + 1)
            return listsOfNodes

        #oneDepth(root, 1)
        returnval = list(dict(oneDepth(root, 1)).values())
        return returnval


        