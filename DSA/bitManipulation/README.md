**Bitwise Operators in Java:**

1. **AND (&)**  
   - Sets each bit to 1 if both bits are 1.  
   - Example: `a & b`

2. **OR (|)**  
   - Sets each bit to 1 if at least one of the bits is 1.  
   - Example: `a | b`

3. **XOR (^)**  
   - Sets each bit to 1 if only one of the bits is 1.  
   - Example: `a ^ b`

4. **NOT (~)**  
   - Inverts all the bits.  
   - Example: `~a`

5. **Left Shift (<<)**  
   - Shifts bits to the left, filling with 0s.  
   - Example: `a << n` (multiplies by 2ⁿ)

6. **Right Shift (>>)**  
   - Shifts bits to the right, preserving the sign (sign extension).  
   - Example: `a >> n` (divides by 2ⁿ)

7. **Unsigned Right Shift (>>>)**  
   - Shifts bits to the right, filling with 0s (no sign extension).  
   - Example: `a >>> n`

---

**Common DSA Uses:**

- **Checking even/odd:** `if ((n & 1) == 0)` (even)
- **Swapping values:** `a ^= b; b ^= a; a ^= b;`
- **Setting a bit:** `n |= (1 << k);`
- **Clearing a bit:** `n &= ~(1 << k);`
- **Toggling a bit:** `n ^= (1 << k);`
- **Checking a bit:** `if ((n & (1 << k)) != 0)`
- **Counting set bits:** Use `Integer.bitCount(n)` or loop with `n & (n-1)`
- **Fast multiplication/division by powers of two:** `n << k`, `n >> k`

---

<<<<<<< HEAD
## How to Count Set Bits Using Brian Kernighan's Algorithm
=======
## How to Count Set Bits Using Brian Kernighan's Algorithm (leetcode problem number 191)
>>>>>>> main
Brian Kernighan's algorithm is an efficient way to count the number of set bits (1s) in the binary representation of an integer. The key idea is that subtracting 1 from a number flips all the bits after the rightmost set bit, including the rightmost set bit itself. By performing n = n & (n - 1), you clear the lowest set bit in each iteration.

**How it works:**
- Initialize a counter to 0.
- While n is not zero:
  - Increment the counter.
  - Set n = n & (n - 1).
- The counter will contain the number of set bits.

**Java Example:**
```java
public int countSetBits(int n) {
    int count = 0;
    while (n != 0) {
        // what n & (n - 1) does is it reduces the number of set bits by 1:
        /* Example:
           n = 12 (1100 in binary)
           n - 1 = 11 (1011 in binary)
           n & (n - 1) = 8 (1000 in binary) -> reduces set bits from 2 to 1
        */
        n = n & (n - 1);
        count++;
    }
    return count;
}
```

**Usage:**
```java
int num = 29; // Binary: 11101
int setBits = countSetBits(num); // setBits = 4
```

<<<<<<< HEAD

=======
## leetcode problem that are related to Bit Manipulation:
1. **191. Number of 1 Bits** - Count the number of 1 bits in an integer.
2. **338. Counting Bits** - Return an array of the number of 1 bits for all numbers from 0 to n.
3. **136. Single Number** - Find the element that appears only once in an array
>>>>>>> main
