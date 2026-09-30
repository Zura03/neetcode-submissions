class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=0
        while left<right:
            area=(right-left)*min(heights[left],heights[right])
            if area>maxarea:
                maxarea=area
            
            if (heights[left])>heights[right]:
                right-=1
            else:
                left+=1
        return maxarea