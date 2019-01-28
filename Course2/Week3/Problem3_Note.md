## Key points

1. To apply Path compression, the only thing need to modify is just ‘Find’ Function. The find function is like the following.

```Python 3
def Find(i):
    if i != parent[i]:
        parent[i]=Find(parent[i])
    return parent[i]
```



2. To apply **Union by Rank**, you need to change the MakeSet() and Union() functions.
3. When merging two elements, this problem required a merging direction, that is from target to destination. However, the merging direction of Union by Rank is from shallow tree to deep tree. However, this does not affect the max value of elements, as long as you do not set the target element value to 0.

## Code:

```python 3
# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def getParent(table):
    # find parent with compress path method
    global parent

    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    global lines, ans, rank, parent
    dest_id, sour_id = getParent(destination), getParent(source)

    if dest_id == sour_id:
        return False

    # we do not differentiate between target element value and destination element value, because we are use union by rank, in some cases it is against
    # the desired merging direction of this problem. If we differentiate target value and destination value, this issue will cause problem.
    lines[dest_id] += lines[sour_id]
    lines[sour_id] = lines[dest_id]

    if rank[dest_id] > rank[sour_id]:
        parent[sour_id] = dest_id
    else:
        parent[dest_id] = sour_id
        if rank[dest_id] == rank[sour_id]:
            rank[sour_id] = rank[sour_id] + 1

    if lines[dest_id] > ans:
        ans = lines[dest_id]

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

```

