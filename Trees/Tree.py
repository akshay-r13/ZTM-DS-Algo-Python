from pprint import pprint

class BinaryTree:
    
    class Node:
        def __init__(self, value, parent=None):
            self.value = value
            self.left = None
            self.right = None
            self.parent = parent
            
        def is_leaf(self):
            # node is a leaf if there are no left and right nodes
            return self.right is None and self.left is None
        
        def __str__(self):
            return str(self.value)
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        # Create a new node with the new value
        if self.root is None:
            new_node = self.Node(value)
            self.root = new_node
        else:
            self._insert_node(current_node = self.root, value = value)
        return self.root
                
    def _insert_node(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                new_node = self.Node(value, parent=current_node)
                current_node.left = new_node
            else:
                self._insert_node(current_node = current_node.left,  value = value)
        else:
            if current_node.right is None:
                new_node = self.Node(value, parent=current_node)
                current_node.right = new_node
            else:
                self._insert_node(current_node = current_node.right,  value = value)
    
    def _lookup_node(self, node, value):
        if value == node.value:
            return node
        if value < node.value and node.left is not None:
            return self._lookup_node(node.left, value)
        if value > node.value and node.right is not None:
            return self._lookup_node(node.right, value)
    
    def lookup(self, value):
        return self._lookup_node(self.root, value)
    
#     def find_successor(self, node):
#         current_node = node
#         while(current_node is not None):
            
        
     
    def remove(self, value):
        # find the node
        node = self.lookup(value)
        
        if node is None:
            raise Exception("Value not found in tree!")
        
        # if node is a leaf. delete the node
        if node.is_leaf():
            # remove link of parent to child node
            parent_node = node.parent
            if node.value > parent_node.value: 
                parent_node.right = None
            else:
                parent_node.left = None
            # delete node
            del node
            return self.root
        
        # if only one child, bypass the node
        # if left node is not present
        if node.left is None:
            parent_node = node.parent
            child_node = node.right
            child_node.parent = parent_node
            if node.value > parent_node.value: 
                parent_node.right = child_node
            else:
                parent_node.left = child_node          
            return self.root
            
            
        # if right node is not present
        if node.right is None:
            parent_node = node.parent
            child_node = node.left
            if node.value > parent_node.value: 
                parent_node.right = child_node
            else:
                parent_node.left = child_node
            return self.root
            
        # if node has only one child. bypass the node
        
        # else replace node with successor
        return self.root
    
    def _traverse_node(self, node):
        tree_dict = {'value': node.value, 'parent': str(node.parent)}
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

rm_val = 5
print(f"Removing {rm_val} from tree (single child): ")
binary_tree.remove(rm_val)
pprint(binary_tree.traverse(), width=1)

print("Lookup value: ",rm_val, binary_tree.lookup(rm_val))

rm_val = 10
print(f"Removing {rm_val} from tree (single child): ")
binary_tree.remove(rm_val)
pprint(binary_tree.traverse(), width=1)

print("Lookup value: ",rm_val, binary_tree.lookup(rm_val))
