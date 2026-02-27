"""
Build a Hash Table
In this lab, you will build a hash table from scratch. A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a class named HashTable with a collection attribute initialized to an empty dictionary when a new instance of HashTable is created. The collection dictionary should store key-value pairs based on the hashed value of the key.

The HashTable class should have four instance methods: hash, add, remove, and lookup.

The hash method should:

Take a string as a parameter.
Return a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string. You can use the ord function for this computation.
The add method should:

Take two arguments representing a key-value pair, and compute the hash of the key.
Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary.
If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value.
The remove method should:

Take a key as its argument and compute its hash.
Confirm if the key exists in the collection.
Remove the corresponding key-value pair from the hash table.
If the key does not exist in the collection, it should not raise an error or remove anything.
The lookup method should:

Take a key as its argument.
Compute the hash of the key, and return the corresponding value stored inside the hash table.
If the key does not exist in the collection, it should return None.
"""


class HashTable:
    def __init__(self):
        # The main storage for the hash table.
        # Keys = hash values (integers)
        # Values = buckets (dictionaries of original key/value pairs)
        self.collection = {}
    
    def hash(self, string: str) -> int:
        # hashing function:
        # Sum the ASCII values of each character in the string.
        ascii_total = 0
        for character in string:
            ascii_total += ord(character)
        return ascii_total

    def add(self, key, value):
        # Compute the hash for the given key.
        hash_value = self.hash(key)

        # If the bucket already exists, add/update the key inside it.
        # Otherwise, create a new bucket containing this key/value pair.
        if hash_value in self.collection:
            self.collection[hash_value][key] = value
        else:
            self.collection[hash_value] = {key: value}

    def remove(self, key: str):
        # Compute the hash for the key to locate its bucket.
        hash_value = self.hash(key)

        # Only attempt removal if the bucket exists AND the key is inside it.
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]

    def lookup(self, key: str):
        # Compute the hash to find the correct bucket.
        hash_value = self.hash(key)

        # If the bucket doesn't exist, the key isn't stored.
        if hash_value not in self.collection:
            return None

        # If the key isn't inside the bucket, return None.
        if key not in self.collection[hash_value]:
            return None    

        # Otherwise, return the stored value.
        return self.collection[hash_value][key]


def main():
    hash_table = HashTable()

    # Add some values to hash_table
    hash_table.add("Corey", 100)
    hash_table.add("Dog", "woof")
    hash_table.add("Cat", "meow")

    # Force a collision: "ab" and "ba" have the same ASCII sum
    hash_table.add("ab", 1)
    hash_table.add("ba", 2)

    # Lookups
    print("Lookup Corey:", hash_table.lookup("Corey"))
    print("Lookup Dog:", hash_table.lookup("Dog"))
    print("Lookup Cat:", hash_table.lookup("Cat"))
    print("Lookup ab:", hash_table.lookup("ab"))
    print("Lookup ba:", hash_table.lookup("ba"))

    # Lookup missing key
    print("Lookup missing key:", hash_table.lookup("Zebra"))

    # Remove a key
    hash_table.remove("Dog")
    print("Lookup Dog after removal:", hash_table.lookup("Dog"))

    # Remove a key inside a collision bucket
    hash_table.remove("ab")
    print("Lookup ab after removal:", hash_table.lookup("ab"))
    print("Lookup ba still exists:", hash_table.lookup("ba"))

    # Print internal structure to inspect buckets
    print("Internal table:", hash_table.collection)


if __name__ == "__main__":
    main()

