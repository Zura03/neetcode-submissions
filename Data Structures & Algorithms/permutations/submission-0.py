class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            subRes = []
            for p in perms:
                for i in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(i, n)
                    subRes.append(pcopy)
                perms = subRes
        
        return perms