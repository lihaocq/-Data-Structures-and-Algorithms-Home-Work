# python3

import sys
import threading
import copy
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:  # class name
    def __init__(self, key, parent, children):
        self.k = key
        self.p = parent
        self.c = children

    def addChidren(self, ChildrenToAdd):
        if ChildrenToAdd in self.c:
            pass
        else:
            self.c.append(int(ChildrenToAdd))


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())

        self.parent = list(map(int, sys.stdin.readline().split()))

    def make_tree(self):
        # make a tree structure
        nodes = copy.deepcopy(self.parent)  # nodes get the # of all nodes

        for i in range(self.n):
            # find the root
            if self.parent[i] == -1:
                root = i

            tempNode = Node(i, self.parent[i], [])

            nodes[i] = tempNode

        nodes_1 = copy.deepcopy(nodes)

        for i in range(self.n):
            if nodes[i].p != -1:
                nodes_1[nodes[i].p].addChidren(i)

        self.Root = root
        self.Nodes = nodes_1

    def compute_height(self, rootNode):
        if len(rootNode.c) == 0:
            return 1
        else:
            height = []
            for i in range(len(rootNode.c)):
                height.append(self.compute_height(self.Nodes[rootNode.c[i]]))
            return 1+max(height)


def main():
    Tree = TreeHeight()
    Tree.read()
    Tree.make_tree()
    print(Tree.compute_height(Tree.Nodes[Tree.Root]))


threading.Thread(target=main).start()
