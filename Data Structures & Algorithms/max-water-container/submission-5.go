func maxArea(heights []int) int {
    l, r := 0, len(heights) - 1
    res := 0

    for l < r {
        a := (r - l)*min(heights[l], heights[r])
        if a > res{
            res = a
        }
        if heights[l] < heights[r]{
            l++
        } else {
            r--
        }
    }
    return res
}
