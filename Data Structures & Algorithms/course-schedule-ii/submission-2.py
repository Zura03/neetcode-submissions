class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        res = []
        visit, cycle = set(), set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            # if preMap[crs] == []:
            #     res.append(crs)
            #     return True
            
            cycle.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)   
            return True           

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res