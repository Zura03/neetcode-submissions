type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    encoded := ""
    for _, str := range(strs){
        encoded += strconv.Itoa(len(str)) + "#" + str
    }
    return encoded
}

func (s *Solution) Decode(encoded string) []string {
    i := 0
    var res []string
    for i < len(encoded){
        j := i
        for encoded[j] != '#'{
            j++
        }
        length, _ := strconv.Atoi(encoded[i:j])
        i = j + 1
        j = i + length
        res = append(res, encoded[i:j])
        i = j
    }
    return res
}
