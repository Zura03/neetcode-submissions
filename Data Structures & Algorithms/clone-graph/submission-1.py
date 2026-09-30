"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # oldToNew = {}

        # def dfs(node):
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     newNode = Node(node.val)
        #     oldToNew[node] = newNode
        #     for neighbor in node.neighbors:
        #         newNode.neighbors.append(dfs(neighbor))

        #     return newNode

        # return dfs(node) if node else None
        
        if not node:
            return None
        
        oldToNew = {}
        oldToNew[node] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in oldToNew:
                    q.append(neighbor)
                    oldToNew[neighbor] = Node(neighbor.val)
                oldToNew[cur].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]