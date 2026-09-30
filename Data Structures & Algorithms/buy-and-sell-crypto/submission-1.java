class Solution {
    public int maxProfit(int[] prices) {
        int res = 0, lowest = prices[0];

        for (int p: prices){
            if (p < lowest){
                lowest = p;
            }
            res = Math.max(res, p - lowest);
        }
        return res;
    }
}
