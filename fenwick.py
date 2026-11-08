"""Fenwick tree (binary indexed tree): point update and prefix sum in O(log n), plus range sums,
range update with point query, and finding the first prefix that reaches a target."""


class Fenwick:
    def __init__(self, n_or_values):
        if isinstance(n_or_values, int):
            self.n = n_or_values
            self.t = [0] * (self.n + 1)
        else:
            vals = list(n_or_values)
            self.n = len(vals)
            self.t = [0] + vals
            for i in range(1, self.n + 1):      # O(n) build: push each node into its parent
                j = i + (i & -i)
                if j <= self.n:
                    self.t[j] += self.t[i]

    def add(self, i, delta):
        """a[i] += delta, for 0-based i."""
        i += 1
        while i <= self.n:
            self.t[i] += delta
            i += i & -i

    def prefix(self, i):
        """a[0] + ... + a[i - 1]."""
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def range_sum(self, lo, hi):
        """a[lo] + ... + a[hi - 1]."""
        return self.prefix(hi) - self.prefix(lo)

    def lower_bound(self, target):
        """Smallest k with prefix(k) >= target, assuming every a[i] >= 0; n + 1 if there is none."""
        pos, rem = 0, target
        step = 1 << self.n.bit_length()
        while step:
            nxt = pos + step
            if nxt <= self.n and self.t[nxt] < rem:
                pos = nxt
                rem -= self.t[nxt]
            step >>= 1
        return pos + 1


class RangeAddPointQuery:
    """Add a value to every a[lo..hi-1] in O(log n) and read a single a[i] in O(log n)."""

    def __init__(self, n):
        self.f = Fenwick(n + 1)

    def add(self, lo, hi, delta):
        self.f.add(lo, delta)
        self.f.add(hi, -delta)

    def get(self, i):
        return self.f.prefix(i + 1)
