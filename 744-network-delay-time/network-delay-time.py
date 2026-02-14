import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue

            for nei, w in graph[node]:
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(pq, (dist[nei], nei))

        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1