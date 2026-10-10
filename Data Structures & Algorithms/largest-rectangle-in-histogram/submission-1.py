class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index, height
        res = 0

        for i, h in enumerate(heights):
            idx = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                res = max(res, (i - index) * height)
                idx = index
            stack.append((idx, h))

        while stack:
            index, height = stack.pop()
            res = max(res, (len(heights) - index) * height)

        return res