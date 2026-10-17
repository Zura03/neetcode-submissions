type MinHeap [][]int

func (h MinHeap) Len() int {return len(h)}
func (h MinHeap) Less(i, j int) bool {return h[i][0] < h[j][0]}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j] , h[i]}
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.([]int))}
func (h *MinHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func kClosest(points [][]int, k int) [][]int {

    distances := [][]int{}
    for i, p := range points {
        x, y := p[0], p[1]
        dist := (x * x) + (y * y)
        distances = append(distances, []int{dist, i})
    }
    minHeap := MinHeap(distances)
    heap.Init(&minHeap)

    res := [][]int{}
    for k > 0 {
        index := heap.Pop(&minHeap).([]int)[1]
        res = append(res, points[index])
        k--
    }
    return res
}
