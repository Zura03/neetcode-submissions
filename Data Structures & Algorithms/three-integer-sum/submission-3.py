class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            target=-nums[i]
            l,r=i+1,len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                curr=nums[l]+nums[r]
                if curr==target:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif curr<target:
                    l+=1
                elif curr>target:
                    r-=1
        return res
