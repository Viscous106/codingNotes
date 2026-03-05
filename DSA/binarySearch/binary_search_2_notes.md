# Binary Search Part 2: Quick Revision Notes

These notes are optimized for quick pre-exam revision, covering the slightly more advanced patterns and concepts from the Binary Search 2 module.

## 1. Single Element in a Sorted Array
**Problem:** Every element in a sorted array occurs exactly twice, except for one element which appears once. Find the unique element. Duplicate elements sit right next to each other.

**Key Idea:** Because duplicates occur in pairs, the index structure depends entirely on whether we have passed the unique element yet. The unique element disrupts the pair alignment!
* **Before Unique Element:** Pairs sit at `(Even, Odd)` indices. Example: `A[0]==A[1]`, `A[2]==A[3]`.
* **After Unique Element:** Pairs sit at `(Odd, Even)` indices. Example: `A[5]==A[6]`.

```java
public int singleNonDuplicate(int[] A) {
    int n = A.length;
    // Base Cases
    if (n == 1) return A[0];
    if (A[0] != A[1]) return A[0];
    if (A[n - 1] != A[n - 2]) return A[n - 1];

    int l = 1, r = n - 2;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        
        // Target found
        if (A[mid] != A[mid - 1] && A[mid] != A[mid + 1]) {
            return A[mid];
        }

        // We are before the single element (Pairs are Even-Odd)
        if ((mid % 2 == 0 && A[mid] == A[mid + 1]) || (mid % 2 == 1 && A[mid] == A[mid - 1])) {
            l = mid + 1; // Uniqueness is to the right
        } else {
            r = mid - 1; // Uniqueness is to the left
        }
    }
    return -1;
}
```
**Time Complexity:** `O(log N)`

---

## 2. Search in Rotated Sorted Array
**Problem:** An initially sorted array of distinct elements is rotated at some unknown pivot. Search efficiently for a target `K`.

**Key Idea:** The array is no longer strictly sorted, but if you split it down the middle, **at least one half will always be perfectly sorted**. 

```java
public int searchRotated(int[] A, int K) {
    int l = 0, r = A.length - 1;
    
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (A[mid] == K) return mid;
        
        // 1. Is the Left Half strictly sorted?
        if (A[l] <= A[mid]) {
            // Is K within this sorted half?
            if (K >= A[l] && K < A[mid]) {
                r = mid - 1; // It must be here
            } else {
                l = mid + 1; // It must be in the OTHER half
            }
        } 
        // 2. Otherwise, the Right Half must be strictly sorted!
        else {
            // Is K within this sorted half?
            if (K > A[mid] && K <= A[r]) {
                l = mid + 1; // It must be here
            } else {
                r = mid - 1; // It must be in the OTHER half
            }
        }
    }
    return -1;
}
```

---

## 3. Painter's Partition Problem
**Problem:** Given $N$ boards of different lengths and $P$ painters, find the minimum time required to paint all boards such that the time is minimized. (Painters work on continuous segments, taking 1 min per unit length).

**Key Idea:** Instead of trying to assign painters to boards directly, we do **Binary Search on the Answer Space** (the amount of Time).

```java
public int paint(int P, int[] C) {
    long l = 0;       // Max single board (Minimum possible answer)
    long r = 0;       // Sum of all boards (Maximum possible answer)
    
    for (int board : C) {
        l = Math.max(l, board);
        r += board;
    }
    
    long ans = r; // Default to max time
    
    while (l <= r) {
        long mid = l + (r - l) / 2; // Mid represents amount of TIME
        
        // If we can finish in 'mid' time
        if (isPossible(C, P, mid)) {
            ans = mid;      // Record potential answer
            r = mid - 1;    // Try to find a FASTER time
        } else {
            l = mid + 1;    // Time too short, need MORE time
        }
    }
    return (int) ans;
}

// Helper: Checks if all boards can be painted in 'maxTime' using 'P' painters
private boolean isPossible(int[] C, int P, long maxTime) {
    int paintersUsed = 1;
    long timeTakenByCurrent = 0;
    
    for (int i = 0; i < C.length; i++) {
        timeTakenByCurrent += C[i];
        
        // If adding this board exceeds time limit, assign to NEXT painter
        if (timeTakenByCurrent > maxTime) {
            paintersUsed++;
            timeTakenByCurrent = C[i]; 
            
            // If we ran out of painters, it's impossible in this 'maxTime'
            if (paintersUsed > P) return false;
        }
    }
    return true;
}
```

---

## 4. Integer Square Root
**Problem:** Find the integer part of the square root of $N$ without built-in functions. (Floor value).

```java
public int floorSqrt(int N) {
    if (N == 0 || N == 1) return N;
    
    long l = 1, r = N; // Search space is 1 to N
    long ans = 1;      // Default safe floor answer
    
    while (l <= r) {
        long mid = l + (r - l) / 2;
        
        // Safest approach against integer overflow: mid * mid <= N
        if (mid * mid <= N) {
            ans = mid;      // Valid floor root
            l = mid + 1;    // Try to find a LARGER valid root
        } else {
            r = mid - 1;    // 'mid' is too big, search smaller numbers
        }
    }
    return (int) ans;
}
```
