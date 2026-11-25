class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones

        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop_max(max_heap)
            second = heapq.heappop_max(max_heap)

            if first != second:
                heapq.heappush_max(max_heap, first - second)
        if max_heap:
            return heapq.heappop_max(max_heap)
        else:
            return 0