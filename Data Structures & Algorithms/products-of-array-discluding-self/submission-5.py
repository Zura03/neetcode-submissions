class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first=[1]*len(nums)
        last=[1]*len(nums)
        prod=[1]*len(nums)
        for i in range(1,len(nums)):
            first[i]=first[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            last[i]=last[i+1]*nums[i+1]
        for i in range(len(nums)):
            prod[i]=first[i]*last[i]
        return prod