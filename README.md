# Spell Checker Application

This spell checker application utilizes a Trie data structure to efficiently check the spelling of words and provide suggestions for corrections. It's written in Python and offers a simple interface for spell checking.

## Trie Data Structure

The application uses a Trie, a tree-like data structure that stores a dynamic set of strings where the keys are usually strings. Each node in the Trie represents a single character of a string, and the strings themselves are stored in a sequence of nodes connected by edges.

- **Efficient Searching**: The Trie allows for fast search, insert, and delete operations on strings.
- **Space Optimization**: It uses less space compared to other data structures like hash tables, as common prefixes of strings are shared.
- **Spell Checking and Suggestions**: The Trie is ideal for spell checking as it can quickly retrieve all words that share a common prefix, which is useful for generating spelling suggestions.

## Features

- **Spell Checking**: Checks if a word is spelled correctly.
- **Suggestions**: Provides suggestions for misspelled words.
- **Add and Remove Words**: Ability to add and remove words from the spell checker's dictionary.

## Running the Application

To run the application, you'll need Python installed on your machine. The application has been tested with Python 3.8.

### Steps:

1. **Clone the Repository**:
git clone [[URL to your repository](https://github.com/EpiXCoder/PrefixTrieSpellChecker.git)]
2. **Navigate to the Application Directory**:
cd [Application Directory]
3. **Load the Dictionary**:
- Place your dictionary file named `words` in the application directory. This file should contain a list of words, one per line.
4. **Run the Application**:
python3 app.py
5. **Use the text editor UI**:
- run the html
- Start typing in the text editor
- If you mispell a word, the application will underline the word in red and provide suggestions for correct spelling.
- Caveat: You must correct the words as you type and not wait till the end to do the correction

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.



## Acknowledgments

- [Any acknowledgments to resources, inspirations, or individuals]
