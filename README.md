# Fenwick tree (binary indexed tree) in Python, tested against a plain list

A Fenwick tree keeps running totals of an array so that you can change one element and ask for any prefix sum, each in O(log n) time, with just an array of n + 1 numbers. It's a common follow-up in coding interviews once you've shown the prefix-sum trick and the interviewer adds "now the array changes". I find it's also the structure people most often half-remember, because the whole thing rests on one line, `i & -i`, the lowest set bit of i.

```python
from fenwick import Fenwick, RangeAddPointQuery

f = Fenwick([3, 1, 4, 1, 5, 9, 2, 6])
f.range_sum(2, 5)     # 4 + 1 + 5 = 10
f.add(3, 10)          # a[3] becomes 11
f.prefix(4)           # 3 + 1 + 4 + 11 = 19
f.lower_bound(8)      # 3, the first prefix length whose sum reaches 8
```

Node i covers the stretch of the array that ends at i and is as long as its lowest set bit, so an update walks up by adding that bit and a query walks down by taking it away. You can build the tree in O(n), not O(n log n), by pushing each node into its parent once. `lower_bound` finds the first prefix whose sum reaches a target by walking down the powers of two, which is handy for sampling by weight or for finding the k-th element of a multiset. `RangeAddPointQuery` turns the idea around, storing differences so that adding to a whole range is two updates and reading one element is a prefix sum.

## Tests

`python3 -m unittest test_fenwick` runs 2,000 random updates and range sums against a plain Python list for arrays of 1, 2, 7, 64 and 100 elements. It checks that the O(n) build gives the same tree as adding the values one at a time, that `lower_bound` agrees with a linear scan for every target, and that range adds with point reads match a list over 1,000 random operations. You'll only need the Python standard library.

## More practice

Coding interview problems with worked solutions in six languages, including prefix sums: https://geodesicpartners.co.uk/coding-interview-course

MIT licence.
