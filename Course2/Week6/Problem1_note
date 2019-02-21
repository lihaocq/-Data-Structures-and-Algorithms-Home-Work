## Key points

1. for recursion, "using a public variable to get data" is faster than "using local variable and **return** local variable. In my code, I used the first method, it takes 1.3 s to run the hardest test. The second method takes 12 s for that test.

## Code:

```python 3
# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

        self.result = []
        self.result0 = []
        self.result1 = []

    def inOrder(self, key_index):

        if self.left[key_index] == -1 and self.right[key_index] == -1:
            self.result.append(self.key[key_index])
            return

        if self.left[key_index] != -1:
            self.inOrder(self.left[key_index])

        ToAddKey = self.key[key_index]
        if ToAddKey is not None:
            self.result.append(ToAddKey)

        if self.right[key_index] != -1:
            self.inOrder(self.right[key_index])

    def preOrder(self, key_index):

        if self.left[key_index] == -1 and self.right[key_index] == -1:
            self.result0.append(self.key[key_index])
            return

        ToAddKey = self.key[key_index]
        if ToAddKey is not None:
            self.result0.append(ToAddKey)

        if self.left[key_index] != -1:
            self.preOrder(self.left[key_index])

        if self.right[key_index] != -1:
            self.preOrder(self.right[key_index])

    def postOrder(self, key_index):

        if self.left[key_index] == -1 and self.right[key_index] == -1:
            self.result1.append(self.key[key_index])
            return

        if self.left[key_index] != -1:
            self.postOrder(self.left[key_index])

        if self.right[key_index] != -1:
            self.postOrder(self.right[key_index])

        ToAddKey = self.key[key_index]
        if ToAddKey is not None:
            self.result1.append(ToAddKey)


def main():
    tree = TreeOrders()
    tree.read()

    tree.inOrder(0)
    print(*tree.result)
    tree.preOrder(0)
    print(*tree.result0)
    tree.postOrder(0)
    print(*tree.result1)


threading.Thread(target=main).start()

```

