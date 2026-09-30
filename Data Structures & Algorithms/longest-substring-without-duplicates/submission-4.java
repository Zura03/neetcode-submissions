class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> chars = new HashSet<>();
        int res = 0, L = 0;

        for (int r = 0; r < s.length(); r++){
            while (chars.contains(s.charAt(r))){
                chars.remove(s.charAt(L));
                L++;
            }
            chars.add(s.charAt(r));
            res = Math.max(res, r - L + 1);
        }
        return res;

    }
}
