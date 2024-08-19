# HashMap: a hashmap(also know as a hash table) is a data structure that stores key-value pairs.
# It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

# Operations:
    # Insert(Put): Adds a key-value pair to the hashmap
    # Search(Get): Retrieves the value associated with a given key
    # Delete(Remove): Removes the key-value pair associated with a given key
    # ContainsKey: Checks if a given key exists in the hashmap
    # Size: Returns the number of key-value pairs in the hashmap

# Implementation:
    # Array-based implementation: Uses an array where each slot contains a linked list or another array to handle collisions(chaining or open addressing)
    # Hash Function: Converts a key into an array index
    # Collision Resolution: Handles cases where multiple keys hash to the same index. Common techniques include chaining(using linked lists) and open addressing(probing)

# Applications:
    # Caching: Hashmaps are used in caches to store and retrieve data quickly
    # Database Indexing: Used to index data for fast retrieval in databases
    # Counting Frequency: Used to count the frequency of elements in a collection

# Complexity Analysis:
    # Insert(Put): O(1) average, O(n) worst case(due to collisions)
    # Search(Get): O(1) average, O(n) worst case(due to collisions)
    # Delete(Remove): O(1) average, O(n) worst case(due to collisions)
    # ContainsKey: O(1) average, O(n) worst case(due to collisions)
    # Size: O(1)

# Implementation of a simple HashMap:
class HashMap:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return -1
    
    def remove(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
# Example Usage
hash_map = HashMap()
hash_map.put(1, 1)
hash_map.put(2, 2)
print(hash_map.get(1))  # Output: 1
print(hash_map.get(3))  # Output: -1 (not found)
hash_map.put(2, 1)  # Update the existing value
print(hash_map.get(2))  # Output: 1
hash_map.remove(2)  # Remove the mapping for 2
print(hash_map.get(2))  # Output: -1 (not found)
            

# PRACTICE PROBLEMS:

# TWO SUM:
    # Given an array of integers, return indices of the two numbers such that they add up to a specific target

def twoSum(nums, target):
    prevMap = {}

    for i, num in enumerate(nums):
        match = target - num
        if match in prevMap:
            return [prevMap[match], i]
        else:
            prevMap[num] = i
    return
        

# GROUP ANAGRAMS:
    # Given an array of strings, group anagrams together
from collections import defaultdict # defaultdict provides defauly value for a nonexistent key

def group_Anagrams(strs):
    hashmap = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        hashmap[key].append(s)
    return list(hashmap.values())

# Example Usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_Anagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
