class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k - 1

        while r < len(nums):   # <-- Fix is here
            Max = max(nums[l:r + 1])
            res.append(Max)

            l += 1
            r = l + k - 1

        return res