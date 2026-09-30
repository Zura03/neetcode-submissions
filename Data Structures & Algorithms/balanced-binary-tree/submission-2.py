# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [0, True]

            left, vl = dfs(root.left)
            right, rl = dfs(root.right)

            if abs(left - right) <= 1 and vl and rl:
                return [1 + max(left, right), True]
            return [-1, False]

        return dfs(root)[1]