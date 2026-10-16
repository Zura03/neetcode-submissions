/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func goodNodes(root *TreeNode) int {
    
    var dfs func (node *TreeNode, maxval int) int

    dfs = func (node *TreeNode, maxval int) int {
        if node == nil {
            return 0
        }

        good := 0
        if node.Val >= maxval {
            good = 1
        }
        maxval = max(maxval, node.Val)
        return good + dfs(node.Left, maxval) + dfs(node.Right, maxval)
    }

    return dfs(root, root.Val)
}
