# Queues and Deque Data Structure Theory Guide

A **Queue** is a linear data structure that stores information in a sequence, following the **FIFO (First In First Out)** principle. The item that has been inserted first into the queue will be the first one to be removed.

## Real-World Examples & Applications
- **Ticket Counter Queue**: The first person entering the line will get the ticket first.
- **Call Centre**: Incoming calls are placed in a queue and handled by the first available agent.

## Core Operations

1. **`enqueue(x)` / `push(x)`**: Adds an element `x` to the rear (back) of the queue.
2. **`dequeue()` / `pop()`**: Removes the element from the front of the queue and returns it.
3. **`front()` / `peek()`**: Returns the element at the front of the queue without removing it.
4. **`rear()`**: Returns the element at the back of the queue.
5. **`isEmpty()`**: Returns a boolean indicating whether the queue has no elements.

*Standard TC (Time Complexity) for all these operations is **O(1)**.*

## Implementation

### 1. Implementation using Arrays
- We maintain two pointers: `front` and `rear`.
- When `enqueue` is called, we add the item at `rear` and increment `rear`.
- When `dequeue` is called, we return the item at `front` and increment `front`.
- *Note:* It is important to handle boundary conditions and perhaps use circular arrays to reuse space when elements are dequeued.

### 2. Implementation using Linked Lists
- We maintain `head` (front) and `tail` (rear) pointers.
- **`enqueue(x)`**: Insert an element at the `tail` node.
- **`dequeue()`**: Remove an element from the `head` node.
- Keeping a reference to both `head` and `tail` allows insertions and deletions in **O(1)**.

### 3. Implementation using 2 Stacks
- We can implement a Queue using two Stacks (`st1` and `st2`).
- **`enqueue(x)`**: Simply push to `st1`. This is an **O(1)** operation.
- **`dequeue()`**:
  - If `st2` is empty, pop all elements from `st1` and push them to `st2`.
  - Then pop the top element from `st2`.
  - Though moving elements takes **O(N)**, the amortized time complexity across multiple `dequeue` operations acts as **O(1)**.

---

## Deque (Double-Ended Queue)
A **Deque** is a generalized version of a queue that allows insertion and deletion from both ends (front and rear).

- Can be implemented using a **Doubly Linked List (DLL)** or a **Dynamic Array**.
- Supports operations like `insertFront()`, `insertBack()`, `removeFront()`, and `removeBack()`, all in **O(1)** time complexity.

## Advanced Patterns & Common Problems

### 1. First A Positive Integers containing specific digits
**Problem**: Given an integer A, generate the first A positive integers that contain only digits 1, 2, and 3. (e.g., A=13 => 1, 2, 3, 11, 12, 13, 21, 22,...)
- **Approach**: 
  - Push the base digits (1, 2, 3) into a queue.
  - While we still need items, `dequeue` the front element (say `X`).
  - Append digits 1, 2, 3 to `X` (yielding `X1`, `X2`, `X3`), add them to the answer, and `enqueue` them back into the queue.

### 2. Sliding Window Maximum (Maximum of all subarrays of size K)
**Problem**: Given an array of integers and a window size `K`, find the maximum element in each contiguous subarray of size `K`.
- **Brute Force**: Iterate over all windows of size `K`. Time Complexity: **O(N * K)**.
- **Optimal (Deque-based)**:
  - We use a Deque to store the indices of useful elements for the current window.
  - Useful elements are those logically larger than newly encountered elements. We maintain a strictly decreasing sequence inside the Deque.
  - While adding a new element `arr[i]`, we remove all elements from the `back` of the deque that are smaller than `arr[i]`.
  - Add `i` to the `back`.
  - Remove elements from the `front` of the deque that are outside the current window (`i - K`).
  - The `front` of the Deque will always contain the maximum for the current window!
  - Time Complexity: **O(N)**. Space Complexity: **O(K)**.

### 3. Sum of Minimum and Maximum of all subarrays of size K
- An extension to the sliding window maximum problem.
- Maintain **two Deques**:
  - `max_dq` storing elements in logically decreasing order to find the max of the window.
  - `min_dq` storing elements in logically increasing order to find the min of the window.
- Extract `front`s from both deques for every window, add them to the total sum.
