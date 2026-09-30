class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> s;
        
        for (int i = 0; i < n; i++){
            int diff = target - nums[i];
            if (s.find(diff) != s.end()){
                return  {s[diff], i};
            }
            s.insert({nums[i], i});
        }
        return {};
    }
};
