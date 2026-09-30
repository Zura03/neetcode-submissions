class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=[[]for i in range(n+1)]
        mydic={}
        for num in nums:
            mydic[num] = 1 + mydic.get(num, 0)
        
        for key,value in mydic.items():
            freq[value].append(key)
        res=[]
        for i in range(n,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res