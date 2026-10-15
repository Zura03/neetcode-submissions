/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isBalanced(root *TreeNode) bool {
    
    var dfs func(root *TreeNode) Result
    dfs = func(root *TreeNode) Result {
        if root == nil {
            return Result{0, true}
        }

        left := dfs(root.Left)
        right := dfs(root.Right)

        balanced := left.balanced && right.balanced && abs(left.height - right.height) <= 1

        return Result{1 + max(left.height, right.height), balanced}
    }

    return dfs(root).balanced
}

type Result struct {
    height   int
    balanced bool
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
