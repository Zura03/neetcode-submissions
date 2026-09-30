class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curSet = new ArrayList<>();
        backtrack(0, nums, curSet, target, 0, res);
        return res;
    }

    public void backtrack(int i, int[] nums, List<Integer> curSet, int target, int curSum, List<List<Integer>> res){
        if (curSum == target) {
            res.add(new ArrayList(curSet));
            return;
        }

        if (curSum > target || i == nums.length){
            return;
        }

        // include nums[i]
        curSet.add(nums[i]);
        backtrack(i, nums, curSet, target, curSum + nums[i], res);
        curSet.remove(curSet.size() - 1);

        //exclude nums[i]
        backtrack(i + 1, nums, curSet, target, curSum, res);

    }
}
