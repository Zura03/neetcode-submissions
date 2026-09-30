class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countMap = defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            countMap[tuple(temp)].append(s)

        res = []
        for key, value in countMap.items():
            res.append(value)
        return res