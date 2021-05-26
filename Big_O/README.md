# Big O Notation

## What is good code?

The 3 pillars of good code are:

1. Readability
2. Scalability
    - Time Complexity
    - Space Complexity

Big O is used to indicate the **Scalability** of code

## Definition of Big O


    “ Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. It is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called Bachmann–Landau notation or asymptotic notation. ”

    — Wikipedia’s definition of Big O notation


In simpler words Big O is used to indicate **how the runtime / memory consumption of a program increases** with increase in size of the input.

---

## Big O Cheat Sheet

### Types

`O(1)` - Constant
- No loops
- Example: Assignment operations

`O(n)` - Linear
- Loops
- Example: For, While loops through **n** items

`O(log N)` - Logarithmic 
- Usually searching algorithms have log n if they are sorted
- Example: Binary Search

`O(n log(n))` - Log Linear 
- Usually sorting operations
- Example: 

`O(n^2)` - Quadratic
- Two nested loops
- Example: Bubble Sort, every element in a collection needs to be compared to ever other element. 

`O(2^n)` - Exponential
- recursive algorithms that solves a problem of size N

`O(n!)` - Factorial
- Worst case scenario
- Example: You are adding a loop for every element

### Big O Time Complexity Operations
1. Arithmetic Operations `(+, -, *, /)`
2. Comparisons `(<, >, ==)`
3. Looping `(for, while)`
4. Function calls `(function())`

### Big O Space Complexity Operations
1. Variables
2. Data Structures
3. Function Calls
4. Allocations

---

## Rule Book

### Rule 1: Always consider the worst Case
Always consider the worst efficient scenario.

**Example:** Finding item in an array

```python
# Function to find item in an array
def find_item(array, item):
    for i in range(0, len(array)):
        print("Checking item number: ", str(i))
        if array[i] == item:
            print("Found Item '", item , "' at index ", str(i))
            return i
    print("Item not found")
```
There are 2 scenarios:

1. Best case scenario: Item is the first element in the list

```python
fruits = ['apple', 'orange', 'banana', 'watermelon', 'mango']

find_item(array=fruits, item='apple')
```
Output:

    Checking item number: 0
    Found Item 'apple' at index 0  

2. Worst case scenario: Item is not present in the list

```python
fruits = ['apple', 'orange', 'banana', 'watermelon', 'mango']

find_item(array=fruits, item='pomegranate')

```

Output:

    Checking item number: 0
    Checking item number: 1
    Checking item number: 2
    Checking item number: 3
    Checking item number: 4
    Item not found

In scenario 1, total operations: 1 . O(1)

In scenario 2, total operations: n (size of array). O(n)

**We must Consider scenario 2 O(n) while calculating Big O**

### Rule 2:  Remove Constants


### Rule 3: Different inputs should have different variables
O(a+b). 
A and B arrays nested would be O(a*b) + for steps in order* for nested steps

### Rule 4: Drop Non-dominant terms
