class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0){
            return 0;
        }

        int L = 0, R = height.length - 1;
        int leftMax = height[L], rightMax = height[R];
        int res = 0;
        while (L < R){
            if (leftMax < rightMax){
                L++;
                leftMax = Math.max(leftMax, height[L]);
                res += leftMax - height[L];
            }
            else {
                R--;
                rightMax = Math.max(rightMax, height[R]);
                res += rightMax - height[R];
            }
        }
        return res;
    }
}
