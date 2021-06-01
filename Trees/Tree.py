from pprint import pprint

class BinaryTree:
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        # Create a new node with the new value
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(parent_node = self.root, new_node = new_node)
                
        return self.root
                
    def _insert_node(self, parent_node, new_node):
        if new_node.value < parent_node.value:
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                self._insert_node(parent_node = parent_node.left, new_node=new_node)
        else:
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                self._insert_node(parent_node = parent_node.right, new_node = new_node)
    
    def _lookup_node(self, node, value):
        if value == node.value:
            return value
        if value < node.value and node.left is not None:
            return self._lookup_node(node.left, value)
        if value > node.value and node.right is not None:
            return self._lookup_node(node.right, value)
    
    def lookup(self, value):
        return self._lookup_node(self.root, value)
        
    
    def remove(self, value):
        pass
    
    def _traverse_node(self, node):
        tree_dict = {'value': node.value}
        tree_dict['right'] = self._traverse_node(node.right) if node.right is not None else None
        tree_dict['left'] = self._traverse_node(node.left) if node.left is not None else None
        return tree_dict
    
    
    def traverse(self):
        tree_dict = self._traverse_node(self.root)
        return tree_dict

    

    
binary_tree = BinaryTree()

print("Insert Value in Tree: ", 20)
binary_tree.insert(20)
print("Insert Value in Tree: ", 10)
binary_tree.insert(10)
print("Insert Value in Tree: ", 30)
binary_tree.insert(30)
print("Insert Value in Tree: ", 5)
binary_tree.insert(5)
print("Insert Value in Tree: ", 14)
binary_tree.insert(14)
print()
print("Tree: ")
pprint(binary_tree.traverse(), width=1)
print()

print("Lookup value: ", 10, binary_tree.lookup(10))
print("Lookup value: ", 25, binary_tree.lookup(25))