class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                my.append(int(i))
            else:
                a=my.pop()
                b=my.pop()
                if i=='+':
                    my.append(b+a)
                if i=='-':
                    my.append(b-a)
                if i=='*':
                    my.append(b*a)
                if i=='/':
                    my.append(int(b/a))
        return my[0]