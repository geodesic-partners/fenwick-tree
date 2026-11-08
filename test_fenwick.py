import random
import unittest

from fenwick import Fenwick, RangeAddPointQuery


class TestFenwick(unittest.TestCase):
    def test_random_operations_against_a_list(self):
        rng = random.Random(5)
        for n in (1, 2, 7, 64, 100):
            a = [rng.randint(-50, 50) for _ in range(n)]
            f = Fenwick(a)
            for _ in range(2000):
                if rng.random() < 0.5:
                    i, d = rng.randrange(n), rng.randint(-20, 20)
                    a[i] += d
                    f.add(i, d)
                else:
                    lo = rng.randrange(n + 1)
                    hi = rng.randrange(lo, n + 1)
                    self.assertEqual(f.range_sum(lo, hi), sum(a[lo:hi]))

    def test_linear_build_matches_repeated_adds(self):
        vals = list(range(1, 38))
        f1, f2 = Fenwick(vals), Fenwick(len(vals))
        for i, v in enumerate(vals):
            f2.add(i, v)
        self.assertEqual(f1.t, f2.t)

    def test_lower_bound(self):
        rng = random.Random(6)
        a = [rng.randint(0, 9) for _ in range(50)]
        f = Fenwick(a)
        total = sum(a)
        for target in range(1, total + 2):
            want = next((k for k in range(1, 51) if sum(a[:k]) >= target), 51)
            self.assertEqual(f.lower_bound(target), want, target)

    def test_range_add_point_query(self):
        rng = random.Random(7)
        n = 40
        a = [0] * n
        r = RangeAddPointQuery(n)
        for _ in range(1000):
            lo = rng.randrange(n)
            hi = rng.randrange(lo, n) + 1
            d = rng.randint(-5, 5)
            r.add(lo, hi, d)
            for i in range(lo, hi):
                a[i] += d
            i = rng.randrange(n)
            self.assertEqual(r.get(i), a[i])


if __name__ == "__main__":
    unittest.main()
