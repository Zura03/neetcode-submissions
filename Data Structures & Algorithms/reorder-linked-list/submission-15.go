/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    slow, fast := head, head.Next

    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    cur := slow.Next
    slow.Next = nil
    var prev *ListNode

    for cur != nil {
        tmp := cur.Next
        cur.Next = prev
        prev = cur
        cur = tmp
    }

    cur = head
    var tmp1 *ListNode
    var tmp2 *ListNode
    for prev != nil {
        tmp1 = cur.Next
        tmp2 = prev.Next
        cur.Next = prev
        prev.Next = tmp1
        cur = tmp1
        prev = tmp2
    }
}
