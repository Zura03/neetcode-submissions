class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]
        
        for num in nums:
            sub = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    newPerm = perm.copy()
                    newPerm.insert(i, num)
                    sub.append(newPerm)
            perms = sub

        return perms