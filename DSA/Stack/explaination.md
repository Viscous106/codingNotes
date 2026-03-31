# Stack Data Structure Theory Guide

A **Stack** is a linear data structure that stores information in a sequence, from bottom to top. It follows a specific order in which the operations are performed. The principle it follows is **LIFO (Last In First Out)**.

The items can only be accessed from the top and new elements can only be added to the top.

## Real-World Examples & Applications
- **Stack of Plates / Chairs**: The last plate placed on the stack is the first one removed.
- **Undo/Redo Mechanisms**: 
  - `Undo()` removes the last change made (reverse the most recent editing action).
  - `Redo()` brings back an action that was undone.
  - Used in text editors, IDEs, browsers (back/forward history), Photoshop, etc.

## Core Operations

1. **`push(x)`**: Adds an element `x` to the top of the stack.
2. **`pop()`**: Removes the element from the top of the stack and returns it.
3. **`top()` / `peek()`**: Returns the element at the top of the stack without removing it.
4. **`isEmpty()`**: Returns a boolean indicating whether the stack has no elements.

*Standard TC (Time Complexity) for all these operations is **O(1)**.*

## Implementation

### 1. Implementation using Dynamic Arrays
- Arrays can be used to implement stacks where the end of the array acts as the top of the stack.
- `push(x)` operation is essentially an `addLast(x)` operation.
- `pop()` operation corresponds to `removeLast()`.
- `peek()` is `getLast()`.

### 2. Implementation using Linked Lists
- A stack can also be efficiently implemented with a Linked List.
- To maintain **O(1)** time complexity, we add and remove items at the **head (front)** of the linked list.
- `push(x)` corresponds to `addFront(x)`.
- `pop()` corresponds to `removeFront()`.
- `peek()` is `getFront()` (returns the value at the head node).

## Advanced Patterns & Common Problems

### 1. Balanced Parentheses
Using a stack to check if a sequence of parentheses (like `[](){}`) is valid.
- We iterate through the string of brackets.
- Whenever we see an 'open' bracket (`(`, `{`, `[`), we push it onto the stack.
- When we encounter a 'closed' bracket, we pop the top of the stack. If the popped item perfectly matches the type of the closing bracket, we continue. Otherwise, it is invalid.
- At the end of the sequence, if the stack is empty, the parentheses are perfectly balanced!

### 2. Evaluate Postfix Expression
Evaluating mathematical expressions written in postfix notation (e.g., `2 3 5 * +`).
- Iterate over the expression.
- Push operands (numbers) onto the stack.
- When an operator (like `+, -, *, /`) is encountered, pop the top two operands from the stack, apply the operator, and push the result back onto the stack.

### 3. Monotonic Stacks (Next Greater / Smaller Elements)
A technique to find the nearest element under specific constraints in **O(N)** time using a stack that guarantees elements in an increasing or decreasing order.
  
- **Nearest Smaller Element (NSE)**: Find the nearest smaller element on the left side of every element in an array. We maintain an increasing stack. If an incoming element is smaller than the top of the stack, we iteratively pop the stack, removing greater or equal items. Then we record the new top as the answer and push the new item.
- **Nearest Greater Element (NGE) / Next Greater Element**: Similar to NSE, but maintaining a decreasing stack to find the nearest larger element on the right/left.

### 4. Largest Rectangle in Histogram
A classic advanced stack problem. Given heights of bars in a histogram, we calculate the maximum continuous rectangular area.
- This merges both **Left NSE** and **Right NSE** concepts.
- `area = height[i] * (RightNSE_index - LeftNSE_index - 1)`. 
- By precalculating Left and Right NSE for all indices in the histogram using a Stack, we solve this in **O(N)**.
