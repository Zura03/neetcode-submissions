# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val
        def helper(root):
            nonlocal res
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            res = max(res, leftMax + rightMax + root.val)
            return max(root.val + leftMax, root.val + rightMax,
                        root.val)

        helper(root)
        return res