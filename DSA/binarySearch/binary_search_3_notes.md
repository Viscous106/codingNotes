# Binary Search Part 3: Quick Revision Notes

These notes summarize the crucial concepts from the "Binary Search 3" module, focusing heavily on **Binary Search on Answer Space** for optimization problems.

## 1. Painter's Partition Problem (Revisited)
**Problem:** Given $N$ boards of different lengths, find the **minimum time required** to paint all boards using **at most** $P$ painters. 
*(Note: A single painter paints continuous segments. 1 unit length = 1 unit time).*

**Key Idea:** Instead of assigning boards directly, we guess the answer (amount of Time) and verify if it's possible.
* **More Time = Less Painters needed.**
* **Less Time = More Painters needed.**
We want the *minimum time* that requires $\le P$ painters.

**Search Space:**
* Minimum Possible Time (`l`) = Largest single board (`max(A)`) $\rightarrow$ If we had infinite painters, the bottleneck is the biggest board.
* Maximum Possible Time (`r`) = Sum of all boards (`sum(A)`) $\rightarrow$ If we only had 1 painter.

```java
public int paint(int P, int[] C) {
    long l = 0, r = 0;
    for (int board : C) {
        l = Math.max(l, board);  // Max single board
        r += board;              // Sum of all boards
    }
    
    long ans = r; 
    
    while (l <= r) {
        long mid = l + (r - l) / 2; // 'mid' is the Guessed Time!
        
        if (canPaintInTime(C, P, mid)) {
            ans = mid;      // Valid answer! But can we do it FASTER?
            r = mid - 1;    // Try less time
        } else {
            l = mid + 1;    // Not enough time! We need MORE time
        }
    }
    return (int) (ans % 10000003); // Sometimes modulo is required
}

// Helper: Checks if all boards can be painted in 'maxTime' using 'P' painters
private boolean canPaintInTime(int[] C, int P, long maxTime) {
    int paintersUsed = 1;
    long currentPainterTime = 0;
    
    for (int length : C) {
        currentPainterTime += length;
        
        if (currentPainterTime > maxTime) {
            paintersUsed++;             // Assign to NEXT painter
            currentPainterTime = length; 
            
            if (paintersUsed > P) return false; // Ran out of painters!
        }
    }
    return true;
}
```
**Time Complexity:** `O(N * log(Sum - Max))`

---

## 2. Aggressive Cows Problem
**Problem:** A farmer has built a barn with $N$ stalls located at positions `A[i]` (sorted array). He needs to place $M$ cows in the stalls. The cows are aggressive, so the farmer wants to place them such that the minimum distance between any two cows is **maximized**. Find this maximum possible minimum distance.

**Key Idea:** This is another "Binary Search on Answer Space" problem!
We guess the *minimum distance `D`*, and check if we can successfully place all $M$ cows in the stalls such that every cow is at least `D` units apart.

**Search Space (The expected Minimum Distance):**
* Minimum Possible Distance (`l`) = `1` $\rightarrow$ Cows are immediately adjacent.
* Maximum Possible Distance (`r`) = `A[N-1] - A[0]` $\rightarrow$ Distance between the first and last stall (only possible if $M=2$).

```java
public int solve(int[] A, int M) {
    Arrays.sort(A); // Stalls MUST be sorted
    
    int n = A.length;
    int l = 1;                                // Min possible distance
    int r = A[n - 1] - A[0];                  // Max possible distance
    int ans = 1;
    
    while (l <= r) {
        int mid = l + (r - l) / 2; // 'mid' is the Guessed Minimum Distance
        
        if (canPlaceCows(A, M, mid)) {
            ans = mid;      // Valid distance! But can we push them FURTHER apart?
            l = mid + 1;    // Try a LARGER distance
        } else {
            r = mid - 1;    // Impossible. The cows must be closer together.
        }
    }
    return ans;
}

// Helper: Can we place M cows such that they are at least 'minDistance' apart?
private boolean canPlaceCows(int[] A, int M, int minDistance) {
    int cowsPlaced = 1;
    int lastPlacedStall = A[0]; // Always optimal to place the first cow in the first stall!
    
    for (int i = 1; i < A.length; i++) {
        // If the gap to the current stall is >= our required minDistance
        if (A[i] - lastPlacedStall >= minDistance) {
            cowsPlaced++;
            lastPlacedStall = A[i];
            
            if (cowsPlaced == M) return true; // Successfully placed all cows!
        }
    }
    return false; // Ran out of stalls before placing all cows
}
```
**Time Complexity:** `O(N * log(Max_Distance))`

---

## Common Observation for BS on Answer Space:
1. Identify the **Search Space** (Usually some range of values like Distance, Time, Speed, Capacity).
2. Write a **Validation Helper Function** (`isPossible(mid)`).
3. Decide how to adjust `l` and `r`. 
   * If trying to **Maximize** an answer (like Cows distance): When valid, save and push `l = mid + 1`.
   * If trying to **Minimize** an answer (like Painters time): When valid, save and push `r = mid - 1`.

---

## 3. Find Smallest Again
**Problem:** Given an integer array $A$ of size $N$. If we store the sum of each triplet of the array $A$ in a new list, then find the $B$-th smallest element among the list.

**Key Idea:** This is Binary Search on Answer Space + Two Pointers.
Instead of generating all $O(N^3)$ triplets, we guess the answer (`mid` sum) and count how many triplets have a sum $\le$ `mid` using Two Pointers.
*   If `count >= B`, this `mid` sum could be our $B$-th smallest, but a smaller sum might also have `count >= B`. We save and try finding a smaller valid sum.
*   If `count < B`, we need a larger sum to reach the $B$-th position.

**Search Space:**
*   Minimum Possible Sum (`low`) = `A[0] + A[1] + A[2]` (smallest 3 elements after sorting).
*   Maximum Possible Sum (`high`) = `A[N-1] + A[N-2] + A[N-3]` (largest 3 elements).

```java
public int solve(int[] A, int B) {
    Arrays.sort(A);
    int n = A.length;
    
    int low = A[0] + A[1] + A[2];
    int high = A[n - 1] + A[n - 2] + A[n - 3];
    int ans = high;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (countTriplets(A, mid) >= B) {
            ans = mid;
            high = mid - 1; // Try to minimize the sum
        } else {
            low = mid + 1;  // Try to increase the sum
        }
    }
    return ans;
}

private int countTriplets(int[] A, int targetSum) {
    int count = 0;
    int n = A.length;
    
    // Fix the first element A[i]
    for (int i = 0; i < n - 2; i++) {
        int j = i + 1; // Left pointer
        int k = n - 1; // Right pointer
        
        while (j < k) {
            if (A[i] + A[j] + A[k] <= targetSum) {
                count += (k - j); // All elements from j+1 to k are valid with A[i] and A[j]
                j++;
            } else {
                k--; // Sum too large, shrink from the right
            }
        }
    }
    return count;
}
```
**Time Complexity:** `O(N * log(N) + N^2 * log(MaxSum))`
