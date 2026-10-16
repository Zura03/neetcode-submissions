/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    q := []*TreeNode{}

    if root != nil {
        q = append(q, root)
    }
    
    var res [][]int
    for len(q) != 0 {
        subres := []int{}
        for range len(q) {
            node := q[0]
            q = q[1:]
            subres = append(subres, node.Val)
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        res = append(res, subres)
    }
    return res
}
