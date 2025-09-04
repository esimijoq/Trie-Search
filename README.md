# Trie-Search
This repository preprocesses text data, builds a trie, provides search and autocomplete functionality for words based on their prefixes.

## The code performs the following steps:

**1. Text Preprocessing:**  
-Removes punctuation from a list of sample texts and from an external text file.  
-Splits texts into individual words for further processing.

**2. Trie Construction:**  
-Builds a trie data structure where each word is stored character by character.  
-Marks word endings to enable accurate search results.

**3. Word Search & Autocomplete:**  
-Implements a function to check whether a given word exists in the trie.  
-Implements another function to return all words that start with a given prefix, providing an autocomplete-like feature.
