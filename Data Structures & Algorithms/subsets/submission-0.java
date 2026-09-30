class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curSet = new ArrayList<>();
        int n = nums.length;
        backtrack(nums, 0, curSet, n, res);
        return res;
    }

    public void backtrack(int[]nums, int i, List<Integer> curSet, int n, List<List<Integer>> res){
        if (i == n) {
            res.add(new ArrayList<>(curSet));
            return;
        }

        //include nums[i]
        curSet.add(nums[i]);
        backtrack(nums, i + 1, curSet, n, res);
        curSet.remove(curSet.size() - 1);

        //exclude nums[i]
        backtrack(nums, i + 1, curSet, n, res);
    }
}
