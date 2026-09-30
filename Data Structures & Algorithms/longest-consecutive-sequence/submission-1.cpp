class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int res = 0;

        for (int num : nums){
            if (!numSet.count(num - 1)){
                int length = 0;
                while (numSet.count(num + length)){
                    length++;
                }
                res = max(res, length);
            }
        }
        return res;
    }
};
