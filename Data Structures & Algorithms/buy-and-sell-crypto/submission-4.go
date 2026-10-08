func maxProfit(prices []int) int {
    l, r := 0, 1
    res := 0

    for r < len(prices) {
        if prices[r] > prices[l]{
            res = max(res, prices[r] - prices[l])
        } else {
            l = r
        }
        r++
    }
    return res
}
