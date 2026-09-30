# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def depth(root):
            if not root:
                return 0

            l=depth(root.left)
            r=depth(root.right)

            res[0]=max(res[0],l+r)

            return 1+max(l,r)
        depth(root)
        return res[0]