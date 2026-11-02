class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]

        for n in nums:
            p = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    subres = perm.copy()
                    subres.insert(i, n)
                    p.append(subres)
                perms = p
        
        return perms