type TrieNode struct {
    children map[byte]*TrieNode
    word bool
}

func NewTrieNode() *TrieNode {
    return &TrieNode{children : make(map[byte]*TrieNode)}
}

type WordDictionary struct {
    root *TrieNode
}

func Constructor() WordDictionary {
    return WordDictionary{root : NewTrieNode()}
}

func (this *WordDictionary) AddWord(word string)  {
    cur := this.root
    for i := range word {
        c := word[i]
        if cur.children[c] == nil {
            cur.children[c] = NewTrieNode()
        }
        cur = cur.children[c]
    }
    cur.word = true
}

func (this *WordDictionary) Search(word string) bool {
    var dfs func(i int, root *TrieNode) bool

    dfs = func(i int, root * TrieNode) bool {
        cur := root
    
        for j := i; j < len(word); j++ {
            c := word[j]

            if c == '.' {
                for _, child := range cur.children {
                    if child != nil && dfs(j + 1, child) {
                        return true
                    }
                }
                return false
            } else {
                if cur.children[c] == nil {
                    return false
                }
                cur = cur.children[c]
            }
        }
        return cur.word
    }

    return dfs(0, this.root)
}
