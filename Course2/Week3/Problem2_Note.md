## Strategy

Use priority heap to chose the thread which is available most soon. In the heap, each element is like [thread number, available time]. The element is ranked in the heap by available time, if the available time is the same then they are ranked by thread number.

Several key points should be mentioned: 

1. min-heap should be used.

2. when extracting available thread, you should insert the same thread with its next available time to the heap. Look at the following function.

   

**Extract Min**

```Python 3
def ExtractMin(self, list_input, time_cost):
    result = list_input[0]
    new_result = [result[0], result[1]+time_cost]
    self.heap[0] = new_result
    self.ShiftDown(0)
    return result
```



## Code:

```python 3
# python3

import math

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def Parent(self, i):
        return int(math.floor((i-1)/2))

    def LeftChild(self, i):
        return 2*(i)+1

    def RightChild(self, i):
        return 2*(i)+2

    def ShiftDown(self, i):
        maxindex = i
        L = self.LeftChild(i)
        if L <= (self.num_workers-1):
            if self.heap[L][1] < self.heap[maxindex][1] or (self.heap[L][1] == self.heap[maxindex][1] and self.heap[L][0] < self.heap[maxindex][0]):
                maxindex = L

        R = self.RightChild(i)
        if R <= (self.num_workers-1):
            if self.heap[R][1] < self.heap[maxindex][1] or (self.heap[R][1] == self.heap[maxindex][1] and self.heap[R][0] < self.heap[maxindex][0]):
                maxindex = R

        if i != maxindex:
            j = maxindex
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            self.ShiftDown(j)

    def BuildHeap(self, list_input):
        for k in range(int(math.floor((self.num_workers - 1)/2)), -1, -1):
            self.ShiftDown(k)

    def ExtractMin(self, list_input, time_cost):
        result = list_input[0]
        new_result = [result[0], result[1]+time_cost]
        self.heap[0] = new_result
        self.ShiftDown(0)
        return result

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        # generate initial heap
        self.heap = []
        for i in range(self.num_workers):
            self.heap.append([i, 0])
        self.BuildHeap(self.heap)

        # arrage jobs
        for i in range(len(self.jobs)):
            worker = self.ExtractMin(self.heap, self.jobs[i])
            self.assigned_workers[i] = worker[0]
            self.start_times[i] = worker[1]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
```

