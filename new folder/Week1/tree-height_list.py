# python3

import sys
import threading
import copy


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        # sys.stdin.readline() is to get input data; self.n means the length of input nodes, for example 5.
        self.n = int(sys.stdin.readline())
        # the whole line is to get the input list, for example, 4 -1 4 1 1
        self.parent = list(map(int, sys.stdin.readline().split()))

    def make_tree(self):
        # make a tree structure, represented by list

        nodes = copy.deepcopy(self.parent)
        for i in range(self.n):
            # find the root
            if self.parent[i] == -1:
                root = i

            # this is one node
            tempNode = [self.parent[i], []]

            nodes[i] = tempNode

        nodes_1 = copy.deepcopy(nodes)  # copy nodes for further operations

        for i in range(self.n):
            if nodes[i][0] != -1:
                nodes_1[nodes[i][0]][1].append(i)

        self.Root = root    # position of root node
        self.Nodes = nodes_1  # the list representing the tree

    def compute_height(self, rootNode):
        if len(rootNode[1]) == 0:
            return 1
        else:
            height = []
            for i in range(len(rootNode[1])):
                height.append(self.compute_height(self.Nodes[rootNode[1][i]]))
            return 1+max(height)


def main():
    Tree = TreeHeight()
    Tree.read()
    Tree.make_tree()
    print(Tree.compute_height(Tree.Nodes[Tree.Root]))


threading.Thread(target=main).start()
