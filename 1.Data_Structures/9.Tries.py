# Tries:
    # A trie, also known as a prefix tree, is a tree data structure used to store a dynamic set or associative array where the keys are usually strings

# Operations:
    # Insert: Adds a word to the trie
    # Search: Checks if a word is in the trie
    # StartsWith: Checks if there is any word in the trie that starts with a given prefix
    # Delete: Removes a word from the trie

# Applications:
    # Autocomplete: Used to suggest completions for a given prefix
    # Spell Checker: Used to check if a word is spelled correctly
    # IP Routing: Used in IP routing for longest prefix matching
    # DNA Sequencing: Used to store and query DNA sequences

# Complex Analysis:
    # Insert: O(m) where m is the length of the word
    # Search: O(m) where m is the length of the word
    # StartsWith: O(m) where m is the length of the prefix
    # Delete: O(m) where m is the length of the word

# Example of Trie Implementation:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char in node.children:
                should_delete_child = _delete(node.children[char], word, depth + 1)
                if should_delete_child:
                    del node.children[char]
                    return len(node.children) == 0
            return False
        _delete(self.root, word, 0)

# Example Usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: False
print(trie.starts_with("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))    # Output: True
trie.delete("apple")
print(trie.search("apple"))  # Output: False

# PRACTICE PROBLEMS:
# Implement a trie with insert, searchm and startsWith methods

class Trie:
        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def search(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end_of_word
        
        def starts_with(self, prefix):
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return True
# Example Usage
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: False
print(trie.starts_with("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))    # Output: True

# Replace Words
    # In a dictionary, find the root of a word and replace it if the root exists in the dictionary

def replaceWords(dictionary, sentence):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    def replace(word):
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end_of_word:
                return word[:i+1]
        return word
    return ' '.join(map(replace, sentence.split()))

# Example Usage
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(dictionary, sentence))  # Output: "the cat was rat by the bat"

