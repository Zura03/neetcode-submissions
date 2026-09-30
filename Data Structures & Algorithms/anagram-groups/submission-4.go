func groupAnagrams(strs []string) [][]string {
    countMap := make(map[[26]int][]string)

    for _, s := range strs {
        var temp [26]int
        for j := range(len(s)){
            temp[s[j] - 'a']++
        }
        countMap[temp] = append(countMap[temp], s)
    }

    var res [][]string
    for _, value := range countMap {
        res = append(res, value)
    }
    return res
}
