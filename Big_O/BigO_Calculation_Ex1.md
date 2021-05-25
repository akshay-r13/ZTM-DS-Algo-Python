// O(1) -> Assignment# Big O Calculation - Exercise 1

**Goal:** To calculate the Big O Notation of the following function

**Language**: `Javascript`


```javascript
function funChallenge(input) {
  let a = 10;
  a = 50 + 3;

  for (let i = 0; i < input.length; i++) {
    anotherFunction();
    let stranger = true;
    a++;
  }
  return a;
}
```

**Analysis:**

Code analysis line by line

```javascript
    let a = 10; // O(1) -> Assignment

    a = 50 + 3; // O(1) -> Assignment

    for (let i = 0; i < input.length; i++) { // O(n) -> loop depends on length of input ( n ). Each operation in loops is executed n times totally

        anotherFunction(); // O(n)* O(1) as function has no dependency on input size

        let stranger = true; // O(n) * O(1) -> Assignment

        let a = 10; // O(n) * O(1) -> Assignment
    }
    return a; // O(1) -> Value return
```

**Calculation:** 

```
    O(fn) = O(1 + 1 + n + n + n + 1)
    O(fn) = O(3 + 3n)
    Simplified as: 
    O(fn) = O(n)
```

**Result:** Big O Notation of this function is `O(n)`

**Notes:**
1. Only the loop operation is dependent on input size
2. Loops generally have O(n) execution time.
3. Assignment has constant execution time
4. Coefficients of O notation can be **simplified to 1**. ( O(3) => O(1) , O(2n) => O(n) )