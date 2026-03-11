# Linked List Concepts and Problem Solving

Based on the transcript from the lecture notes you provided, here is a breakdown of the concepts covered, followed by explanations, LeetCode solutions, and a deep-dive on how to copy a linked list in Java.

## 1. Concepts Covered in the Transcript

The lecture covered several core Linked List algorithms:

### A. Merging Two Sorted Linked Lists
This involves taking two linked lists that are already sorted and combining them into a single sorted linked list by continually picking the smaller of the two node values.
- **Time Complexity**: $O(N + M)$ where N and M are the lengths of the two lists.
- **Space Complexity**: $O(1)$ since we are just rearranging pointers and not creating new nodes.

### B. Merge Sort on Linked Lists
To sort a linked list optimally in $O(N \log N)$ time, Merge Sort is heavily used. The algorithm dictates:
1. **Find the middle** of the linked list (using fast and slow pointers approach).
2. **Split** the list into two halves and recursively sort both of them.
3. **Merge** the two sorted halves (using the exact logic from concept A).
- **Time Complexity**: $O(N \log N)$
- **Space Complexity**: $O(\log N)$ for the recursive call stack depth.

### C. Detecting a Loop / Cycle in a Linked List (Floyd's Cycle Finding Algorithm)
To find if a cycle exists, we use a `slow` pointer (moves 1 step at a time) and a `fast` pointer (moves 2 steps at a time). If they ever meet, a cycle definitely exists.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$

### D. Finding the Starting Point of the Loop
If a loop is detected, the transcript includes the mathematical proof (involving distances where `2x = L + KC`) to find exactly where the start of the loop is.
- **Algorithm**: Once `fast` and `slow` meet (confirming a cycle), reset either `slow` or `fast` to the `head` of the list. Then, move both one step at a time. The very node where they meet again is guaranteed to be the starting point of the cycle.
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$

---

## 2. Related LeetCode Questions in Java

Here are the optimal Java implementations for the concepts discussed.

### LeetCode 21: Merge Two Sorted Lists
```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Dummy node simplifies handling the head of our new list
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;
        
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        
        // Attach any remaining nodes from the non-empty list
        current.next = (list1 != null) ? list1 : list2;
        
        return dummy.next;
    }
}
```

### LeetCode 148: Sort List (Merge Sort)
```java
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        // Step 1: Find middle
        ListNode slow = head, fast = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Step 2: Break the list into two halves
        prev.next = null;
        
        // Step 3: Recursively sort both halves
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        
        // Step 4: Merge them
        return mergeTwoLists(l1, l2);
    }
    
    // Using the same merge helper as above
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

### LeetCode 141 & 142: Linked List Cycle I & II (Detect and Find Start)
```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;
        
        // Detect cycle
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                hasCycle = true;
                break;
            }
        }
        
        // Return early if no cycle exists
        if (!hasCycle) return null;
        
        // Find starting point (reset one to head, move both by 1 step)
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        
        return slow; // The node where they meet is the cycle's starting point
    }
}
```

---

## 3. How to Make a Copy of a Linked List (from Basics)

Copying a linked list generally points to the famous **"Copy List with Random Pointer" (LeetCode 138)** problem, where each node has a standard `next` pointer and an arbitrary `random` pointer that can point to literally any node (or point to null).

### The Basics: Deep Copy vs Shallow Copy
- **Shallow Copy**: Copying only the references. The new list points to the exact same nodes in memory. Changing one changes the other. This isn't a true structural copy.
- **Deep Copy**: Creating entirely new nodes in memory with the same values, so the two lists are completely independent.

### The Problem with Random Pointers
If it was just a normal linked list (with only `next` pointers), we could simply iterate through and create new nodes one by one. But with `random` pointers, when we try to assign `newNode.random`, the exact target node it should point to might not have been created yet, or we don't know which newly created node corresponds to it!

### Approach 1: Using a HashMap ($O(N)$ Extra Space)
The easiest way to understand this is using a Map to keep track of the mapping from old nodes to new nodes.
We structure our memory as `Old Node -> New Node`.
1. **Pass 1:** Iterate through the original list. For each node, create a blank new node with the same value and put them in our map: `map.put(oldNode, newNode)`.
2. **Pass 2:** Iterate again. Now all clone nodes exist. We can easily connect the newly created pointers because we know which old node maps to which new node.
   - `newNode.next = map.get(oldNode.next);`
   - `newNode.random = map.get(oldNode.random);`

### Strategy 2: The $O(1)$ Space Trick (Interweaving - Highly Optimal)
This is the most optimal way to solve it and is heavily favored in technical interviews since it drops the $O(N)$ HashMap extra space.

**Step 1: Create Interleaved Array**
Insert every cloned node immediately after its original node in the same linked structure.
`A -> A' -> B -> B' -> C -> C'`

**Step 2: Assign Random Pointers**
Since `A'` is situated right next to `A`, the random pointer of `A'` is simply the node next to the random pointer of `A`!
`A'.random = A.random.next;`

**Step 3: Separate (Unweave) the Lists**
Restore the original list back to how it was and extract out the cloned `next` structures.

### Java Implementation ($O(1)$ Space approach)
```java
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        
        // Step 1: Clone nodes and interweave
        Node curr = head;
        while (curr != null) {
            Node clone = new Node(curr.val);
            clone.next = curr.next;
            curr.next = clone;
            curr = clone.next;
        }
        
        // Step 2: Assign random pointers for the clones
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                // curr.next is our cloned node
                // curr.random.next is the clone of our random target
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        
        // Step 3: Separate the original and cloned lists
        curr = head;
        Node cloneHead = head.next;
        Node cloneCurr = cloneHead;
        
        while (curr != null) {
            curr.next = curr.next.next;
            if (cloneCurr.next != null) {
                cloneCurr.next = cloneCurr.next.next;
            }
            curr = curr.next;
            cloneCurr = cloneCurr.next;
        }
        
        return cloneHead;
    }
}
```
