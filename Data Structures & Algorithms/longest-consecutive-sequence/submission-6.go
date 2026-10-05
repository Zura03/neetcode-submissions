func longestConsecutive(nums []int) int {
    
    nset := make(map[int]bool)
    longest := 0

    for _, n:= range nums{
        nset[n] = true
    }

    for n := range nset{
        if _, found := nset[n-1]; !found{
            l := 0
            for {
                if _, exists := nset[n+l]; exists{
                l++
                } else {
                    break
                }
            }
            if l > longest{
                longest = l
            }
        }
    }
    return longest
}