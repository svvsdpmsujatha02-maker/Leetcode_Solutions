import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        # Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][count] = minimum cost
        # count = consecutive occurrences of current label
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Starting node has consecutive count 1
        dist[0][1] = 0

        # Min heap: (cost, node, count)
        pq = [(0, 0, 1)]

        while pq:
            cost, u, count = heapq.heappop(pq)

            # Skip outdated states
            if cost > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            for v, w in graph[u]:

                # Same character: increase count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    # Different character: reset count
                    new_count = 1

                # Check consecutive character condition
                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    dist[v][new_count] = new_cost

                    heapq.heappush(
                        pq, (new_cost, v, new_count)
                    )

        return -1
