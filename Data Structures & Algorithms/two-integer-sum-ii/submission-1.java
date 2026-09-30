class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int L = 0, R = numbers.length - 1;

        while (L < R){
            int curSum = numbers[L] + numbers[R];
            if (curSum == target){
                return new int[] {L+1, R+1};
            }
            if (curSum > target){
                R--;
            }
            else {
                L++;
            }
        }
        return new int[0];
    }
}
