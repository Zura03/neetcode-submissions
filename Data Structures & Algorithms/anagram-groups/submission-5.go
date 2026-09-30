func groupAnagrams(strs []string) [][]string {
    countMap := make(map[[26]int][]string)

    for _, s := range strs {
        var temp [26]int
        for _, c := range(s){
            temp[c - 'a']++
        }
        countMap[temp] = append(countMap[temp], s)
    }

    var res [][]string
    for _, value := range countMap {
        res = append(res, value)
    }
    return res
}
