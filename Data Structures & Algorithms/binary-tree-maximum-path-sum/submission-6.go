/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxPathSum(root *TreeNode) int {
    res := -math.MaxInt

    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return 0
        }

        left := dfs(node.Left)
        right := dfs(node.Right)
        
        res = max(res, left + node.Val + right) 

        return max(0, left + node.Val, right + node.Val)
    }

    dfs(root)
    return res
}
