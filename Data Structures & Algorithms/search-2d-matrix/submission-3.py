class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1
        while top<=bot:
            m=top+(bot-top)//2
            if target<matrix[m][0]:
                bot=m-1
            elif target>matrix[m][-1]:
                top=m+1
            else:
                break
        
        left,right=0,len(matrix[0])-1
        while left<=right:
            mid=left+(right-left)//2
            if target<matrix[m][mid]:
                right=mid-1
            elif target>matrix[m][mid]:
                left=mid+1
            else:
                return True
        return False
