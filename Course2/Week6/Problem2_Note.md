## Key points

1. use the inOrder method from the first problem.  It returns a list, let's say, A, which have all the key sorted with "inOrder" method.
2. To ensure the condition of binary search tree, elements in list A should sorted in ascending order.

## Code:

```python 3
#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:

    def __init__(self, L_key, L_left, L_right):
        self.key = L_key
        self.left = L_left
        self.right = L_right
        self.result = []

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

    def IsBinarySearchTree(self):
        # Implement correct algorithm her
        flag = True
        if len(self.key) == 0:
            return True

        self.inOrder(0)
        last = self.result[0]
        for i in range(1, len(self.result)):
            now = self.result[i]
            if now <= last:
                flag = False
            last = self.result[i]

        return flag


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []

    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    L_key = []
    L_left = []
    L_right = []

    for element in tree:
        L_key.append(element[0])
        L_left.append(element[1])
        L_right.append(element[2])

    TheTree = TreeOrders(L_key, L_left, L_right)

    if TheTree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
```

