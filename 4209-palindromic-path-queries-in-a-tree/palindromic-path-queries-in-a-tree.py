class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in g[u]:
                if parent[v] == -1:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        for u in reversed(order[1:]):
            p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 or size[u] > size[heavy[p]]:
                heavy[p] = u

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in g[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        chars = list(s)
        arr = [0] * n
        for u in range(n):
            arr[pos[u]] = 1 << (ord(chars[u]) - 97)

        seg = [0] * (4 * n)

        def build(i, l, r):
            if l == r:
                seg[i] = arr[l]
                return
            m = (l + r) // 2
            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(i, l, r, p, val):
            if l == r:
                seg[i] = val
                return
            m = (l + r) // 2
            if p <= m:
                update(i * 2, l, m, p, val)
            else:
                update(i * 2 + 1, m + 1, r, p, val)
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def query(i, l, r, ql, qr):
            if ql <= l and r <= qr:
                return seg[i]
            m = (l + r) // 2
            res = 0
            if ql <= m:
                res ^= query(i * 2, l, m, ql, qr)
            if qr > m:
                res ^= query(i * 2 + 1, m + 1, r, ql, qr)
            return res

        def path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query(1, 0, n - 1, pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            res ^= query(1, 0, n - 1, pos[u], pos[v])
            return res

        build(1, 0, n - 1)
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
                update(
                    1, 0, n - 1, pos[u],
                    1 << (ord(c) - 97)
                )
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans