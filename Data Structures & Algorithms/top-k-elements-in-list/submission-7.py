class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            res[cnt].append(num)

        ans = []
        for i in range(len(res) - 1, 0, -1):
            for num in res[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans