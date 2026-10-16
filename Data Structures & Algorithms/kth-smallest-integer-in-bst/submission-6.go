/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    
    cur := root
    stack := []*TreeNode{}

    for len(stack) != 0 || cur != nil {
        for cur != nil {
            stack = append(stack, cur)
            cur = cur.Left
        }
        cur = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        k -= 1
        if k == 0 {
            return cur.Val
        }
        cur = cur.Right
    }
    return -1
}
