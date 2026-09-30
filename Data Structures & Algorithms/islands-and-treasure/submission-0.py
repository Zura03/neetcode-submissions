from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        # Initialize the queue with all zero cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                # Update the distance for the current cell
                #if grid[row][col] == 2147483647:
                grid[row][col] = dist

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r not in range(rows) or c not in range(cols)
                        or grid[r][c] == -1 or (r, c) in visit):
                        continue
                    
                    q.append((r, c))
                    visit.add((r, c))
            dist += 1
