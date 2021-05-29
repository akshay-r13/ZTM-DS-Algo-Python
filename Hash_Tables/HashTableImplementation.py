
class HashTable:
    # Constructor that will receive a size (memory space size)
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i ) % self.size
        return hash
    
    def set(self, key, value):
        key_hash = self._hash(key)
        if self.data[key_hash] is None:
            self.data[key_hash] = []
        self.data[key_hash].append((key, value))
        return self.data[key_hash]
    
    def get(self, key):
        key_hash = self._hash(key)
        if self.data[key_hash] is not None:
            for i in self.data[key_hash]:
                if i[0] == key:
                    return i
        return None
    
hash_table = HashTable(2)

print(hash_table.set('grapes', 1))
print(hash_table.set('apple', 2))
print(hash_table.set('orange', 3))

print(hash_table.get('akshay'))
print(hash_table.get('grapes'))
print(hash_table.get('apple'))
print(hash_table.get('orange'))