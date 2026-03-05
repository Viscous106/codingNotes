# Hashing Part 3: Under the Hood & Advanced Applications

Welcome to the final part of the Hashing Study Guide! In this section, we'll dive into how HashMaps actually work behind the scenes, and then tackle two advanced string and sequence problems.

---

## 1. Hash Function, Collision, and Chaining

Have you ever wondered *how* a HashMap can store and retrieve data in $O(1)$ instant time? It uses an array internally, but maps Keys to array indices using a **Hash Function**.

### The Process:
1. **Hash Code:** When you `put(Key, Value)`, the HashMap passes the Key through a mathematical formula (Hash Function) to generate a unique integer called a Hash Code.
2. **Modulo:** This Hash Code can be huge, so it is modulo'd by the size of the internal array to get a valid index (`index = HashCode % arraySize`).
3. **Insertion:** The Value is stored at that specific index in the array.

### What is a Collision?
Sometimes, two completely different Keys will produce the exact same array index. This is called a **Collision**.
* *Example:* If our array size is 10, Keys with Hash Codes `15` and `25` will both land at index `5` (`15 % 10 = 5` and `25 % 10 = 5`).
* We can't just overwrite the old value! We need a way to store both.

### The Solution: Chaining
To resolve collisions, HashMaps use **Chaining**. 
Instead of storing a single value at each array index, every index actually holds a **LinkedList**. When a collision occurs, the HashMap just adds the new Key-Value pair to the end of the LinkedList at that specific index.

* **Searching `get(Key)`:** The HashMap hashes your Key to find the index, then searches through the short LinkedList at that index to find your exact Key and return its Value.
* Because the array is dynamically resized to be very large, collisions are rare, meaning the LinkedLists stay very small. This is why operations remain incredibly fast, averaging at $O(1)$!

---

## 2. Longest Substring Without Repeating Characters

**The Problem:** Given a string `s`, find the length of the longest contiguous substring that contains no repeating characters.
* *Input:* `"abcabcbb"`
* *Output:* `3` (The substring is `"abc"`)

**The Logic (Sliding Window + HashSet):**
We can use two pointers, `i` (left) and `j` (right), to represent a "window" of characters. We will use a **HashSet** to keep track of the characters currently inside our window.
1. Start both `i` and `j` at index `0`.
2. Look at the character at `j`.
3. **If the character is NOT in our set:** We haven't seen it in our current window! Add it to the set, update our maximum length `max_len = max(max_len, j - i + 1)`, and expand the window by moving `j` to the right (`j++`).
4. **If the character IS in our set:** We've found a repeat! We must shrink our window from the left until the repeating character is removed. We remove the character at `i` from the set, and move `i` to the right (`i++`).

**Code Example:**
```java
import java.util.HashSet;

public class LongestSubstring {
    public static int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int i = 0; // Left pointer
        int j = 0; // Right pointer
        int maxLen = 0;
        
        while (j < s.length()) {
            char currentChar = s.charAt(j);
            
            // If we haven't seen the character in our current window
            if (!set.contains(currentChar)) {
                set.add(currentChar);
                maxLen = Math.max(maxLen, j - i + 1); // j - i + 1 is the current window length
                j++; // Expand window
            } 
            // If it's a repeat!
            else {
                // Remove the character at the left pointer and shrink window
                set.remove(s.charAt(i));
                i++; 
            }
        }
        
        return maxLen;
    }
}
```

---

## 3. Length of Longest Consecutive Sequence

**The Problem:** Given an unsorted array of integers, find the length of the longest consecutive elements sequence. A consecutive sequence is `x, x+1, x+2, x+3...` (e.g., `4, 5, 6, 7`). The order they appear in the array does not matter!
* *Input:* `[100, 4, 200, 1, 3, 2]`
* *Output:* `4` (The sequence is `1, 2, 3, 4`)

