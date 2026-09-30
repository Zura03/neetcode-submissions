class Solution:
    def isValid(self, s: str) -> bool:
        my=[]
        mapp={']':'[',')':'(','}':'{'}
        for i in s:
            if i in {'{','(','['}:
                my.append(i)
            else:
                if my and mapp[i]==my[-1]:
                    my.pop()
                else:
                    return False
        if not my:
            return True
        
        return False                
            
