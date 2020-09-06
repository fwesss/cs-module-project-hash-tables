#!/usr/bin/env python
from functools import reduce
from typing import Any, List, Optional


class HashTableEntry:
    def __init__(self, key: Optional[str], value: Any):
        self._key = key
        self._value = value
        self._next = None

    @property
    def key(self) -> str:
        return self._key

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node


class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = HashTableEntry(None, None)

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    @property
    def head(self) -> HashTableEntry:
        return self._head

    def _find(self, key: str) -> Optional[HashTableEntry]:
        if self.size == 0:
            return None

        current = self.head
        while current is not None:
            if current.key == key:
                return current

            current = current.next

        return None

    def _add(self, key: str, value: Any) -> None:
        new_node = HashTableEntry(key, value)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def put(self, key: str, value: Any) -> None:
        if self.size == 0:
            self._add(key, value)
        else:
            node_to_update = self._find(key)
            if node_to_update:
                node_to_update.value = value
            else:
                self._add(key, value)

    def get(self, key: str) -> Optional[Any]:
        if self.size == 0:
            return None

        return self._find(key).value

    def delete(self, key: str) -> None:
        if self.size == 0:
            return None

        previous = self.head
        while previous.next is not None:
            if previous.next.key == key:
                previous.next = previous.next.next
                self.size -= 1
                return None

        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity: int = MIN_CAPACITY):
        self._capacity = capacity
        self._storage = [LinkedList() for _ in range(capacity)]

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def storage(self) -> List[LinkedList]:
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
        return (
            reduce(
                lambda accumulator, linked_list: accumulator + linked_list.size,
                self.storage,
                0,
            )
            / self.capacity
        )

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
                0x1505,
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
        self.storage[self.hash_index(key)].put(key, value)

    def delete(self, key: str) -> None:
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        """
        try:
            self.storage[self.hash_index(key)].delete(key)
        except IndexError:
            print("Key not found")

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        try:
            return self.storage[self.hash_index(key)].get(key)
        except IndexError:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
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
