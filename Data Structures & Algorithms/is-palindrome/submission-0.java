class Solution {
    public boolean isPalindrome(String s) {
        int L = 0, R = s.length() - 1;
        
        while (L < R){
            while (L < R && !alphaNum(s.charAt(L))){
                L++;
            }
            while (R > L && !alphaNum(s.charAt(R))){
                R--;
            }
            if (Character.toLowerCase(s.charAt(L)) != Character.toLowerCase(s.charAt(R))){
                return false;
            }
            L++; R--;
        }
        return true;
    }

    public boolean alphaNum(char c){
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}
