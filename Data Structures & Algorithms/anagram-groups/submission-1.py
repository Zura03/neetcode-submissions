class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map={}

        for each in strs:
            count=[0]*26
            
            for char in each:
                count[ord(char)-ord('a')]+=1
            
            count_tuple=tuple(count)

            if count_tuple not in anagram_map:
                anagram_map[count_tuple]=[]
            anagram_map[count_tuple].append(each)
        return list(anagram_map.values())