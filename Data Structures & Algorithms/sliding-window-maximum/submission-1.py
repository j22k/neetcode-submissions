class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # l, r = 0, k - 1

        # while r < len(nums):
        #     Max = max(nums[l:r + 1])
        #     res.append(Max)

        #     l += 1
        #     r = l + k - 1

        # return res

        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


