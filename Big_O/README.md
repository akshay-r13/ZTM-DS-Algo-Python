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

When calculating the Big O, we have to ignore the constants.

**Example:** Consider the following function

```python

def print_boxes_twice(boxes):
    for i in range(0, 4): # O(4)
        print("Printing number: ", + str(i))
    
    for i in range(len(boxes)): # O(n)
        print("Box: ", boxes[i])
        
    for i in range(len(boxes)): # O(n)
        print("Box: ",  boxes[i])
        

        
boxes = ['box1', 'box2', 'box3']

print_boxes_twice(boxes)

```

Output:
    
        Printing number: 0
        Printing number: 1
        Printing number: 2
        Printing number: 3
        Box: box1
        Box: box2
        Box: box3
        Box: box1
        Box: box2
        Box: box3
    
The runtime of the above function can be calculated as:

`O(fn) = O(4 + 2n)`

Here we can ignore 4 and `2n` can be simplified to `n`.

`O(fn) = O(n)`


### Rule 3: Different inputs should have different variables

In case of multiple inputs affecting the scale of a function. Consider the different inputs as different variables.

**Example:** Consider the following function

```python
def print_2_arrays(array1, array2):
    # Print first array
    for i in range(len(array1)):
        print(array1[i])
    # Print second array
    for i in range(len(array2)):
        print(array2[i])
        
        
array1 = [0,1,2,3]
array2 = ['a', 'b', 'c', 'd', 'e']

print_2_arrays(array1, array2)
```

Output:
    0
    1
    2
    3
    a
    b
    c
    d
    e
    
In the above example, the runtime depends on 2 inputs `array1` and `array2`. 

It can be denoted as:

`O(fn) = O(a + b)`

### Rule 4: Drop Non-dominant terms

Always consider the dominant terms in the calculation

**Example:** Consider the following function

```python

def print_numbers_then_combos(numbers):
    print("These are the numbers:")
    for i in range(len(numbers)):
        print(numbers[i])
        
    print("These are all the combinations:")
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])

numbers = [1,2,3]

print_numbers_then_combos(numbers)
```

Output:

    These are the numbers:
    1
    2
    3
    These are all the combinations:
    1, 1
    1, 2
    1, 3
    2, 1
    2, 2
    2, 3
    3, 1
    3, 2
    3, 3
    
For the above example

`O(fn) = O(n) + O(n^2)`

However we only care about the dominant term. So O(n) can be ignored

`O(fn) = O(n^2)`