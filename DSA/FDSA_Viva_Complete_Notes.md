# FDSA Viva — Complete Notes (Zero to Confident)

> **How to use this file:** Read top to bottom. Every topic starts from *"what even is this"* and builds up to code + complexity + viva questions. If you've never touched a topic, you can still follow it. Boxes marked **🎤 VIVA** are the questions examiners actually ask.

**Topics covered:** Bit Manipulation · Binary Search · Hashing · Linked List · Stack · Queue · Binary Tree

---

## Table of Contents
1. [Foundations You Must Know First](#0-foundations)
2. [Bit Manipulation](#1-bit-manipulation)
3. [Binary Search](#2-binary-search)
4. [Hashing](#3-hashing)
5. [Linked List](#4-linked-list)
6. [Stack](#5-stack)
7. [Queue](#6-queue)
8. [Binary Tree](#7-binary-tree)
9. [Rapid-Fire Cross-Topic Q&A](#8-rapid-fire)
10. [LeetCode Practice Problems](#9-leetcode)
11. [Last-Minute Cheat Sheet](#10-cheat-sheet)

---

<a name="0-foundations"></a>
## 0. Foundations You Must Know First

Before any topic, understand these — they come up in *every* viva.

### What is a Data Structure?
A **way of organizing data** in memory so it can be used efficiently. Example: an array, a linked list, a tree.

### What is an Algorithm?
A **step-by-step procedure** to solve a problem. Example: binary search is an algorithm; the sorted array it runs on is a data structure.

### Time & Space Complexity (Big-O)
**Big-O** describes how the running time (or memory) **grows as input size `n` grows**. We care about the worst case.

| Notation | Name | Meaning | Example |
|----------|------|---------|---------|
| O(1) | Constant | Same time regardless of n | Accessing `arr[5]` |
| O(log n) | Logarithmic | Halves each step | Binary search |
| O(n) | Linear | Grows with n | Loop through array |
| O(n log n) | Linearithmic | Good sorts | Merge sort |
| O(n²) | Quadratic | Nested loops | Bubble sort |

> **🎤 VIVA — Why Big-O and not seconds?**
> Because actual seconds depend on hardware. Big-O measures *growth*, which is machine-independent and tells us how the algorithm scales.

> **🎤 VIVA — Time vs Space complexity?**
> Time = how many operations. Space = how much extra memory the algorithm uses (beyond the input).

---

<a name="1-bit-manipulation"></a>
## 1. Bit Manipulation

### 1.1 What is it?
Every number in a computer is stored in **binary** — a sequence of **bits** (0s and 1s). **Bit manipulation** means directly changing/reading those bits using special operators. It's used because these operations are **extremely fast** (done by the CPU in a single step).

**Binary basics:**
- `5` in binary = `101` → (1×4) + (0×2) + (1×1) = 5
- `3` in binary = `011`
- Rightmost bit = "least significant bit" (LSB). Leftmost = "most significant bit" (MSB).

### 1.2 The Bitwise Operators

| Operator | Symbol | What it does |
|----------|--------|--------------|
| AND | `&` | 1 only if **both** bits are 1 |
| OR | `\|` | 1 if **at least one** bit is 1 |
| XOR | `^` | 1 if bits are **different** |
| NOT | `~` | Flips every bit |
| Left shift | `<<` | Shifts bits left (adds 0s on right) |
| Right shift | `>>` | Shifts bits right |

**Worked examples** (using 5 = `101`, 3 = `011`):
```
  101   (5)          101   (5)          101   (5)
& 011   (3)        | 011   (3)        ^ 011   (3)
-----              -----              -----
  001 = 1            111 = 7            110 = 6
 (AND)               (OR)               (XOR)
```

**Shifts are multiply/divide by powers of 2:**
- `5 << 1` = `1010` = 10  (multiplied by 2)
- `5 << 2` = `10100` = 20 (multiplied by 4)
- `5 >> 1` = `10` = 2  (divided by 2, drops remainder)

### 1.3 The Essential Tricks (memorize these)

```c
// Check if i-th bit is set (1) or not
(n >> i) & 1        // gives 1 if set, 0 if not

// Set the i-th bit to 1
n = n | (1 << i)

// Clear the i-th bit to 0
n = n & ~(1 << i)

// Toggle (flip) the i-th bit
n = n ^ (1 << i)

// Check odd or even
n & 1               // 1 = odd, 0 = even

// Swap two numbers WITHOUT a temp variable
a = a ^ b;
b = a ^ b;
a = a ^ b;
```

**The two famous power-tricks:**

**(a) `n & (n-1)` removes the lowest set bit.**
```
n     = 12 = 1100
n-1   = 11 = 1011
n&(n-1)=      1000 = 8   (the lowest 1 got removed)
```
- If `n & (n-1) == 0` (and n > 0) → **n is a power of 2** (because powers of 2 have exactly one set bit).
- Repeatedly doing this **counts set bits** (Brian Kernighan's algorithm).

**(b) XOR to find the unique element.**
If every element appears twice except one, XOR them all → the answer.
Why? `x ^ x = 0` and `x ^ 0 = x`. All pairs cancel out, leaving the single one.
```
arr = [4, 1, 2, 1, 2]
4^1^2^1^2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4
```

### 1.4 XOR Properties (very commonly asked)
- `a ^ a = 0`
- `a ^ 0 = a`
- Commutative: `a ^ b = b ^ a`
- Associative: `(a^b)^c = a^(b^c)`

### 1.5 Signed Numbers — 2's Complement
Negative numbers are stored using **2's complement**: flip all bits and add 1.
- `~n = -(n+1)` → so `~5 = -6`.
- This is why `NOT` gives "weird" negative results.

> **🎤 VIVA QUESTIONS**
> - **Why is bit manipulation fast?** → Operations happen at hardware level in a single CPU cycle.
> - **How to check if a number is a power of 2?** → `n > 0 && (n & (n-1)) == 0`.
> - **What does XOR of a number with itself give?** → 0.
> - **Difference between `<<` and `>>`?** → Left shift multiplies by 2, right shift divides by 2.
> - **How to swap without a third variable?** → Using XOR (shown above).
> - **What is 2's complement?** → A way to represent negative numbers: invert bits and add 1.
> - **Count set bits efficiently?** → Brian Kernighan: `while(n){ n = n & (n-1); count++; }` — runs only as many times as there are set bits.

---

<a name="2-binary-search"></a>
## 2. Binary Search

### 2.1 What is it?
A method to find an element in a **sorted** array by **repeatedly halving** the search area. Instead of checking every element (linear, O(n)), you eliminate half the array each step → **O(log n)**.

**Analogy:** Finding a word in a dictionary. You don't read page by page — you open the middle, decide left or right half, repeat.

### 2.2 How it works (step by step)
Array must be **sorted**. Keep two pointers: `low` (start) and `high` (end).
1. Find middle: `mid = low + (high - low)/2`.
2. If `arr[mid] == key` → found it.
3. If `arr[mid] < key` → key is in the right half → `low = mid + 1`.
4. If `arr[mid] > key` → key is in the left half → `high = mid - 1`.
5. Repeat while `low <= high`. If loop ends → not found.

**Example:** search 7 in `[1, 3, 5, 7, 9, 11]`
```
low=0, high=5 → mid=2 → arr[2]=5 < 7 → go right, low=3
low=3, high=5 → mid=4 → arr[4]=9 > 7 → go left, high=3
low=3, high=3 → mid=3 → arr[3]=7 == 7 → FOUND at index 3 ✓
```

### 2.3 Code (Iterative — preferred)
```c
int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;   // avoids overflow
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;   // not found
}
```

### 2.4 Code (Recursive)
```c
int binarySearch(int arr[], int low, int high, int key) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == key) return mid;
    else if (arr[mid] < key)
        return binarySearch(arr, mid + 1, high, key);
    else
        return binarySearch(arr, low, mid - 1, key);
}
```

### 2.5 Why `mid = low + (high - low)/2`?
If you write `(low + high)/2` and both are large, `low + high` can **overflow** the integer limit. The subtraction form avoids this. **This is a favorite viva question.**

### 2.6 Complexity
- **Time:** O(log n) — halves each step. Recurrence: `T(n) = T(n/2) + O(1)`.
- **Space:** O(1) iterative; **O(log n)** recursive (function call stack).

### 2.7 Variants to name
- First / last occurrence of a repeated element.
- Lower bound / upper bound.
- Search in a **rotated** sorted array.
- **Binary search on the answer** (e.g., finding square root, or minimum value satisfying a condition).

> **🎤 VIVA QUESTIONS**
> - **Precondition for binary search?** → Array must be **sorted**.
> - **Time complexity and why?** → O(log n), because search space halves each step.
> - **Why `low + (high-low)/2`?** → Prevents integer overflow.
> - **Iterative vs recursive space?** → O(1) vs O(log n) (call stack).
> - **Can binary search work on a linked list?** → Not efficiently — no O(1) access to the middle element; reaching mid takes O(n).
> - **Linear vs binary search?** → Linear: O(n), works on unsorted. Binary: O(log n), needs sorted.
> - **Worst case?** → Element not present, or found after full halving → O(log n).

---

<a name="3-hashing"></a>
## 3. Hashing

### 3.1 What is it?
**Hashing** stores data so you can find it in **O(1) average time** (instantly, on average). It uses a **hash function** to convert a *key* into an *index* of an array (called a **hash table**).

**Analogy:** A library assigns each book a shelf number based on its title. Instead of scanning every shelf, you compute the number and go straight there.

### 3.2 Key Terms
- **Hash Table:** the array that stores the data.
- **Hash Function:** converts a key → an index. Example: `index = key % table_size`.
- **Collision:** when two different keys produce the **same** index.
- **Load Factor (α):** `number_of_entries / table_size`. Tells how "full" the table is. Higher α → more collisions.

**Example hash function** (table size 10):
```
key=25 → 25 % 10 = 5  → store at index 5
key=15 → 15 % 10 = 5  → COLLISION! also wants index 5
```

### 3.3 Collision Resolution (THE most important part)

Two main strategies:

**(A) Chaining (Open Hashing)**
Each slot in the table holds a **linked list**. Colliding elements are appended to the list at that index.
```
index 5 → [25] → [15] → [35]     (all hashed to 5, chained together)
```
- ✅ Table never "fills up", simple to implement.
- ❌ Extra memory for pointers; poor cache performance.

**(B) Open Addressing (Closed Hashing)**
All elements stay **inside the array**. On collision, probe for the next empty slot.
- **Linear Probing:** try `(hash + 1) % size`, `(hash + 2) % size`, ... 
  - Problem: **primary clustering** (long runs of filled slots).
- **Quadratic Probing:** try `(hash + 1²)`, `(hash + 2²)`, `(hash + 3²)` ... reduces clustering.
- **Double Hashing:** use a **second hash function** to decide the step size → best distribution.

### 3.4 Rehashing
When load factor gets too high (~0.7), the table is **resized** (usually doubled) and all elements **re-inserted** (rehashed). This keeps operations fast.

### 3.5 Complexity
| Case | Time |
|------|------|
| Average (good hash) | **O(1)** |
| Worst (all collide) | **O(n)** |

### 3.6 Properties of a Good Hash Function
- **Uniform distribution** (spreads keys evenly).
- **Fast** to compute.
- **Deterministic** (same key → same index always).
- **Minimizes collisions**.

### 3.7 Real-World Uses
Dictionaries / maps / `HashMap`, database **indexing**, **caches**, symbol tables in compilers, password storage (cryptographic hashing).

> **🎤 VIVA QUESTIONS**
> - **What is a collision?** → Two keys mapping to the same index.
> - **How do you resolve collisions?** → Chaining or open addressing (linear/quadratic probing, double hashing).
> - **Chaining vs open addressing?** → Chaining uses linked lists (extra memory, no clustering); open addressing stays in the array (cache-friendly but suffers clustering).
> - **What is load factor? Ideal value?** → entries/size; kept around 0.7, else rehash.
> - **Worst-case time of hashing?** → O(n), when all keys collide into one slot.
> - **What makes a good hash function?** → Uniform, fast, deterministic, few collisions.
> - **Difference between hashing and direct addressing?** → Direct addressing needs one slot per possible key (huge memory); hashing maps a big key space into a small table.

---

<a name="4-linked-list"></a>
## 4. Linked List

### 4.1 What is it?
A **linear** data structure made of **nodes**. Each node stores **data** + a **pointer (address)** to the next node. Unlike an array, nodes are **not** stored in contiguous memory — they're linked by pointers.

```
[data|next] -> [data|next] -> [data|next] -> NULL
   Head                                      (end)
```

**Why use it?** Arrays have a **fixed size** and inserting/deleting in the middle requires **shifting** elements. Linked lists **grow/shrink dynamically** and insert/delete without shifting.

### 4.2 Node Structure
```c
struct Node {
    int data;
    struct Node* next;
};
```

### 4.3 Types
- **Singly Linked List:** each node points to the **next** only. One-directional.
- **Doubly Linked List:** each node has **prev** and **next** pointers → can traverse both ways.
- **Circular Linked List:** the last node points back to the **head** (forms a loop).

```
Singly:   A -> B -> C -> NULL
Doubly:   NULL <- A <-> B <-> C -> NULL
Circular: A -> B -> C --+
          ^-------------+
```

### 4.4 Array vs Linked List (asked in almost every viva)
| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory | Contiguous | Scattered (pointers) |
| Size | Fixed | Dynamic |
| Access by index | **O(1)** random | **O(n)** sequential |
| Insert/Delete (middle) | O(n) (shifting) | **O(1)** if node is known |
| Extra memory | None | Pointer per node |
| Cache performance | Good | Poor |

### 4.5 Complexities
- Insert/delete at **head**: **O(1)**
- Insert/delete at **tail**: O(n) singly (O(1) if you keep a tail pointer)
- **Search / access by position**: **O(n)**

### 4.6 Must-Know Operations

**Traversal:**
```c
void traverse(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
```

**Insert at head:**
```c
struct Node* insertAtHead(struct Node* head, int value) {
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = head;   // point to old head
    return newNode;         // new node becomes head
}
```

**Reverse a linked list** (3-pointer technique — VERY common):
```c
struct Node* reverse(struct Node* head) {
    struct Node *prev = NULL, *curr = head, *next = NULL;
    while (curr != NULL) {
        next = curr->next;   // save next
        curr->next = prev;   // reverse the link
        prev = curr;         // move prev forward
        curr = next;         // move curr forward
    }
    return prev;             // prev is the new head
}
```

### 4.7 Floyd's Cycle Detection (slow/fast pointer)
To detect a **loop** in a linked list, use two pointers: `slow` moves 1 step, `fast` moves 2 steps. If they ever **meet**, there's a cycle. If `fast` reaches NULL, no cycle. (Also called **tortoise and hare**.)
```c
int hasCycle(struct Node* head) {
    struct Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return 1;   // cycle found
    }
    return 0;
}
```
The same slow/fast idea also **finds the middle** of a list (when fast reaches the end, slow is at the middle).

> **🎤 VIVA QUESTIONS**
> - **Advantage over arrays?** → Dynamic size, O(1) insert/delete without shifting.
> - **Disadvantages?** → No random access (O(n) to reach an element), extra pointer memory, poor cache locality.
> - **How to detect a loop?** → Floyd's cycle detection (slow & fast pointers).
> - **Singly vs doubly?** → Doubly allows backward traversal and easier deletion, but uses extra memory per node.
> - **Can you binary-search a linked list?** → No efficient way — no O(1) access to the middle.
> - **How to reverse a linked list?** → Iteratively with prev/curr/next pointers.
> - **How to find the middle?** → Slow/fast pointer.

---

<a name="5-stack"></a>
## 5. Stack

### 5.1 What is it?
A linear structure following **LIFO** — **Last In, First Out**. The last item you put in is the first one you take out. All action happens at **one end**, called the **top**.

**Analogy:** A stack of plates. You add to the top and remove from the top.

```
   | 30 |  <- top (last in, first out)
   | 20 |
   | 10 |  <- bottom (first in)
   ------
```

### 5.2 Operations (all O(1))
| Operation | Meaning |
|-----------|---------|
| `push(x)` | Add x to the top |
| `pop()` | Remove & return the top |
| `peek()` / `top()` | Look at top without removing |
| `isEmpty()` | Check if stack is empty |
| `isFull()` | (array impl) Check if full |

### 5.3 Array Implementation
```c
#define SIZE 100
int stack[SIZE];
int top = -1;               // -1 means empty

void push(int x) {
    if (top == SIZE - 1) { printf("Overflow"); return; }
    stack[++top] = x;
}
int pop() {
    if (top == -1) { printf("Underflow"); return -1; }
    return stack[top--];
}
```

### 5.4 Overflow & Underflow
- **Stack Overflow:** trying to `push` onto a **full** stack.
- **Stack Underflow:** trying to `pop` from an **empty** stack.

### 5.5 Applications (memorize this list!)
- **Function calls & recursion** — the **call stack** stores each function's frame.
- **Expression conversion** — infix → postfix / prefix.
- **Expression evaluation** — postfix evaluation.
- **Balanced parentheses** checking `{[()]}`.
- **Undo/Redo** in editors.
- **Backtracking** — mazes, DFS.
- **Browser back button** / history.

### 5.6 Why Postfix? (common question)
Infix (`a + b * c`) needs **precedence rules and parentheses**. Postfix (`a b c * +`) can be evaluated left-to-right using a stack with **no parentheses needed** → easier for machines.

**Balanced parentheses logic:** push every opening bracket; on a closing bracket, pop and check it matches. At the end, stack must be empty.

> **🎤 VIVA QUESTIONS**
> - **What is LIFO?** → Last In First Out; the stack principle.
> - **Overflow vs underflow?** → Push on full vs pop on empty.
> - **Real-life example?** → Stack of plates, browser history, undo.
> - **How does recursion use a stack?** → Each call pushes a frame (parameters, local vars, return address); returning pops it.
> - **Which DS converts infix to postfix?** → Stack (holds operators).
> - **Can you implement a stack using queues?** → Yes (classic trick — using two queues).
> - **Applications of stack?** → (list above).

---

<a name="6-queue"></a>
## 6. Queue

### 6.1 What is it?
A linear structure following **FIFO** — **First In, First Out**. The first item added is the first removed. Insertion happens at the **rear**, deletion at the **front**.

**Analogy:** A line at a ticket counter. First person in line is served first.

```
front ->  [10][20][30]  <- rear
          out         in
```

### 6.2 Operations (O(1))
| Operation | Meaning |
|-----------|---------|
| `enqueue(x)` | Add x at the rear |
| `dequeue()` | Remove from the front |
| `front()` | See the front element |
| `rear()` | See the rear element |
| `isEmpty()` | Check if empty |

### 6.3 Types of Queues (IMPORTANT)
- **Simple / Linear Queue:** basic FIFO. **Problem:** after some dequeues, the front slots are wasted and can't be reused even if empty.
- **Circular Queue:** the rear **wraps around** to the front using `(rear + 1) % size`. Solves the wasted-space problem.
- **Priority Queue:** elements are served by **priority**, not arrival order. Usually implemented with a **heap**.
- **Deque (Double-Ended Queue):** insert and delete at **both** ends.

### 6.4 Circular Queue — Why?
In a linear queue, once `rear` reaches the end, you can't insert even if front slots are free (they got dequeued). A **circular queue** reuses those slots by wrapping around.

**Conditions (circular queue of size `n`):**
- **Full:** `(rear + 1) % n == front`
- **Empty:** `front == -1`

### 6.5 Simple Array Implementation
```c
#define SIZE 100
int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int x) {
    if (rear == SIZE - 1) { printf("Overflow"); return; }
    if (front == -1) front = 0;
    queue[++rear] = x;
}
int dequeue() {
    if (front == -1 || front > rear) { printf("Underflow"); return -1; }
    return queue[front++];
}
```

### 6.6 Applications
- **CPU scheduling**, **disk scheduling**.
- **BFS (Breadth-First Search)** in graphs and trees.
- **Printer spooling** (print jobs queued).
- **IO buffers**, handling requests in web servers.

### 6.7 Stack vs Queue
| | Stack | Queue |
|--|-------|-------|
| Principle | LIFO | FIFO |
| Ends used | One (top) | Two (front & rear) |
| Used in | Recursion, DFS | Scheduling, BFS |

> **🎤 VIVA QUESTIONS**
> - **What is FIFO?** → First In First Out; the queue principle.
> - **Why circular queue?** → To reuse empty front slots and avoid false overflow.
> - **Full/empty condition in circular queue?** → Full: `(rear+1)%n == front`; Empty: `front == -1`.
> - **Stack vs queue?** → LIFO one-end vs FIFO two-ends.
> - **What is a priority queue?** → Elements served by priority, implemented with a heap.
> - **What is a deque?** → Double-ended queue; insert/delete at both ends.
> - **Which traversal uses a queue?** → BFS / level-order.

---

<a name="7-binary-tree"></a>
## 7. Binary Tree

### 7.1 What is it?
A **hierarchical** (non-linear) data structure. Each **node** has at most **two children**: a **left** child and a **right** child. The top node is the **root**.

```
          1          <- root
        /   \
       2     3
      / \     \
     4   5     6      <- 4,5,6 are leaves
```

### 7.2 Key Terminology
- **Root:** topmost node.
- **Leaf:** node with **no children**.
- **Parent / Child:** direct relationships.
- **Edge:** link between two nodes.
- **Height of tree:** number of edges on the **longest path** from root to a leaf.
- **Depth of a node:** number of edges from the **root** to that node.
- **Degree:** number of children a node has.
- **Level:** root is level 0, its children level 1, etc.

**Useful formulas:**
- Max nodes at level `l` = **2^l**.
- Max nodes in a tree of height `h` = **2^(h+1) − 1**.

### 7.3 Types of Binary Trees
- **Full (Strict):** every node has **0 or 2** children (never just 1).
- **Complete:** all levels full except possibly the last, which fills **left to right**.
- **Perfect:** all internal nodes have 2 children **and** all leaves are at the **same level**.
- **Balanced:** height is kept ≈ **O(log n)** (e.g., AVL tree).
- **Skewed:** all nodes lean to one side (like a linked list) — worst case.

### 7.4 Binary Search Tree (BST) — special & important
A binary tree with an **ordering rule**:
> For every node: **left subtree < node < right subtree**.

This ordering lets you **search in O(log n)** (like binary search, but on a tree).
```
        8
       / \
      3   10
     / \    \
    1   6    14
```
Search for 6: 6<8 go left → 6>3 go right → found. ✓

### 7.5 Tree Traversals (BE ABLE TO WRITE THESE)

Traversal = the order in which you visit all nodes.

**Depth-First (use recursion / a stack):**
- **Inorder (Left, Root, Right):** For a **BST, gives sorted order!** ← examiners love this
- **Preorder (Root, Left, Right):** used to **copy/create** a tree.
- **Postorder (Left, Right, Root):** used to **delete** a tree (children before parent).

**Breadth-First:**
- **Level Order (level by level):** uses a **queue**.

**Code:**
```c
struct Node { int data; struct Node *left, *right; };

void inorder(struct Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);      // visit root between children
    inorder(root->right);
}
void preorder(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);      // visit root first
    preorder(root->left);
    preorder(root->right);
}
void postorder(struct Node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);      // visit root last
}
```

**Traversal example** on the tree in 7.1 (root=1):
- Inorder: `4 2 5 1 3 6`
- Preorder: `1 2 4 5 3 6`
- Postorder: `4 5 2 6 3 1`
- Level order: `1 2 3 4 5 6`

### 7.6 Complexity (BST)
| Operation | Balanced | Worst (skewed) |
|-----------|----------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

**Why worst case O(n)?** If you insert **already-sorted** data into a BST, it becomes a straight line (skewed) — just like a linked list. **Fix:** self-balancing trees (**AVL**, **Red-Black**).

### 7.7 Tree vs Graph
- **Tree:** connected, **no cycles**, exactly **n−1 edges** for n nodes, one root.
- **Graph:** can have cycles, multiple components, any number of edges.

> **🎤 VIVA QUESTIONS**
> - **Binary tree vs BST?** → BST has the ordering property (left < root < right); a plain binary tree has no ordering.
> - **Which traversal gives sorted output on a BST?** → **Inorder**.
> - **Which traversal is used to delete a tree?** → **Postorder** (delete children before parent).
> - **Which traversal to copy a tree?** → Preorder.
> - **Which DS does level-order use?** → **Queue**.
> - **Worst-case BST search and why?** → O(n), when the tree is skewed (sorted input).
> - **How to keep a BST balanced?** → Use AVL or Red-Black trees.
> - **Height of a balanced tree with n nodes?** → O(log n).
> - **Max nodes at level l?** → 2^l.
> - **Difference between tree and graph?** → Tree is acyclic & connected with n−1 edges; graph can have cycles.

---

<a name="8-rapid-fire"></a>
## 8. Rapid-Fire Cross-Topic Q&A

These get fired quickly to test breadth. Know them cold.

| Question | Answer |
|----------|--------|
| LIFO structure? | Stack |
| FIFO structure? | Queue |
| DS used by recursion? | Stack (call stack) |
| DS used by BFS / level-order? | Queue |
| DS used by DFS? | Stack (or recursion) |
| O(1) average lookup DS? | Hash table |
| Search a sorted array? | Binary search — O(log n) |
| Inorder traversal of a BST gives? | Sorted order |
| Detect a linked-list cycle? | Floyd's two-pointer |
| Check power of 2? | `n & (n-1) == 0` |
| Find the single unique element? | XOR everything |
| Reverse a linked list? | prev/curr/next pointers |
| Worst case of hashing? | O(n) |
| Worst case of BST? | O(n) (skewed) |
| Self-balancing trees? | AVL, Red-Black |
| Swap without temp variable? | XOR trick |

---

<a name="9-leetcode"></a>
## 9. LeetCode Practice Problems

> **Difficulty:** 🟢 Easy · 🟡 Medium · 🔴 Hard
> **Strategy for tonight:** do the 🟢 ones first (they cement the concept), then attempt 1–2 🟡 per topic. Don't chase 🔴 unless you're solid. **Start with the ⭐ starred ones — they map directly to your viva topics.**

### Bit Manipulation
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 136 | ⭐ Single Number (XOR trick) | 🟢 | https://leetcode.com/problems/single-number/ |
| 191 | ⭐ Number of 1 Bits (count set bits) | 🟢 | https://leetcode.com/problems/number-of-1-bits/ |
| 231 | ⭐ Power of Two (`n & (n-1)`) | 🟢 | https://leetcode.com/problems/power-of-two/ |
| 268 | Missing Number | 🟢 | https://leetcode.com/problems/missing-number/ |
| 338 | Counting Bits | 🟢 | https://leetcode.com/problems/counting-bits/ |
| 260 | Single Number III | 🟡 | https://leetcode.com/problems/single-number-iii/ |
| 371 | Sum of Two Integers (add without `+`) | 🟡 | https://leetcode.com/problems/sum-of-two-integers/ |

### Binary Search
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 704 | ⭐ Binary Search (the classic template) | 🟢 | https://leetcode.com/problems/binary-search/ |
| 35 | ⭐ Search Insert Position | 🟢 | https://leetcode.com/problems/search-insert-position/ |
| 69 | Sqrt(x) (binary search on answer) | 🟢 | https://leetcode.com/problems/sqrtx/ |
| 34 | ⭐ First & Last Position of Element | 🟡 | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 33 | Search in Rotated Sorted Array | 🟡 | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| 153 | Find Minimum in Rotated Sorted Array | 🟡 | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ |
| 875 | Koko Eating Bananas (search on answer) | 🟡 | https://leetcode.com/problems/koko-eating-bananas/ |

### Hashing
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 1 | ⭐ Two Sum (the most famous hashing problem) | 🟢 | https://leetcode.com/problems/two-sum/ |
| 217 | ⭐ Contains Duplicate | 🟢 | https://leetcode.com/problems/contains-duplicate/ |
| 242 | ⭐ Valid Anagram | 🟢 | https://leetcode.com/problems/valid-anagram/ |
| 349 | Intersection of Two Arrays | 🟢 | https://leetcode.com/problems/intersection-of-two-arrays/ |
| 49 | Group Anagrams | 🟡 | https://leetcode.com/problems/group-anagrams/ |
| 3 | Longest Substring Without Repeating Characters | 🟡 | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| 560 | Subarray Sum Equals K | 🟡 | https://leetcode.com/problems/subarray-sum-equals-k/ |
| 128 | Longest Consecutive Sequence | 🟡 | https://leetcode.com/problems/longest-consecutive-sequence/ |

### Linked List
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 206 | ⭐ Reverse Linked List (prev/curr/next) | 🟢 | https://leetcode.com/problems/reverse-linked-list/ |
| 141 | ⭐ Linked List Cycle (Floyd's) | 🟢 | https://leetcode.com/problems/linked-list-cycle/ |
| 876 | ⭐ Middle of the Linked List (slow/fast) | 🟢 | https://leetcode.com/problems/middle-of-the-linked-list/ |
| 21 | Merge Two Sorted Lists | 🟢 | https://leetcode.com/problems/merge-two-sorted-lists/ |
| 234 | Palindrome Linked List | 🟢 | https://leetcode.com/problems/palindrome-linked-list/ |
| 142 | Linked List Cycle II (find start of loop) | 🟡 | https://leetcode.com/problems/linked-list-cycle-ii/ |
| 19 | Remove Nth Node From End | 🟡 | https://leetcode.com/problems/remove-nth-node-from-end-of-list/ |
| 2 | Add Two Numbers | 🟡 | https://leetcode.com/problems/add-two-numbers/ |

### Stack
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 20 | ⭐ Valid Parentheses (balanced brackets) | 🟢 | https://leetcode.com/problems/valid-parentheses/ |
| 155 | ⭐ Min Stack | 🟡 | https://leetcode.com/problems/min-stack/ |
| 232 | ⭐ Implement Queue using Stacks | 🟢 | https://leetcode.com/problems/implement-queue-using-stacks/ |
| 150 | Evaluate Reverse Polish Notation (postfix) | 🟡 | https://leetcode.com/problems/evaluate-reverse-polish-notation/ |
| 496 | Next Greater Element I | 🟢 | https://leetcode.com/problems/next-greater-element-i/ |
| 739 | Daily Temperatures (monotonic stack) | 🟡 | https://leetcode.com/problems/daily-temperatures/ |

### Queue
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 225 | ⭐ Implement Stack using Queues | 🟢 | https://leetcode.com/problems/implement-stack-using-queues/ |
| 622 | ⭐ Design Circular Queue | 🟡 | https://leetcode.com/problems/design-circular-queue/ |
| 933 | Number of Recent Calls | 🟢 | https://leetcode.com/problems/number-of-recent-calls/ |
| 239 | Sliding Window Maximum (deque) | 🔴 | https://leetcode.com/problems/sliding-window-maximum/ |
| 542 | 01 Matrix (BFS uses a queue) | 🟡 | https://leetcode.com/problems/01-matrix/ |

### Binary Tree
| # | Problem | Difficulty | Link |
|---|---------|-----------|------|
| 94 | ⭐ Inorder Traversal | 🟢 | https://leetcode.com/problems/binary-tree-inorder-traversal/ |
| 144 | Preorder Traversal | 🟢 | https://leetcode.com/problems/binary-tree-preorder-traversal/ |
| 145 | Postorder Traversal | 🟢 | https://leetcode.com/problems/binary-tree-postorder-traversal/ |
| 102 | ⭐ Level Order Traversal (BFS + queue) | 🟡 | https://leetcode.com/problems/binary-tree-level-order-traversal/ |
| 104 | ⭐ Maximum Depth of Binary Tree | 🟢 | https://leetcode.com/problems/maximum-depth-of-binary-tree/ |
| 226 | Invert Binary Tree | 🟢 | https://leetcode.com/problems/invert-binary-tree/ |
| 101 | Symmetric Tree | 🟢 | https://leetcode.com/problems/symmetric-tree/ |
| 98 | ⭐ Validate Binary Search Tree | 🟡 | https://leetcode.com/problems/validate-binary-search-tree/ |
| 700 | Search in a BST | 🟢 | https://leetcode.com/problems/search-in-a-binary-search-tree/ |
| 235 | Lowest Common Ancestor of a BST | 🟡 | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ |

> **If you only have time for 7 problems (one per topic), do these:**
> 136 (Bit) · 704 (Binary Search) · 1 (Hashing) · 206 (Linked List) · 20 (Stack) · 622 (Queue) · 94 (Binary Tree).

---

<a name="10-cheat-sheet"></a>
## 10. Last-Minute Cheat Sheet

**Complexities at a glance:**
| Structure/Algo | Search | Insert | Delete | Notes |
|----------------|--------|--------|--------|-------|
| Binary Search | O(log n) | — | — | sorted array only |
| Hash Table | O(1) avg / O(n) worst | O(1) avg | O(1) avg | collisions hurt |
| Linked List | O(n) | O(1) at head | O(1) if node known | no random access |
| Stack | O(n) | O(1) push | O(1) pop | LIFO |
| Queue | O(n) | O(1) enqueue | O(1) dequeue | FIFO |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(n) if skewed |

**One-liners to always say in viva:**
- Always state **time and space complexity** with each answer — it signals you know your stuff.
- "Binary search needs a **sorted** array."
- "Hashing gives **O(1) average**, O(n) worst due to collisions."
- "Inorder of a BST is **sorted**."
- "Stack is **LIFO**, Queue is **FIFO**."
- "Linked list = dynamic size, no random access."

**The 6-hour study plan:**
1. **(1.5h)** Read this whole file once, out loud.
2. **(2h)** Write on paper: binary search, reverse a linked list, cycle detection, 3 tree traversals, balanced-parentheses with a stack.
3. **(1h)** Cover the answers, quiz yourself on every 🎤 VIVA box.
4. **(1h)** Drill definitions + complexities (fast-fire section).
5. **(0.5h)** Rest before the viva. Confidence beats last-minute panic.

---

*You've got this. Speak clearly, state complexities, and if unsure, reason out loud — examiners reward thinking. Good luck! 🚀*
