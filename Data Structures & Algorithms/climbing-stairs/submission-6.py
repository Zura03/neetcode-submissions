class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 1, 1
        n -= 2
        while n >= 0:
            temp = one
            one = one + two
            two = temp
            n -= 1
        return one
