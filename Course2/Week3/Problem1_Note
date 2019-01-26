## Strategy

Combine the following functions, they are just modified a little bit from the functions given in the lecture mainly because that 

1. list starts from 0 in python.
2. the min heap should be used in this case. 



**Build Heap**

```Python 3
def BuildHeap(A[0...n-1]):
    size = n
    for i from math.floor((n-1)/2) downto 0:
        ShiftDown(i)
```



**Shift Down**

```python 3
def ShiftDown(i):
    maxindex = i
    L = LeftChild(i)
    if L <= (size-1) and A[L] < A[maxindex]:
    	maxindex = L
    R = RightChild(i)
    if R <= (size-1) and A[R] < A[maxindex]:
    maxindex = R
    
    if i != maxindex:
		swap A[i] and A[maxindex]
        ShiftDown(maxindex)
```



**Parent**

```python 3
def Parent[i]:
	return math.floor((i-1)/2)
```



**Right Child**

```python 3
def RightChild(i):
	return 2*i+1	
```



**Left Child**

```python 3
def LeftChild(i):
	return 2*i+2
```



### Code

```python 3
# python3
import math


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self.num = 0

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)
        self.num = n

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def Parent(self, i):
        return int(math.floor((i-1)/2))

    def LeftChild(self, i):
        return 2*(i)+1

    def RightChild(self, i):
        return 2*(i)+2

    def ShiftDown(self, i):
        maxindex = i
        L = self.LeftChild(i)
        if L <= (self.num-1) and self._data[L] < self._data[maxindex]:
            maxindex = L

        R = self.RightChild(i)
        if R <= (self.num-1) and self._data[R] < self._data[maxindex]:
            maxindex = R

        if i != maxindex:
            j = maxindex
            self._swaps.append((i, j))
            self._data[i], self._data[j] = self._data[j], self._data[i]
            self.ShiftDown(j)

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for k in range(int(math.floor((self.num-1)/2)), -1, -1):
            self.ShiftDown(k)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
```

