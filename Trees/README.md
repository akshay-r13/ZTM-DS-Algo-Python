# Trees

Tree components

Root 
Parent
Chld
Leaf 
Sibling

DOM in Websites is a Tree data structure

website comment sections

Abstract syntax tree

Child node in tree doesnt need to point to parent

Many types of tree data structures

## Binary Trees

Binary tree is a tree where each node has 0,1 or 2 child nodes.

Every child node has only 1 parent

Perfect Binary Tree
1. Very efficient
2. Number of total nodes doubles as we move down the tree
3. 1 -> 2 -> 4 -> 8 ...
4. Number of nodes in last level = sum(all nodes above last level) + 1
5. Half of our nodes are in the last level.



Full Binary Tree

## Olog(n)

Level 0: 2^0
Level 1: 2^1
Level 2: 2^2
Level 3: 2^3
.
.
.


Number of nodes in a Tree: 2^h - 1
h = height of the tree (or) number of levels in the tree

logN , divide and conquer. at every stage check one of many possibilities

https://visualgo.net/bn/bst

## Balanced & Unbalanced BST

Kind of becomes a linked list

Ideally we want a balanced BST

avl tree , red black tree for having balanced trees

## Pros & Cons


Olog(n) operations
Ordered
Flexible size

No O(1) operations. 


