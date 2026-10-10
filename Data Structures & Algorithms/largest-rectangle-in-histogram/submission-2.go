func largestRectangleArea(heights []int) int {
    stack := make([][2]int, 0) // index, height
    res := 0

    for i, h := range heights {
        idx := i
        for len(stack) > 0 && stack[len(stack) - 1][1] > h {
            index:= stack[len(stack) - 1][0]
            height := stack[len(stack) - 1][1]
            stack = stack[:len(stack) - 1]
            res = max(res, (i - index) * height)
            idx = index
        }
        stack = append(stack, [2]int{idx, h})
    }

    for len(stack) > 0 {
        index:= stack[len(stack) - 1][0]
        height := stack[len(stack) - 1][1]
        stack = stack[:len(stack) - 1]
        res = max(res, (len(heights) - index) * height)
    }

    return res
}
