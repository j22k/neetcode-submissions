from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # Store negative counts to simulate a max-heap
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # Stores pairs of [-cnt, idle_until_time]

        while max_heap or q:
            time += 1
            if max_heap:
                # Add 1 since counts are negative (e.g., -3 + 1 = -2)
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            
            # Must be outside `if max_heap` to handle idle CPU cycles
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
