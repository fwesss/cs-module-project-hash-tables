#!/usr/bin/env python
from functools import reduce
from typing import Any, List, Optional


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key: str, value: Any):
        self._key = key
        self._value = value
        self._next = None

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> Any:
        return self._value

    @property
    def next(self):
        return self._next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity: int = MIN_CAPACITY):
        self._capacity = capacity
        self._storage = [None] * capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def storage(self) -> List[Optional[int]]:
        return self._storage

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """

        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        # Your code here
        pass

    @staticmethod
    def fnv1(key: str) -> int:
        """
        FNV-1 Hash, 64-bit
        """
        return reduce(
            lambda hash_key, letter: (hash_key ^ ord(letter)) * 0x100000001B3,
            key,
            0xCBF29CE484222325,
        )

    @staticmethod
    def djb2(key: str) -> int:
        """
        DJB2 hash, 32-bit
        """
        return (
            reduce(
                lambda hash_key, letter: ((hash_key << 5) + hash_key) + ord(letter),
                key,
                5381,
            )
            & 0xFFFFFFFF
        )

    def hash_index(self, key: str) -> int:
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key: str, value: Any) -> None:
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """
        self.storage[self.hash_index(key)] = value

    def delete(self, key: str) -> None:
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        try:
            del self.storage[self.hash_index(key)]
        except IndexError:
            print("Key not found")

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        try:
            return self.storage[self.hash_index(key)]
        except IndexError:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
