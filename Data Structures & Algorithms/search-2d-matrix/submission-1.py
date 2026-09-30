class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        up, down = 0, ROWS - 1

        while up <= down:
            mid = (up + down) // 2
            if target > matrix[mid][-1]:
                up = mid + 1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                break

        # if not up <= down:
        #     return False
        
        L, R = 0, COLS - 1
        while L <= R:
            m = (L + R) // 2
            if matrix[mid][m] > target:
                R = m - 1
            elif matrix[mid][m] < target:
                L = m + 1
            else:
                return True
        return False