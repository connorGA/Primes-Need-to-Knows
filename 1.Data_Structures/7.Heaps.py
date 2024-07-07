# Heaps:
    # A heap is a special tree-based data structure that satisfies the heap property.
    # In a max heap, for any given node, the value of the node is greater than or equal to the values of its children.
    # In a min heap, the value of the node is less than or equal to the values of its children

# Operations:
    # Insert: Adds a new element ot the heap while maintaining the heap property
    # Delete: Removes the root element(maximum for the max heap, minimum for the min heap) and reheapifies
    # Peek: Returns the root element without removing it
    # Heapify: Converts an arbitrary array into a heap
    # Extract: Removes and returns the root element

# Types of Heaps:
    # Max Heap: The key at the root must be the largest among all keys present in the binary heap
    # Min Heap: The key at the root must be the smallest among all keys present in the binary heap

# Applications:
    # Priority Queues: Heaps are used to implement priority queues
    # Heap Sort: An efficient sorting algorithm based on heap data structure
    # Graph Algorithms: Used in algorithms like Dijkstra's shortest path and Prim's minimum spanning tree

# Complex Analysis:
    # Insert: O(log n)
    # Delete: O(log n)
    # Peek: O(1)
    # Heapify: O(n)

# Example of Max Heap Implementation:
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self,val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_val = self.heap.pop()
            self._heapify_dwon(0)
        elif self.heap:
            max_val = self.heap.pop()
        else:
            max_val = None
        return max_val
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def _heapify_up(self, index):
        parent_index = (index -1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Example Usage
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(30)
print(heap.peek())  # Output: 30
print(heap.delete())  # Output: 30
print(heap.peek())  # Output: 20

# PRACTICE PROBLEMS
# Kth Largest Elements in an Array:
    # Find the kth largest element in an unsorted array
import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5    


# Merge K Sorted Lists:
    # Merge k sorted linked lists and return it as one sorted list

from heapq import heappop, heappush, heapify

class ListNode:
    def __init__(self):
        self.val = val 
        self.next = next
    
    def mergeKLists(lists):
        min_heap = []
        for idx, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, idx, l))

        dummy = ListNode()
        current = dummy


        while min_heap:
            val, idx, node = heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next
    
# Example Usage
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Create sample lists
a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

lists = [a, b, c]

# Merge lists and print the result
merged_list = mergeKLists(lists)
print_list(merged_list)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None
