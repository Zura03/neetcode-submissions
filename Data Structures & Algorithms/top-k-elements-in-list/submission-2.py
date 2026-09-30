class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res