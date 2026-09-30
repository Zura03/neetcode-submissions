class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(L, R):
            pivot, p = nums[R], L
            for i in range(L, R):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[R] = nums[R], nums[p]
            
            if p > k:
                return quickSelect(L, p - 1)
            elif p < k:
                return quickSelect(p + 1, R)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)