func partition(s string) [][]string {
    res := [][]string{}
    subres := []string{}

    var dfs func(i int)
    dfs = func(i int) {
        if i == len(s){
            tmp := make([]string, len(subres))
            copy(tmp, subres)
            res = append(res, tmp)
            return
        }

        for j:= i; j < len(s); j++ {
            if isPalin(s, i, j){
                subres = append(subres, s[i:j + 1])
                dfs(j + 1)
                subres = subres[:len(subres) - 1]
            }
        }
    }

    dfs(0)
    return res
}

func isPalin(s string, l, r int) bool {
    for l < r {
        if s[l] != s[r] {
            return false
        }
        l++
        r--
    }
    return true
}
