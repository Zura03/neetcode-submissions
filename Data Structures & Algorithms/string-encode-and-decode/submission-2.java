class Solution {

    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        for (String s: strs){
            encodedString.append(s.length()).append("#").append(s);
        }
        return encodedString.toString();
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();
        int i = 0;
        while (i < str.length()){
            int j = i;
            while (str.charAt(j) != '#'){
                j++;
            }
            int length = Integer.valueOf(str.substring(i, j));
            i = j + 1;
            j = i + length;
            list.add(str.substring(i, j));
            i = j;
        }
        return list;
    }
}
