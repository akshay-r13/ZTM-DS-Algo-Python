
class HashTable:
    '''
        A Simple Hash Table Class.
        
        Uses custom hash function
        
    '''
    
    def __init__(self, size):
        '''
        __init__()
        
        Input:
            size (int) -> Size of the hashmap
        Returns:
            None
        '''
        self.size = size
        self.data = [None] * size
        
    def _hash(self, key):
        '''
        _hash() Hash function for HashTable obj
        
        Input:
            key (str) -> The string which is to be hashed
        Returns:
            hash: Hash value computed for the given key
        '''
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i ) % self.size
        return hash
    
    def set(self, key, value):
        '''
        set() -> Set value for key in hash table
        
        Input:
            key (str) -> The key to store
            value (any) -> The value to store under the given key
        Returns:
            list of (key, value) pairs stored under the key
        '''
        # Obtaining hash of the key
        key_hash = self._hash(key)
        # Create a list under the key hash if not exists (To deal with hash collisions)
        if self.data[key_hash] is None:
            self.data[key_hash] = []
        # Store the key, value pair under the key hash list
        self.data[key_hash].append((key, value))
        return self.data[key_hash]
    
    def get(self, key):
        '''
        get() -> Get value from hash table for given key
        Input:
            key (str)
        Returns:
            value -> The value stored under the key. None if key doesn't exist in the table.
        
        '''
        key_hash = self._hash(key)
        if self.data[key_hash] is not None:
            for i in self.data[key_hash]:
                if i[0] == key:
                    return i
        return None
    
    
# Create a hash table
hash_table = HashTable(2)

# Set key, values
print(hash_table.set('grapes', 1))
print(hash_table.set('apple', 2))
print(hash_table.set('orange', 3))

# Get values using key
print(hash_table.get('akshay'))
print(hash_table.get('grapes'))
print(hash_table.get('apple'))
print(hash_table.get('orange'))