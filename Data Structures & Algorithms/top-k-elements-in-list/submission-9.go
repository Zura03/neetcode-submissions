func topKFrequent(nums []int, k int) []int {
    freqMap := make(map[int]int)
    freq := make([][]int, len(nums)+1)

    for _, n := range(nums){
        freqMap[n]++
    }

    for key, val := range(freqMap){
        freq[val] = append(freq[val], key)
    }

    var res []int
    for i := len(nums); i > 0; i--{
        for _, n := range(freq[i]){
            res = append(res, n)
            if len(res) == k{
                return res
            }
        }
    }
    return []int{}
}
