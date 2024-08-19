# Array : a collection of elements, each identified by an array index or key. Arrays are a fundamental data structure used to store a collection of elements(values or variables), tpyically of the same data type.

# Properties:
    # Fixed Size: Once an array is created, its size cannot be changed
    # Indexing: Elements in an array can be accessed using their index, with the first element having an index of 0
    # Contiguous Memory Allocation: Arrays are stored in contiguous memory locations

# Operations:
    # Access: 'array[index]'
    # Update: 'array[index] = value'
    # Traversal: Loop through the array using a for loop(for,while)
    # Insertion: Adding an element at a specific position(may require shifting elements)
    # Deletion: Removing an element from a specific position(may require shifting elements)

# Time Complexity:
    # Access: O(1)
    # Update: O(1)
    # Traversal: O(n)
    # Insertion (at end): O(1)(if no resizing needed), O(n)(if resizing needed)
    # Deletion: O(n) (due to shifting)


# Creating an array
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1

# Updating an element
arr[1] = 20
print(arr) 

# Traversing the array
for element in arr:
    print(element) # Output: prints every element in arr

# Inserting an element
arr.insert(2, 10)
print(arr) # Output: [1, 20, 10, 3, 4, 5]   inserts new element into 2 index

# Deleting an element
arr.pop(3)
print(arr) # Output: [1, 20, 10, 4, 5] deleted element at index 3


# Practice Problems

# 1. Reverse an Array:
def reverse_array(arr):
    return arr[::-1]            # 'arr[start:stop:step]' is the general form of slicing in python. start is the index to start slice and stop is the index to stop slice. Step is the step size or stride. Since start and stop arent specified in the slice, these values default to beginning and end of array. Step -1 means the slice will be taken from the end towards the beginning, effectively reversing the array

print(reverse_array(arr))

# 2. Find the maximum and minimum element:
def find_max_min(arr):
    arr_max = max(arr)
    arr_min = min(arr)

    return arr_max, arr_min

print(find_max_min(arr))

# 3. Rotate Array:
#  Write a function that rotate an array to the right by 'k' steps
def rotate_array(arr, k):
    k = k % len(arr) #handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))
