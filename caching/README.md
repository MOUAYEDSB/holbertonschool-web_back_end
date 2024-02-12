# Caching Project
<img src="image/images.jpg" alt="python-img-project ">

## Description

In this project, we explore different caching algorithms and implement them in Python. Each caching system has unique characteristics and is designed to optimize performance in various scenarios.

## Requirements

### Python Scripts:

- All Python files should be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- All your files should use the `pycodestyle` style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.

## Tasks

### 0. Basic dictionary

Create a class BasicCache that inherits from BaseCaching and is a caching system:

- Must use self.cache_data - dictionary from the parent class BaseCaching.
- This caching system doesn’t have a limit.
- Implement put(self, key, item) and get(self, key) methods.

### 1. FIFO caching

Create a class FIFOCache that inherits from BaseCaching and is a caching system:

- Must use self.cache_data - dictionary from the parent class BaseCaching.
- Implement put(self, key, item) and get(self, key) methods.
- If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS, discard the first item put in cache (FIFO algorithm).

### 2. LIFO caching

Create a class LIFOCache that inherits from BaseCaching and is a caching system:

- Must use self.cache_data - dictionary from the parent class BaseCaching.
- Implement put(self, key, item) and get(self, key) methods.
- If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS, discard the last item put in cache (LIFO algorithm).

### 3. LRU caching

Create a class LRUCache that inherits from BaseCaching and is a caching system:

- Must use self.cache_data - dictionary from the parent class BaseCaching.
- Implement put(self, key, item) and get(self, key) methods.
- If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS, discard the least recently used item (LRU algorithm).

### 4. MRU caching

Create a class MRUCache that inherits from BaseCaching and is a caching system:

- Must use self.cache_data - dictionary from the parent class BaseCaching.
- Implement put(self, key, item) and get(self, key) methods.
- If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS, discard the most recently used item (MRU algorithm).

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing the caching scripts.
3. Run the desired script using Python 3.

```bash
$ python3 script_name.py
```
