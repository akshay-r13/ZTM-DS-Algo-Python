# Big O Calculation - Exercise 2

**Goal:** To calculate the Big O Notation of the following function

**Language**: `Javascript`


```javascript
function anotherFunChallenge(input) {
  let a = 5;
  let b = 10;
  let c = 50;
  for (let i = 0; i < input; i++) {
    let x = i + 1;
    let y = i + 2;
    let z = i + 3;

  }
  for (let j = 0; j < input; j++) {
    let p = j * 2;
    let q = j * 2;
  }
  let whoAmI = "I don't know";
}
```

**Analysis:**

Code analysis line by line

```javascript
  let a = 5; // O(1) -> Assignment
  let b = 10; // O(1) -> Assignment
  let c = 50; // O(1) -> Assignment
  for (let i = 0; i < input; i++) { // O(n) -> loop depends on size of input ( n )
    let x = i + 1; // O(n) * O(1) -> Assignment  
    let y = i + 2; // O(n) * O(1) -> Assignment
    let z = i + 3; // O(n) * O(1) -> Assignment

  }
  for (let j = 0; j < input; j++) {  // O(n) -> loop depends on size of input ( n )
    let p = j * 2; // O(n) * O(1) -> Assignment
    let q = j * 2; // O(n) * O(1) -> Assignment
  }
  let whoAmI = "I don't know"; // O(1) -> Assignment
```

**Calculation:** 

```
    O(fn) = O(1 + 1 + 1 + 3n + 2n + 1 )
    O(fn) = O(4 + 5n)
    Simplified as:
    =>  O(fn) = O(n)
    
    
```

**Result:** Big O Notation of this function is `O(n)`

**Notes:**
1. Only the loop operation is dependent on input size
2. Loops generally have O(n) execution time.
3. Assignment has constant execution time
4. Coefficients of O notation can be **simplified to 1**. ( O(3) => O(1) , O(2n) => O(n) )