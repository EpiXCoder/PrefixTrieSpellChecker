# Path to the macOS system dictionary
# dictionary_path = '/usr/share/dict/words'
import os

current_directory = os.path.dirname(__file__)
dictionary_path = os.path.join(current_directory, 'words')

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
    
    def remove(self, word):
        self._remove(self.root, word, 0)

    def _remove(self, node, word, index):
        if index == len(word):
            if not node.is_end_of_word:
                return False 
            node.is_end_of_word = False
            return len(node.children) == 0 

        char = word[index]
        child_node = node.children.get(char)
        if not child_node:
            return False 

        should_delete_child = self._remove(child_node, word, index + 1)

        if should_delete_child:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word

        return False

def load_system_dictionary(trie, dictionary_path):
    with open(dictionary_path, 'r') as file:
        for word in file:
            trie.insert(word.strip().lower())


def is_word_spelled_correctly(trie, word):
    return trie.search(word.lower())


def suggest_corrections(trie, word, max_suggestions=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    suggestions = set()

    def edits(word, depth):
        if depth == 0:
            return {word}
        elif depth == 1:
            splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
            deletes = [L + R[1:] for L, R in splits if R]
            replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
            inserts = [L + c + R for L, R in splits for c in letters]
            return set(deletes + replaces + inserts)
        else:
            return set(e2 for e1 in edits(word, depth - 1) for e2 in edits(e1, 1))

    suggestions.update(edits(word, 1))
    suggestions.update(edits(word, 2))

    filtered_suggestions = [w.lower() for w in suggestions if trie.search(w.lower())]

    # Sorts suggestions by Levenshtein distance
    filtered_suggestions.sort(key=lambda x: levenshtein_distance(word, x))

    # Limits the number of suggestions
    return filtered_suggestions[:max_suggestions]

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def spell_checker_interface():
    word = input("Enter a word to check: ")
    if is_word_spelled_correctly(trie, word):
        print(f"'{word}' is spelled correctly.")
    else:
        print(f"'{word}' might be misspelled.")
        corrections = suggest_corrections(trie, word)
        if corrections:
            print("Did you mean:", ", ".join(corrections))
        else:
            print("No suggestions available.")

# Initialize Trie and load dictionary
trie = Trie()
load_system_dictionary(trie, dictionary_path)
# spell_checker_interface()