class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int L = 1, R = *max_element(piles.begin(), piles.end());
        int res = R;
        while (L <= R){
            int m = (L + R)/2;
            long hours = 0;
            for(int p : piles){
                hours += ceil(static_cast<double>(p)/m);
            }
            if(hours <= h){
                R = m - 1;
                res = m;
            }
            else{
                L = m + 1;
            }
        }
        return res;
    }
};
