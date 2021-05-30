
class Array:
    
    def __init__(self, data=[]):
        self.length = 0
        self.data = data
    
    def get(self, index):
        return self.data[index]
    
    def add(self, item):
        self.data.append(item)
        return self.data
    
    def delete(self, index):
        data_after = self.data[index+1:]
        self.data = self.data[:index]
        self.data = self.data + data_after
        return self.data
    
    def insert(self, item, index=0):
        data_after = self.data[index:]
        self.data = self.data[:index]
        self.data = self.data + [item] + data_after
        return self.data
    
    
    def __getitem__(self, index):
        return self.get(index)
    
    def __delitem__(self, index):
        self.delete(index)
        
    def __repr__(self):
        return str(self.data)
        
        
my_array = Array([1,2,3,4,5])

print("Adding to Array: ", my_array.add(6))
print("Getting item at index 3: ", my_array[3])
del my_array[3]
print("Deleted item at index 3: ", my_array)
print("Inserting to index 3: ", my_array.insert(4, index=3))
