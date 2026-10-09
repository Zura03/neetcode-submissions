func isValid(s string) bool {
    stack := []rune{}
    pmap := map[rune]rune{
        ')' : '(' ,
        '}' : '{' ,
        ']' : '[' ,
    }

    for _, c := range s {
        if _, exists := pmap[c]; !exists {
            stack = append(stack, c)
        } else {
            if len(stack) > 0 && stack[len(stack) - 1] == pmap[c] {
                stack = stack[:len(stack) - 1]
            } else {
                return false
            }
        }
    }
    return len(stack) == 0
}