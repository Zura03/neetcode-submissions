# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res=[True]

        def depth(root):
            if not root:
                return 0
            l=depth(root.left)
            r=depth(root.right)
            if abs(l-r)>1:
                res[0]=False
            return 1+max(l,r)
        depth(root)

        return res[0]