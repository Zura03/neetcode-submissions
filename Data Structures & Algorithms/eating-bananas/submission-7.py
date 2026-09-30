class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(s):
            total=0
            for pile in piles:
                total+=math.ceil(pile/s)
            return total<=h
        
        left,right=1,max(piles)
        result=right
        
        while left<=right:
            m=left+(right-left)//2
            if valid(m):
                result=m
                right=m-1
            else:
                left=m+1
        return result
