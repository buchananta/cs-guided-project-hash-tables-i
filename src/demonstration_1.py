"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self, capacity = 100):
        # Your code here
       self.capacity = capacity
       self.storage = [None for _ in range(self.capacity)]

    def _hash(self, key):
        return id(key) % self.capacity

    def put(self, key, value):
        # Your code here
        i = self._hash(key)
        if self.storage[i] == None:
            self.storage[i] = ListNode(key, value)
        else:
            print(f"collision at {i}")
            node = self.storage[i]
            while node.next:
                if node.next.key == key:
                    node.next.value = value
                    return
                node = node.next
            node.next = ListNode(key, value)
            

    def get(self, key):
        # Your code here
        i = self._hash(key)
        if not self.storage[i]:
            return -1
        elif self.storage[i].key == key:
            return self.storage[i].value
        else:
            node = self.storage[i]
            while node.next:
                if node.next.key == key:
                    return node.next.value
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        # Your code here
        i = self._hash(key)
        if self.storage[i]:
            prev = None
            cur = self.storage[i]
            while cur:
                if cur.key == key:
                    if prev:
                        prev.next = cur.next
                        return
                    else:
                        self.storage[i] = cur.next
                        return
                prev = cur
                cur = cur.next 


hash_table = MyHashTable()
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a"))            
print(hash_table.get("c"))            
hash_table.put("b", 1)         
print(hash_table.get("b"))            
hash_table.remove("b")         
print(hash_table.get("b")) 
