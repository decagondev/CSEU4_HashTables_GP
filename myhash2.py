class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'

# lets refactor some code













if __name__ == "__main__":

    # put("Hello", "Hello Value")
    # put("World", "World Value")

    # print(f"{hash_table}\n")

    # put("foo", "foo value")   # "foo" hashes to same index as "Hello"
    #                         # AKA "foo collides with Hello"
    # print(f"\n{hash_table}\n");

    # v = get("Hello")
    # print(f'Hello value is: {v}') # Should be "Hello Value", but gives "foo value"
    pass