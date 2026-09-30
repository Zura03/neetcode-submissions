class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = 0

        def climb(step):
            nonlocal res
            if step == n:
                res += 1

            if step > n:
                return

            climb(step + 1)
            climb(step + 2)

        climb(0)
        return res