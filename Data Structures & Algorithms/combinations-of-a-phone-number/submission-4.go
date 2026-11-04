func letterCombinations(digits string) []string {
	lmap := map[byte][]string{
        '2' : {"a", "b", "c"},
        '3' : {"d", "e", "f"},
        '4' : {"g", "h", "i"},
        '5' : {"j", "k", "l"},
        '6' : {"m", "n", "o"},
        '7' : {"p", "q", "r", "s"},
        '8' : {"t", "u", "v"},
        '9' : {"w", "x", "y", "z"},
    }

    res := []string{}
    subres := ""
    var dfs func(i int)
    dfs = func(i int) {
        if i == len(digits){
            res = append(res, subres)
            return
        }

        for _, c := range(lmap[digits[i]]) {
            subres += c
            dfs(i + 1)
            subres = subres[:len(subres) - 1]
        }
    }

    dfs(0)
    if res[0] == ""{
        return []string{}
    }
    return res
}
