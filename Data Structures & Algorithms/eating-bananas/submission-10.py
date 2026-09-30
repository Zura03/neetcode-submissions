class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=0
        while l<=r:
            total=0
            m=l+(r-l)//2
            for pile in piles:
                total+=math.ceil(pile/m)
            if total<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res