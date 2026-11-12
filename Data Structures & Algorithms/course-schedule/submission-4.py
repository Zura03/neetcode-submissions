class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)

        visit = set()
        def dfs(x):
            nonlocal visit
            if x in visit:
                return False
            if prereq[x] == []:
                return True
            
            visit.add(x)
            for course in prereq[x]:
                if not dfs(course):
                    return False
            visit.remove(x)
            prereq[x] = []
            return True

        for x in range(numCourses):
            if not dfs(x):
                return False
            
        return True
        