# Binary Search Part 1: Quick Revision Notes

These notes are optimized for quick pre-exam revision, covering all key patterns and concepts from the Binary Search 1 module.

## 1. Introduction to Searching
* **Search Space**: Finding an item efficiently depends heavily on the structure of the space.
* **Linear Search**: Scans element by element.
  * **Time Complexity**: **O(N)**.
  * A brute-force search space (e.g., $N=240,000$ takes up to $240,000$ comparisons).
* **Binary Search**: Used for **monotonic** (sorted/increasing/decreasing) conditions. At each step, we discard exactly **half** the search space.
  * **Time Complexity**: **O(log N)** (e.g., $N=240,000$ takes only $\approx 18$ comparisons).
  * **Space Complexity**: **O(1)**.

---

## 2. Standard Search (Distinct Elements)
**Problem:** Find index of element `K` in a sorted array of unique elements.

**Core Formula**: Always compute `mid` securely to avoid integer overflow:
```java
int mid = l + (r - l) / 2;
```

**Conditions:**
* `A[mid] == K` $\rightarrow$ Return `mid`.
* `A[mid] < K` $\rightarrow$ The element must be to the right, so `l = mid + 1`.
* `A[mid] > K` $\rightarrow$ The element must be to the left, so `r = mid - 1`.

---

## 3. First and Last Occurrence (Repeated Elements)
**Problem:** Find the *first* or *last* index of element `K` in a sorted array with duplicates.

**Key Idea:** Finding `K` doesn't mean you stop. You record the index as a potential answer and keep pushing in the direction you want!
* **First Occurrence**: Once found, save `ans = mid` but keep searching **left** (`r = mid - 1`) because an earlier occurrence might exist.
* **Last Occurrence**: Once found, save `ans = mid` but keep searching **right** (`l = mid + 1`) because a later occurrence might exist.

```java
// Logic for First Occurrence 
int firstOccurrence(int[] arr, int K) {
    int l = 0, r = arr.length - 1;
    int ans = -1;
    while(l <= r) {
        int mid = l + (r - l) / 2;
        if(arr[mid] == K) {
            ans = mid;       // Potential answer
            r = mid - 1;     // Push Left!
        } else if(arr[mid] < K) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return ans;
}
```

---

## 4. Find Peak Element (Mountain Array)
**Problem:** Array increases strictly and then decreases strictly. Find the maximum element (the peak).

**Key Idea:** Look at the slope formed by adjacent elements to know which half the peak lies in. Base condition: `A[mid]` is greater than *both* neighbors $\rightarrow$ Peak!
* **Increasing Slope**: `A[mid] > A[mid - 1]` $\rightarrow$ The peak must be further **right**, so move `l = mid + 1`.
* **Decreasing Slope**: `A[mid] < A[mid - 1]` $\rightarrow$ The peak must be further **left**, so move `r = mid - 1`.

---

## 5. Find Any Local Minima
**Problem:** Array of distinct elements. Find *any* element smaller than its adjacent neighbors. (Corner elements only check 1 inner neighbor).

**Key Idea:** You are guaranteed a local minima if you always walk "down" the slope!
1. **Check Corners First** (Base cases):
   * If `A[0] < A[1]` $\rightarrow$ Return `0`.
   * If `A[N-1] < A[N-2]` $\rightarrow$ Return `N-1`.
2. **Binary Search Middle Elements (`l = 1`, `r = N - 2`)**:
   * If `A[mid] < A[mid - 1]` AND `A[mid] < A[mid + 1]` $\rightarrow$ Found local minima, return `mid`.
   * **Dip goes left**: If `A[mid] > A[mid - 1]`, curve dips left $\rightarrow$ min lies **left**, so `r = mid - 1`.
   * **Dip goes right**: If `A[mid] > A[mid + 1]`, curve dips right $\rightarrow$ min lies **right**, so `l = mid + 1`.
