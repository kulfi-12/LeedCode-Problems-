class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge
            g[a].append(b)
            g[b].append(a)

        v = [False]*n
        q = deque([source])
        while q:
            x = q.popleft()
            v[x] = True
            if x == destination:
                return True
            for neigh in g[x]:
                if not v[neigh]:
                    q.append(neigh)
        return False
