# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        def dfs(node, maxval):
            nonlocal good
            if not node:
                return
            
            if node.val >= maxval:
                maxval = node.val
                good += 1
            dfs(node.left, maxval)
            dfs(node.right, maxval)

        dfs(root, root.val)
        return good