**The Logic:**
The slow way is sorting $O(N \log N)$. The fast way ($O(N)$) is using a **HashSet**.
1. Dump every single element of the array into a HashSet so we can do instant $O(1)$ lookups.
2. Iterate through the array. For every number `x`, we want to check if it's the **start** of a sequence.
3. *How do we know if `x` is the start?* If `x - 1` is NOT in the HashSet! If `x - 1` exists, then `x` is just the middle of some sequence, and we can ignore it for now.
4. If `x` *is* the start of a sequence, we use a `while` loop to repeatedly check if `x + 1`, `x + 2`, `x + 3`... exist in the HashSet. We count how long the sequence goes!

**Code Example:**
```java
import java.util.HashSet;

public class LongestConsecutiveSequence {
    public static int longestConsecutive(int[] A) {
        HashSet<Integer> set = new HashSet<>();
        
        // Step 1: Dump EVERYTHING into the HashSet
        for (int num : A) {
            set.add(num);
        }
        
        int maxLength = 0;
        
        // Step 2: Traverse array to find sequence starts
        for (int i = 0; i < A.length; i++) {
            int currentNum = A[i];
            
            // Check if this number is the START of a sequence
            // (It is the start ONLY if currentNum - 1 does not exist!)
            if (!set.contains(currentNum - 1)) {
                
                // We found a start! Let's count how long this sequence goes.
                int currentStreak = 1;
                int nextNum = currentNum + 1;
                
                while (set.contains(nextNum)) {
                    currentStreak++;
                    nextNum++;
                }
                
                // Update our maximum length found so far
                maxLength = Math.max(maxLength, currentStreak);
            }
        }
        
        return maxLength;
    }
}
```

---
## Practice Problem: Sort Array in Given Order
**Problem:** Given two arrays of integers `A` and `B`, sort `A` in such a way that the relative order among the elements will be the same as those in `B`. For elements not present in `B`, append them at the end in sorted order.

**Solution (Standard HashMap):**
If you aren't familiar with `TreeMap`, we can easily solve this using the standard tools taught in class: a **HashMap** and an **Array Sort**.
1. Build a frequency map of `A` using a standard `HashMap`.
2. Loop through `B`. For each element, look it up in the `HashMap`. If it exists, append it to our answer array `frequency` times. Then, **remove** it from the map completely.
3. Once we finish looping through `B`, what is left in our `HashMap`? Only the numbers from `A` that were *not* in `B`.
4. Loop through our original array `A`. If the current number `A[i]` is STILL in our map, it means we haven't used it! Add it to our answer array and decrease its frequency in the map.
5. Because we need these leftover numbers sorted, we just use Java's built-in `Arrays.sort()` to sort *only* the rightmost leftover chunk of our final answer array!

```java
import java.util.HashMap;
import java.util.Arrays;

public class Solution {
    public int[] solve(int[] A, int[] B) {
        // Step 1: Count frequencies using a standard HashMap
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int i = 0; i < A.length; i++) {
            freqMap.put(A[i], freqMap.getOrDefault(A[i], 0) + 1);
        }
        
        int[] ans = new int[A.length];
        int index = 0;
        
        // Step 2: Extract elements in the exact order they appear in B
        for (int i = 0; i < B.length; i++) {
            int num = B[i];
            
            if (freqMap.containsKey(num)) {
                int count = freqMap.get(num);
                while (count > 0) {
                    ans[index] = num;
                    index++;
                    count--;
                }
                // We used this number completely, so remove it from the map!
                freqMap.remove(num);
            }
        }
        
        // Step 3: Gather the remaining leftover elements
        // Remember where the leftover elements start in our array
        int leftoverStartIndex = index; 
        
        // Loop through the original array. If the number is still in the map, add it
        // and reduce its count. 
        for (int i = 0; i < A.length; i++) {
            int num = A[i];
            
            if (freqMap.containsKey(num)) {
                ans[index] = num;
                index++;
                
                int newCount = freqMap.get(num) - 1;
                if (newCount == 0) {
                    freqMap.remove(num);
                } else {
                    freqMap.put(num, newCount);
                }
            }
        }
        
        // Step 4: Sort ONLY the leftmost part of the array
        // Arrays.sort(array, startIndex, endIndex)
        Arrays.sort(ans, leftoverStartIndex, ans.length);
        
        return ans;
    }
}
```
