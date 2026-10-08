func lengthOfLongestSubstring(s string) int {
    charSet := make(map[rune]bool)
    l := 0
    res := 0

    for r, c := range(s){
        for charSet[rune(s[r])] {
            delete(charSet, rune(s[l]))
            l++
        }
        charSet[c] = true
        res = max(res, r - l + 1)
    }
    return res
}
