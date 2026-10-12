func minEatingSpeed(piles []int, h int) int {
    l, r := 1, 0
    for _, p := range piles {
        if p > r {
            r = p
        }
    }
    res := r

    for l <= r {
        k := (l + r) / 2

        hours := 0
        for _, p := range piles {
            hours += int(math.Ceil(float64(p)/float64(k))) // '/' does integer division if both are integers, so 4/3 will be 1 but we need ceil[1.33] = 2. so covert p and k to floats first -> float division
        }

        if hours <= h {
            res = k
            r = k - 1
        } else {
            l = k + 1
        }
    }
    return res
}
