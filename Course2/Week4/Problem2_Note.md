## Key points

1. Create an array with size m to store the mapping, where m is the cardinality of the hash function. Each element is a list, which represents the chain of keys which share the same hash value

```Python 3
self.elems = [[] for i in range(0, bucket_count)]
```



## Code:

```python 3
# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            # if type is not 'check', self.s is 'name' to be added, deleted, or found
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count

        # store all strings in one list. Create an array with size m, where m is the cardinality of the hash function.
        self.elems = [[] for i in range(0, bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        if query.type == "check":

            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems[query.ind]))
        else:
            h_value = self._hash_func(query.s)

            try:  # Check if elems already have query.s

                temp_cell = self.elems[h_value]
                ind = temp_cell.index(query.s)

            except ValueError:

                ind = -1  # if query.s does not exist in elems, set ind to -1

            if query.type == 'find':
                self.write_search_result(ind != -1)

            elif query.type == 'add':
                if ind == -1:
                    self.elems[h_value].append(query.s)
            else:
                if ind != -1:
                    self.elems[h_value].pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

```

