class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R
        while L <= R:
            hours = 0
            k = (L + R) // 2
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                R = k - 1
                res = k
            else:
                L = k + 1

        return res