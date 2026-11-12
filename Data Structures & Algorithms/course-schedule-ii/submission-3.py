class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        res = []
        
        cycle, visit = set(), set()

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True

            cycle.add(i)
            for n in preMap[i]:
                if not dfs(n):
                    return False
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
