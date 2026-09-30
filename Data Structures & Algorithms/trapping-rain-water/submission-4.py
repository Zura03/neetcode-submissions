class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        L, R = 0, len(height) - 1
        leftMax, rightMax = height[L], height[R]

        while L < R:
            if leftMax <= rightMax:
                res += (leftMax - height[L])
                L += 1
                leftMax = max(leftMax, height[L])
            else:
                res += (rightMax - height[R])
                R -= 1
                rightMax = max(rightMax, height[R])

        return res