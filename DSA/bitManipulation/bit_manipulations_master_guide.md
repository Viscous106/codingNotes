# High-Yield Study Guide: Bit Manipulations (Classes 1 - 3)

This master document synthesizes the core concepts, bitwise properties, algorithms, and classic LeetCode problems covered across your entire 3-part Bit Manipulations lecture series.

---

## Part 1: Fundamentals & Properties (Class 1)

### 1. Data Size Context
* **`byte`** (8 bits): Range from `-128` to `127`
* **`short`** (16 bits): Range from $-2^{15}$ to $2^{15} - 1$
* **`int`** (32 bits): Range from $-2^{31}$ to $2^{31} - 1$
* **`long`** (64 bits): Range from $-2^{63}$ to $2^{63} - 1$

### 2. The 4 Main Logical Operators
* **AND (`&`)**: Returns `1` **only if both** bits are `1`.
* **OR (`|`)**: Returns `1` **if at least one** bit is `1`.
* **XOR (`^`)**: Returns `1` **only if the bits are different**.
* **NOT (`~`)**: Inverts the bits (`1` $\rightarrow$ `0`, `0` $\rightarrow$ `1`). 

### 3. Vital Mathematical Bit Properties
These cancelation properties are the backbone of $O(N)$ competitive programming solutions:
* **Null Properties**: 
  * `A & 0 = 0`
  * `A | 0 = A`
  * `A ^ 0 = A`
* **Self-Cancellation**: 
  * `A & A = A`
  * `A | A = A`
  * **`A ^ A = 0`** *(Crucial! Any number XORed with itself is completely erased).*

### 4. Basic Techniques
* **Even / Odd Checker**: 
  * `if (A & 1 == 1)` $\rightarrow$ Odd Number. 
  * `if (A & 1 == 0)` $\rightarrow$ Even Number.
* **Left Shift (`<<`)**: `A << n` acts as **Multiplying** `A` by $2^n$.
* **Right Shift (`>>`)**: `A >> n` acts as integer **Division** of `A` by $2^n$.
* **Negative Numbers (2's Complement)**: To store negatives, computers invert the absolute value's binary and add `1`.

---

## Part 2: Specific Bit Targeting (Class 2)

Class 2 focuses heavily on using **Bitmasks** (usually `1 << i`) to manipulate a specific $i$-th bit of a number `N` (0-indexed from right to left).

* **Check Bit**: Is the $i$-th bit a 1?
  * `if ((N & (1 << i)) != 0)`
* **Set Bit**: Force the $i$-th bit to become 1.
  * `N = N | (1 << i)`
* **Toggle (Flip) Bit**: Change the $i$-th bit (`0`$\rightarrow$`1` or `1`$\rightarrow$`0`).
  * `N = N ^ (1 << i)`
* **Unset Bit**: Force the $i$-th bit to become 0.
  * `N = N & ~(1 << i)`

### Array Problem: Subarrays with OR = 0
* **Concept**: A bitwise OR sum is only `0` if **every single element** in the subarray is `0`.
* **Algorithm**: Traverse the array, counting the lengths of consecutive `0` clusters. For a cluster of length $k$, the valid subarrays it creates is exactly $k \times (k + 1) / 2$. Sum these up.

### Array Problem: Maximum AND Pair
* **Concept**: Find two numbers in an array that produce the highest `AND` product.
* **$O(N)$ Algorithm**: Iterate from highest bit (31) down to lowest (0). Count how many array values have a `1` at the current bit position. If `count >= 2`, lock this bit as part of your answer, and "delete/ignore" all numbers that have a `0` at this bit position. Move to the next bit.

---

## Part 3: XOR Algorithms & Single Numbers (Class 3)

Class 3 focuses on using the `A ^ A = 0` property to isolate unique numbers hiding among duplicates in an array perfectly in linear time.

### 1. Count Set Bits (Kernighan's Algorithm)
* **Problem**: Quickly count how many `1`s are in a number.
* **Algorithm**: Run a `while (N > 0)` loop executing the operation `N = N & (N - 1)`. This specific math drops the rightmost `1` from the integer. Increment a counter each time until `N == 0`. It runs incredibly fast because it skips all `0`s!

### 2. Single Number I (LeetCode 136)
* **Problem**: Every element appears twice, except for one unique element. `[4, 5, 5, 4, 1]`
* **Algorithm**: XOR the entire array together. The duplicates all cancel each other out ($4 \verb|^| 4 = 0$, $5 \verb|^| 5 = 0$). Only the unique element is left behind! `Ans = 1`.

### 3. Single Number II (LeetCode 137)
* **Problem**: Every element appears **three times**, except for one unique element.
* **Algorithm (Counting Strategy)**: Loop through bits 0 to 31. Vertically count how many total `1`s exist at that bit column. Since duplicates appear 3 times, take the `count % 3`. If the remainder is `1`, the unique number has a `1` at this bit! Piece it together using Set Bit logic.
* **Algorithm (Optimal State-Machine)**: Use `ones` and `twos` buckets:
  * `ones = (ones ^ num) & ~twos`
  * `twos = (twos ^ num) & ~ones`
  * At the end of the loop, the unique number securely sits inside `ones`.

### 4. Single Number III (LeetCode 260)
* **Problem**: Every element appears twice, except for **two distinct numbers**. `[4, 5, 4, 1, 6, 6, 5, 2]`
* **Algorithm**: 
  1. XOR the entire array to get `xorAll`. This leaves you with `uniqueX ^ uniqueY`.
  2. Find any set bit (a `1`) inside `xorAll`. *This bit represents a position where uniqueX and uniqueY are different.* You can find the rightmost set bit using `int mask = xorAll & -xorAll`.
  3. Traverse the array again and split the numbers into two buckets based on that bit: `if ((num & mask) != 0)`.
  4. The two unique numbers get separated into different buckets. The duplicate pairs get forced into the exact same buckets together and cleanly cancel out!
  5. XOR everything inside Bucket 1 to get `uniqueX`. XOR everything inside Bucket 2 to get `uniqueY`.
