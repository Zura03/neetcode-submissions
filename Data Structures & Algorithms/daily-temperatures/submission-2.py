class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[]
        for i,j in enumerate(temperatures):
            while st and j>st[-1][0]:
                stackt,stacki=st.pop()
                res[stacki]=i-stacki
            st.append([j,i])
        return res