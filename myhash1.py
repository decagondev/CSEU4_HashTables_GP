hash_table = [None] * 8   # 8 slots, all initiailized to None

def my_hash(s):
    sb = s.encode()  # Get the UTF-8 bytes for the string

    sum = 0

    for b in sb:
        sum += b
        sum &= 0xffffffff  # clamp to 32 bits

    return sum

# hash the index
def hash_index(key):
    pass

# put
def put(key, val):
    pass

# get
def get(key):
    pass

# delete
def delete(key):
    pass


if __name__ == "__main__":

    put("Hello", "Hello Value")
    put("World", "World Value")
    put("foo", "foo value")   # "foo" hashes to same index as "Hello"
                            # AKA "foo collides with Hello"

    print(hash_table)

    v = get("Hello")
    print(v) # "Hello Value"

    # Get "Frogs" from the table
    # Doesn't exist!
    v = get("Frogs")
    print(v)  # "None"