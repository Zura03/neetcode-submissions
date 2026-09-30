class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)] 
        freqMap = {}

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        for key, val in freqMap.items():
            freq[val].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res