class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        area = 0
        while L < R:
            area = max(min(heights[L], heights[R])*(R - L), area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return area