class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.timeMap[key]:
            res = ""
            L, R = 0, len(self.timeMap[key]) - 1
            while L <= R:
                mid = (L + R) // 2
                if self.timeMap[key][mid][1] <= timestamp:
                    res = self.timeMap[key][mid][0]
                    L = mid + 1
                else:
                    R = mid - 1
            return str(res)
        else:
            return ""
