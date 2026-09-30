class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        while up <= down:
            row = (up + down) // 2

            if target < matrix[row][0]:
                down = row - 1
            elif target > matrix[row][-1]:
                up = row + 1
            else:
                break
    
        if not up <= down:
            return False
        L, R = 0, len(matrix[0])
        while L <= R:
            mid = (L + R) // 2

            if target < matrix[row][mid]:
                R = mid - 1
            elif target > matrix[row][mid]:
                L = mid + 1
            else:
                return True

        return False