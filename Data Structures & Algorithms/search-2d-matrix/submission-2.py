class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1

        while top<=bottom:
            m=top+(bottom-top)//2
            if matrix[m][0]>target:
                bottom=m-1
            elif matrix[m][-1]<target:
                top=m+1
            else:
                break
        if top>bottom:
            return False
        while left<=right:
            mid=left+(right-left)//2
            if matrix[m][mid]<target:
                left=mid+1
            elif matrix[m][mid]>target:
                right=mid-1
            else:
                return True
        return False