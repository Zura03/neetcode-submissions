# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, maxval):
            if not root:
                return 0

            maxval = max(maxval, root.val)
            left = helper(root.left, maxval)
            right = helper(root.right, maxval)
            return left + right + (1 if maxval <= root.val else 0)

        res = helper(root, float("-inf"))
        return res