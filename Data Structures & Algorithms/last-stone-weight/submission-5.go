type MaxHeap []int

func (h MaxHeap) Len() int { return len(h)}
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j]}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i]}
func (h *MaxHeap) Push(x interface{}) { *h = append(*h, x.(int))}
func (h *MaxHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func lastStoneWeight(stones []int) int {
    pq := &MaxHeap{}
    heap.Init(pq)

    for _, s := range stones {
        heap.Push(pq, s)
    }

    for pq.Len() > 1 {
        x := heap.Pop(pq).(int)
        y := heap.Pop(pq).(int)

        if x != y {
            heap.Push(pq, x - y)
        }
    }

    heap.Push(pq, 0)
    return heap.Pop(pq).(int)
}
