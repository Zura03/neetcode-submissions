class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store=set(numbers)
        res=[0]*2
        number=0
        for i in range(len(numbers)):
            if (target-numbers[i]) in store:
                res[0]=i+1
                number=numbers[i]
                break
        for i in range(res[0],len(numbers)):
            if (target-number)==numbers[i]:
                res[1]=i+1
        return res