type TimeMap struct {
    m map[string][]pair
}

type pair struct {
    timestamp int
    value     string
}

func Constructor() TimeMap {
    return TimeMap{
        m: make(map[string][]pair),
    }
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
    this.m[key] = append(this.m[key], pair{timestamp, value})
}

func (this *TimeMap) Get(key string, timestamp int) string {
    if _, exists := this.m[key]; !exists {
        return ""
    }

    pairs := this.m[key]
    l, r := 0, len(pairs) - 1
    res := ""

    for l <= r {
        m := (l + r) / 2
        if pairs[m].timestamp <= timestamp{
            res = pairs[m].value
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return res
}
