class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mydic1={}
        for i in s:
            if i in mydic1:
                mydic1[i]+=1
            else:
                mydic1[i]=1
        for i in t:
            if i not in mydic1:
                return False
            else:
                mydic1[i]-=1
                if mydic1[i]==0:
                    del mydic1[i]
        # mydic2={}
        # for i in t:
        #     if i in mydic2:
        #         mydic2[i]+=1
        #     else:
        #         mydic2[i]=1
        return not mydic1