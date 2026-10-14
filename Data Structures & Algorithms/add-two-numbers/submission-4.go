/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    carry := 0

    var v1 int
    var v2 int
    var val int

    for l1 != nil || l2 != nil || carry != 0 {
        if l1 != nil {
            v1 = l1.Val
        } else {
            v1 = 0
        }
        if l2 != nil {
            v2 = l2.Val
        } else {
            v2 = 0
        }

        val = v1 + v2 + carry
        carry = val / 10
        val = val % 10
        cur.Next = &ListNode{Val : val}

        cur = cur.Next
        if l1 != nil {
            l1 = l1.Next
        } else {
            l1 = nil
        }
        if l2 != nil {
            l2 = l2.Next
        } else {
            l2 = nil
        }
    }

    return dummy.Next
}
