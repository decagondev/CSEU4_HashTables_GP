# Hash Tables

## The Problem With Arrays

What is the problem we are trying to solve?
- With a list / array it is `O(n)` to linear search and `O(log n)` for a binary search.

```python
arr = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
#        0         1        2       3      4           5              6          7    
```

- Can we do better?
YES!

lookup with `O(1)` time complexity using a magic function?
- 

## Hash Functions

What is a hash function?
- we can input a string
- it will output a number
- it has to be deterministic



## Map the hash!

The numbers that we have generated could get fairly large and we need a way to turn them in to an index of a list / array.

Think of ways to do this geven a finite size of a list to turn the number in to one clamped to a range


## Summary
Hash Table has mthods / functions to put data in to it and to get data out of it

To Put:
1. Run the key string through a hashing function to get a hash value
2. Mod the hash value with the table size to get the index
3. Store the value at this index

To Get:
1. Run the key string through a hashing function to get a hash value
2. Mod the hash value with the table size to get the index
3. Return the value at this index



## LLC

```
Slot
Index    Chain (LL)
-----    -------------------------------------------
0        -> ({ key: "qux", val: 10 })
1        -> ({ key: "foo", val: 12 }) -> ({ key: "plugh", val: 20 })
2        -> ({ key: "bar", val: 30 }) -> ({ key: "baz", val: 999 }) -> ({ key: "xyzzy", val: 50 })
3        -> None
```

```python

# Put
put("foo", 12) # hash to 1
put("bar", 30) # hash to 2
put("baz", 999) # hashes to 2 (collision!)
put("qux", 10) # hash to 0
put("plugh", 20) # hash to 1 (Collision!)
put("xyzzy", 50) # hash to 2 (Collision!)

# Get
get("foo") # 1 => 12
get("bar") # 2 => 30
get("baz") # 2 C -> move to heads next => 999
```

```
