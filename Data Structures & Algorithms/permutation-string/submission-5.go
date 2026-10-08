func checkInclusion(s1 string, s2 string) bool {
    if len(s1) > len(s2) { 
        return false
    }

    s1count := make([]int, 26)
    s2count := make([]int, 26)
    for i := 0; i < len(s1); i++ {
        s1count[s1[i] - 'a']++ 
        s2count[s2[i] - 'a']++
    }

    matches := 0
    for i := range(26){
        if s1count[i] == s2count[i]{
            matches++
        }
    }

    l := 0
    for r := len(s1); r < len(s2); r++ {
        if matches == 26 {
            return true
        }

        index := s2[r] - 'a'
        s2count[index]++

        if s1count[index] == s2count[index] {
            matches += 1
        } else if s1count[index] + 1 == s2count[index] {
            matches -= 1
        }

        index = s2[l] - 'a'
        s2count[index]--
        if s1count[index] == s2count[index] {
            matches += 1
        } else if s1count[index] - 1 == s2count[index] {
            matches -= 1
        }

        l++
    }
    return matches == 26


}
