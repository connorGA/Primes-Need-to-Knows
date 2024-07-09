# Priority Queues:
    # A priority queue is an abstract data type similar to a regular queue or a stack data structure, but where each element has a "priority" associated with it.
    # In a priority queue, an element with high priority is served before an element with low priority

# Operations:
    # Insert(Push/Enqueue): Adds an element to the priority queue with a given priority
    # Extract-Min(Pop/Dequeue): Removes and returns the element with the highest priority(usually the smallest value)
    # Peek(Top/Front): Returns the element with the highest priority without removing it
    # Change Priority: Changes the priority of a given element

# Applications:
    # Scheduling: Used in operating systems for scheduling processes
    # Graph Algorithms: Used in algorithms like Dijkstra's shortest path and Prim's minimum spanning tree
    # Event Simulation: Used to manage events in a simulation

# Complex Analysis:
    # Insert: O(log n)
    # Extrac-Min: O(log n)
    # Peek: O(1)
    # Change Priority: O(log n)

# Implementation:
    # Priority queues are often implemented using heaps, which are binary trees that satisfy the heap property:
            # Min-Heap: The parent node is always less than or equal to the child nodes
            # Max-Heap: The parent node is always great than or equal to the child nodes

# Example of Priority Queue Implementation in Python Using 'heapq'
    # Min-Heap Implementation
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def change_priority(self, old_item, new_item):
        idx = self.heap.index(old_item)
        self.heap[idx] = new_item
        heapq.heapify(self.heap) #Re-heapify after changing priority

# Example Usage
pq = PriorityQueue()
pq.push(3)
pq.push(1)
pq.push(2)

print(pq.peek())  # Output: 1 (smallest element)
print(pq.pop())   # Output: 1 (removes and returns the smallest element)
print(pq.pop())   # Output: 2
pq.push(4)
print(pq.peek())  # Output: 3


# PRACTICE PROBLEMS:
# Kth Largest Element in a Stream
    # Design a class to find the k-th largest element in a stream

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
# Example Usage
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8

# Merge k Sorted Lists:
    # Merge k sorted linked lists and return it as one sorted list

from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    for l in lists:
        if l:
            heappush(min_heap, (l.val, l))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, node = heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if node.next:
            heappush(min_heap, (node.next.val, node.next))

    return dummy.next

# Example Usage
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

lists = [a, b, c]
merged_list = mergeKLists(lists)
print_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None