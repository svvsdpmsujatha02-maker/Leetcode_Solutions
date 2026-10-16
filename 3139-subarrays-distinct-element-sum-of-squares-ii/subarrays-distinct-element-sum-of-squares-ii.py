class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left > end or right < start:
                return

            if left <= start and end <= right:
                length = end - start + 1
                d = 1

                sq[node] = (
                    sq[node] + 2 * tree[node] + length
                ) % MOD

                tree[node] = (tree[node] + length) % MOD
                lazy[node] += d
                return

            mid = (start + end) // 2

            push(node, start, end)

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = (
                tree[node * 2] + tree[node * 2 + 1]
            ) % MOD

            sq[node] = (
                sq[node * 2] + sq[node * 2 + 1]
            ) % MOD

        def push(node, start, end):
            d = lazy[node]

            if d == 0 or start == end:
                return

            mid = (start + end) // 2

            for child, length in (
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid)
            ):
                sq[child] = (
                    sq[child] + 2 * d * tree[child]
                    + d * d * length
                ) % MOD

                tree[child] = (
                    tree[child] + d * length
                ) % MOD

                lazy[child] += d

            lazy[node] = 0

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans