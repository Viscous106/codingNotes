# Binary Trees — Concepts and Problem Solving

Based on 5 lecture transcripts covering Binary Trees from scratch to advanced problems.

## Topics Covered

1. **Tree Fundamentals** — Terminology, structure, node definition
2. **BFS / Level-Order Traversal** — Iterative queue-based traversal
3. **DFS Traversals** — Pre-order, In-order, Post-order (recursive + iterative)
4. **Serialised Tree Input** — How to build a tree from pre-order input
5. **Basic Recursive Problems** — Count nodes, Sum of nodes, Height
6. **Height Balanced Check**
7. **Diameter of a Binary Tree**
8. **Root-to-Leaf Path Sum**
9. **Equal Tree Partition**
10. **Populate Next Right Pointers (Level-order linking)**
11. **Construct Tree from Inorder + Postorder**
12. **Flatten Binary Tree to Linked List**
13. **Vertical Order Traversal**

---

> 📅 **SESSION 1 — Trees 1 (24th March)** · Topics: Tree fundamentals, BFS, DFS traversals

## 1. Tree Fundamentals

A **Tree** is a hierarchical, non-linear data structure made up of **nodes** connected by **edges**, with **no cycles**.

### Key Terminology

| Term | Meaning |
|---|---|
| **Root** | The topmost node (no parent) |
| **Parent / Child** | A node is a parent of the nodes directly below it |
| **Leaf** | A node with no children |
| **Height** | The longest path from a node DOWN to a leaf |
| **Depth** | The distance from the root DOWN to a given node |
| **Subtree** | A node and all its descendants |

### Binary Tree

A **Binary Tree** is a tree where every node has **at most 2 children**: `left` and `right`.

```java
class Node {
    int data;
    Node left;
    Node right;

    Node(int x) {
        data = x;
        left = null;
        right = null;
    }
}
```

> A node with `data = 10`, `left = null`, `right = null` is a **leaf node**.

---

## 2. BFS — Level-Order Traversal

Visit nodes **level by level**, from left to right, using a **Queue**.

### Algorithm
1. Add the root to a Queue.
2. While the queue is not empty:
   - Remove the front node.
   - Print it.
   - Add its left child (if exists) to the queue.
   - Add its right child (if exists) to the queue.

```java
void levelOrder(Node root) {
    if (root == null) return;

    Queue<Node> q = new LinkedList<>();
    q.add(root);

    while (!q.isEmpty()) {
        Node removed = q.remove();
        System.out.print(removed.data + " ");

        if (removed.left != null)  q.add(removed.left);
        if (removed.right != null) q.add(removed.right);
    }
}
```

- **Time Complexity**: $O(N)$ — every node visited once
- **Space Complexity**: $O(N)$ — queue can hold up to one full level

---

## 3. DFS Traversals

All three traversals differ only in **when you print** relative to the recursive calls on left and right.

```
Pre-order  →  Root | Left | Right   (N L R)
In-order   →  Left | Root | Right   (L N R)
Post-order →  Left | Right | Root   (L R N)
```

### 3A. Pre-order (Root → Left → Right)

```java
void preorder(Node root) {
    if (root == null) return;
    System.out.print(root.data + " ");   // ← print FIRST
    preorder(root.left);
    preorder(root.right);
}
// Output for tree [1,2,3,4,5,7,6]: 1 2 4 5 7 3 6
```

### 3B. In-order (Left → Root → Right)

```java
void inorder(Node root) {
    if (root == null) return;
    inorder(root.left);
    System.out.print(root.data + " ");   // ← print MIDDLE
    inorder(root.right);
}
```

> **Key insight**: In-order traversal of a **BST** produces a **sorted** output.

### 3C. Post-order (Left → Right → Root)

```java
void postorder(Node root) {
    if (root == null) return;
    postorder(root.left);
    postorder(root.right);
    System.out.print(root.data + " ");   // ← print LAST
}
```

> **Use case**: Deleting a tree, evaluating expression trees — children must be processed before the parent.

### Iterative In-order Traversal

Uses an explicit Stack to simulate the recursion.

```java
void iterativeInorder(Node root) {
    Stack<Node> stack = new Stack<>();
    Node curr = root;

    while (curr != null || !stack.isEmpty()) {
        // Reach leftmost node
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        // Process node
        curr = stack.pop();
        System.out.print(curr.data + " ");
        // Move to right subtree
        curr = curr.right;
    }
}
```

---

> ✅ **END OF SESSION 1 — Trees 1 (24th March)**

---

> 📅 **SESSION 2 — Binary Trees 2** · Topics: Serialised input, Count/Sum/Height, Height Balanced

## 4. Serialised Tree Input (Building a Tree from Pre-order Input)

This format is used on platforms like Scaler. `-1` represents a `null` node.

**Example input**: `1 2 3 4 5 -1 6 -1 -1 7 -1 8 9 -1 -1 -1 -1 -1 -1`

The tree is built using a **queue**: every time you create a real node, enqueue it and set its left and right children from the next two values in the input.

```java
Node buildTree(int[] arr) {
    if (arr == null || arr[0] == -1) return null;

    Node root = new Node(arr[0]);
    Queue<Node> q = new LinkedList<>();
    q.add(root);
    int i = 1;

    while (!q.isEmpty() && i < arr.length) {
        Node curr = q.remove();

        // Left child
        if (arr[i] != -1) {
            curr.left = new Node(arr[i]);
            q.add(curr.left);
        }
        i++;

        // Right child
        if (i < arr.length && arr[i] != -1) {
            curr.right = new Node(arr[i]);
            q.add(curr.right);
        }
        i++;
    }
    return root;
}
```

---

## 5. Basic Recursive Problems

### 5A. Count Nodes

```java
int count(Node root) {
    if (root == null) return 0;

    int lc = count(root.left);
    int rc = count(root.right);

    return lc + rc + 1;
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$ where H = height of tree (recursion stack)

### 5B. Sum of Nodes

```java
int sum(Node root) {
    if (root == null) return 0;

    int ls = sum(root.left);
    int rs = sum(root.right);

    return ls + rs + root.data;
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$

### 5C. Height of a Binary Tree

The **height** at any node = `max(height of left subtree, height of right subtree) + 1`. Leaf nodes have height `1`.

```java
int height(Node root) {
    if (root == null) return 0;

    int lh = height(root.left);
    int rh = height(root.right);

    return Math.max(lh, rh) + 1;
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$

---

## 6. Height Balanced Binary Tree

A tree is **height-balanced** if for **every node**:

$$| \text{height(left)} - \text{height(right)} | \leq 1$$

### Approach 1: Brute Force — $O(N^2)$

Call `height()` at every node separately.

### Approach 2: Optimised — $O(N)$

Return `-1` as a sentinel value from `height()` when the subtree is already imbalanced. This avoids recomputing subtree heights.

```java
// Returns height if balanced, -1 if not balanced
int checkHeight(Node root) {
    if (root == null) return 0;

    int lh = checkHeight(root.left);
    if (lh == -1) return -1;   // already broken

    int rh = checkHeight(root.right);
    if (rh == -1) return -1;   // already broken

    if (Math.abs(lh - rh) > 1) return -1;  // this node breaks balance

    return Math.max(lh, rh) + 1;
}

boolean isBalanced(Node root) {
    return checkHeight(root) != -1;
}
```
- **TC**: $O(N)$ — each node visited once | **SC**: $O(H)$

---

> ✅ **END OF SESSION 2 — Binary Trees 2**

---

> 📅 **SESSION 3 — Trees 3 (31st March)** · Topics: Diameter, Root-to-Leaf Path Sum, Left View

## 7. Diameter of a Binary Tree

The **diameter** is the longest path between **any two nodes** in the tree. The path may or may not pass through the root.

For each node, the longest path through it =  
`height(left subtree) + height(right subtree) + 2` (counting edges)  
or equivalently `lh + rh + 2` if we count heights as number of nodes.

### Approach 1: $O(N^2)$ — Calling height separately

```java
int diameter(Node root) {
    if (root == null) return 1;

    int ld = diameter(root.left);
    int rd = diameter(root.right);
    int lh = height(root.left);
    int rh = height(root.right);

    return Math.max(ld, Math.max(rd, lh + rh + 2));
}
```

### Approach 2: $O(N)$ — Compute diameter and height together

Use an array (or wrapper class) to pass the diameter up the call stack, while the function itself returns height.

```java
int diameterHelper(Node root, int[] maxDiam) {
    if (root == null) return 0;

    int lh = diameterHelper(root.left, maxDiam);
    int rh = diameterHelper(root.right, maxDiam);

    // Update global max diameter at this node
    maxDiam[0] = Math.max(maxDiam[0], lh + rh + 2);

    return Math.max(lh, rh) + 1;
}

int diameter(Node root) {
    int[] maxDiam = new int[1];
    diameterHelper(root, maxDiam);
    return maxDiam[0];
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$

---

## 8. Root-to-Leaf Path Sum

Given a tree and a target `K`, check if there's any **root-to-leaf path** whose node values sum to `K`.

### Logic

At each recursive call, subtract the current node's value from K. When we reach a **leaf**, check if the remaining `K == 0`.

```java
boolean hasPath(Node root, int K) {
    if (root == null) return false;

    // Check if it's a leaf and K is satisfied
    if (root.left == null && root.right == null) {
        return (K - root.data == 0);
    }

    boolean la = hasPath(root.left,  K - root.data);
    boolean ra = hasPath(root.right, K - root.data);

    return la || ra;
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$

---

> ✅ **END OF SESSION 3 — Trees 3 (31st March)**

---

> 📅 **SESSION 4 — Trees 4 (2nd April)** · Topics: Equal Tree Partition, Next Right Pointers, Construct from In+Post

## 9. Equal Tree Partition

**Question**: Given a binary tree, can it be split into **two non-empty subtrees** with **equal sum** by removing exactly one edge?

### Key Insight

If total sum of tree = `S`, we need a subtree with sum = `S / 2`.  
Walk the tree. If any subtree's sum equals `S / 2`, return `true`.

```java
int totalSum;

boolean isPartitionPossible(Node root) {
    totalSum = sum(root);
    if (totalSum % 2 != 0) return false; // odd total → impossible
    boolean[] ans = new boolean[1];
    checkPartition(root, ans);
    return ans[0];
}

int checkPartition(Node root, boolean[] ans) {
    if (root == null) return 0;

    int la = checkPartition(root.left, ans);
    int ra = checkPartition(root.right, ans);
    int currSum = la + ra + root.data;

    if (currSum == totalSum / 2) ans[0] = true;

    return currSum;
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$

> **Edge case**: The root itself should not count as the "cut" — it represents the whole tree. We only consider non-root subtrees during traversal.

---

## 10. Populate Next Right Pointers (Level-Order Linking)

**Question**: Given a perfect binary tree where each node also has a `next` pointer (initially `null`), connect each node's `next` pointer to the node immediately to its **right on the same level**. The last node on each level should point to `null`.

```
      1        →  1->null
    /   \
   2     3    →  2->3->null
  / \   / \
 4   5 6   7  →  4->5->6->7->null
```

### Approach: Level-Order with Queue

```java
void connect(Node root) {
    if (root == null) return;

    Queue<Node> q = new LinkedList<>();
    q.add(root);

    while (!q.isEmpty()) {
        int size = q.size(); // size of current level

        for (int i = 0; i < size; i++) {
            Node curr = q.poll();

            // If not last node on this level, link to next
            if (i < size - 1) {
                curr.next = q.peek(); // next in queue = right neighbour
            }

            if (curr.left  != null) q.add(curr.left);
            if (curr.right != null) q.add(curr.right);
        }
    }
}
```
- **TC**: $O(N)$ | **SC**: $O(N)$

---

## 11. Construct Tree from Inorder + Postorder

**Question**: Given the **inorder** and **postorder** traversal arrays of a binary tree, reconstruct the tree.

### Key Properties

- **Postorder**: Last element = **root**
- **Inorder**: Root divides into left subtree and right subtree

### Algorithm

1. Pick the **last element** of `postorder` as root.
2. Find that element's position `idx` in `inorder`.
3. Everything left of `idx` → left subtree | Everything right of `idx` → right subtree.
4. Recursively build both subtrees.

```
inorder:   [4, 2, 5, 1, 6, 3, 7]
postorder: [4, 5, 2, 6, 7, 3, 1]
                          ↑
                        root = 1
inorder:   [4,2,5] | [6,3,7]   idx=3
```

```java
int[] in, post;

Node createTree(int ip, int rp, int li, int ri) {
    if (ip > rp || li > ri) return null;

    Node root = new Node(post[rp]);  // last of postorder = root

    // Find root in inorder to split subtrees
    int pos = -1;
    for (int i = li; i <= ri; i++) {
        if (in[i] == post[rp]) { pos = i; break; }
    }

    int leftSize = pos - li;

    root.left  = createTree(ip, ip + leftSize - 1, li, pos - 1);
    root.right = createTree(ip + leftSize, rp - 1, pos + 1, ri);

    return root;
}
```
- **TC**: $O(N^2)$ brute force (linear search). Can improve to $O(N)$ using a HashMap for inorder index lookup.

---

> ✅ **END OF SESSION 4 — Trees 4 (2nd April)**

---

> 📅 **SESSION 5 — Trees 5 (4th April)** · Topics: Flatten Binary Tree, Vertical Order Traversal

## 12. Flatten Binary Tree to Linked List

**Question**: Given a binary tree, flatten it into a **linked list in-place** following **pre-order** traversal. All nodes use only the `right` pointer; `left` is always `null`.

```
    1              1
   / \              \
  2   5      →      2
 / \   \              \
3   4   6              3
                        \
                         4
                          \
                           5
                            \
                             6
```

### Algorithm

1. **Flatten** left subtree first (recursive).
2. **Flatten** right subtree.
3. Save `root.right` into `temp`.
4. Move the flattened left subtree to `root.right`.
5. Set `root.left = null`.
6. Traverse to the tail of the newly placed left (now right) list and attach `temp`.

```java
void flatten(Node root) {
    if (root == null) return;

    flatten(root.left);
    flatten(root.right);

    Node temp = root.right;  // save right subtree

    root.right = root.left;  // move left to right
    root.left = null;

    // Find end of the now-right chain
    Node curr = root;
    while (curr.right != null) {
        curr = curr.right;
    }

    curr.right = temp;  // attach saved right subtree
}
```
- **TC**: $O(N)$ | **SC**: $O(H)$ (recursion stack)

---

## 13. Vertical Order Traversal

**Question**: Return the nodes of a binary tree grouped by **vertical column**, from leftmost to rightmost.

### Key Idea

Assign each node a **column number** (also called `num` or horizontal distance):
- Root → `num = 0`
- Going **left** → `num - 1`
- Going **right** → `num + 1`

Use a **HashMap** mapping `column_num → List<node values>`. Then collect all lists sorted by key.

```java
void preorder(Node root, int num, HashMap<Integer, List<Integer>> map) {
    if (root == null) return;

    if (map.containsKey(num)) {
        map.get(num).add(root.data);
    } else {
        List<Integer> list = new ArrayList<>();
        list.add(root.data);
        map.put(num, list);
    }

    preorder(root.left,  num - 1, map);
    preorder(root.right, num + 1, map);
}

List<List<Integer>> verticalOrder(Node root) {
    HashMap<Integer, List<Integer>> map = new HashMap<>();
    preorder(root, 0, map);

    // Find min and max column numbers
    int min = Collections.min(map.keySet());
    int max = Collections.max(map.keySet());

    List<List<Integer>> result = new ArrayList<>();
    for (int i = min; i <= max; i++) {
        result.add(map.get(i));
    }
    return result;
}
```
- **TC**: $O(N)$ for traversal, $O(N \log N)$ if sorting is needed within columns
- **SC**: $O(N)$

---

> ✅ **END OF SESSION 5 — Trees 5 (4th April)**

---

## Summary — Complexity Reference

| Problem | Time | Space |
|---|---|---|
| Level-Order Traversal (BFS) | $O(N)$ | $O(N)$ |
| DFS Traversals (Pre/In/Post) | $O(N)$ | $O(H)$ |
| Count Nodes | $O(N)$ | $O(H)$ |
| Sum of Nodes | $O(N)$ | $O(H)$ |
| Height of Tree | $O(N)$ | $O(H)$ |
| Height Balanced Check (Optimised) | $O(N)$ | $O(H)$ |
| Diameter (Optimised) | $O(N)$ | $O(H)$ |
| Root-to-Leaf Path Sum | $O(N)$ | $O(H)$ |
| Equal Tree Partition | $O(N)$ | $O(H)$ |
| Next Right Pointers | $O(N)$ | $O(N)$ |
| Build Tree from In+Post | $O(N^2)$ brute / $O(N)$ w/ HashMap | $O(N)$ |
| Flatten to Linked List | $O(N)$ | $O(H)$ |
| Vertical Order Traversal | $O(N)$ | $O(N)$ |

> $H$ = height of the tree. In the worst case (skewed tree), $H = N$. For a balanced tree, $H = \log N$.
