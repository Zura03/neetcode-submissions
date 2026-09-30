class Solution {
    public int maxArea(int[] heights) {
        int L = 0, R = heights.length - 1;
        int area = 0;
        while (L < R) {
            area = Math.max(Math.min(heights[L], heights[R])*(R - L), area);
            if (heights[L] < heights[R]){
                L++;
            }
            else{
                R--;
            }
        }
        return area;
    }
}
