# Fix My Code Challenge

A series of broken code snippets to debug and fix across multiple languages.

## Files

### 1. Print Square - challenge/1-print_square.js
Language: JavaScript (Node.js)
Bug: parseInt used base 16 instead of 10, causing wrong square size.
Fix: Changed parseInt(process.argv[2], 16) to parseInt(process.argv[2], 10).

### 2. Sort Arguments - challenge/2-sort.rb
Language: Ruby
Bug: Arguments sorted as strings (lexicographic) instead of integers.
Fix: Added map(&:to_i) to convert to integers before sorting.

### 3. User Password - challenge/3-user.py
Language: Python 3
Bug 1: Setter wrote to _password instead of __password.
Bug 2: is_valid_password compared hashes with .upper() vs .lower().
Fix: Corrected attribute name and unified hash comparison to .lower().

### 4. Double Linked List - challenge/4-delete_dnodeint/
Language: C
Bug 1: prev->prev updated instead of prev->next, breaking the chain.
Bug 2: head dereferenced after free(), causing undefined behavior.
Fix: Saved node to tmp before freeing, then correctly updated both links.

## Author
Holberton School - Fix My Code Challenge
