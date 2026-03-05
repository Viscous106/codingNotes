# Hashing: The Ultimate Beginner's Study Guide

Welcome! Since you're starting from scratch, don't worry. This guide translates the entire transcript into a simple, easy-to-understand format so you can **ace your exam**.

The transcript covers six main topics. We'll go through them step by step.

---

## 1. Introduction to HashMap & its Functions

**What is a HashMap?**
Imagine you work at a hotel reception, and you have a record of who is in which room. Instead of searching through every room to find a specific person, you have a register that instantly tells you: "Room 101 -> John Doe". 

A **HashMap** (also known as a Dictionary in Python) works exactly like this. It stores data in **Key-Value pairs**.
* **Key:** The unique identifier (e.g., Room Number, Country Name).
* **Value:** The data associated with that key (e.g., Guest Name, Population).

**Why use a HashMap?**
Because it is incredibly fast! It can store a key-value pair and retrieve a value using its key in **$O(1)$ time complexity** (meaning it takes a constant, instant amount of time, no matter how much data you have).

**Given Examples from the Transcript:**
* *Population of every country:* `HashMap<String, Long>` (Key: Country Name, Value: Population).
* *States in a country:* `HashMap<String, List<String>>` (Key: Country Name, Value: List of State Names).

**Common Functions:**
* `put(key, value)`: Inserts a new key-value pair (or updates an existing key).
* `get(key)`: Retrieves the value for the given key.
* `containsKey(key)`: Returns `true` if the key exists, `false` otherwise.
* `remove(key)`: Deletes the key-value pair.

**Code Example:**
```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        // 1. Declare HashMap<KeyType, ValueType>
        HashMap<String, Integer> map = new HashMap<>();

        // 2. Insert or Update (put)
        map.put("India", 145);
        map.put("USA", 65);

        // 3. Retrieve (get)
        System.out.println(map.get("India")); // Prints 145

        // 4. Check if Key exists (containsKey)
        if (map.containsKey("USA")) {
            System.out.println("USA is in the map!");
        }

        // 5. Remove (remove)
        map.remove("USA");
    }
}
```

---

## 2. Given queries, find the frequency of an element

**The Problem:** You are given a list of N numbers. You will then be asked Q questions (queries) like: "How many times does the number 5 appear?".

**The Naive Way:** For every query, loop through the entire list to count. This takes too much time ($O(N)$ for each query).

**The HashMap Way (Frequency Map):**
We can use a HashMap where:
* **Key** = The number from the array.
* **Value** = The frequency (how many times we've seen it).

**Step-by-Step Logic:**
1. Create an empty `HashMap<Integer, Integer>`.
2. Loop through your given list of numbers.
3. For each number:
   * If it's already in the HashMap, get its current frequency, add 1, and update it.
   * If it's not in the HashMap, put it in with a frequency of 1.
4. Now, to answer any query, just do `map.get(number)`. It takes instant $O(1)$ time!

**Code Example:**
```java
import java.util.HashMap;

public class Frequency {
    public static void main(String[] args) {
        int[] arr = {5, 2, 5, 2, 8};
        
        // HashMap to store: Number -> Frequency
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for (int num : arr) {
            // If number exists, get its count. Otherwise, default to 0. Add 1.
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Output queries in O(1) time
        System.out.println("Frequency of 5: " + freqMap.getOrDefault(5, 0)); // Prints 2
        System.out.println("Frequency of 8: " + freqMap.getOrDefault(8, 0)); // Prints 1
        System.out.println("Frequency of 10: " + freqMap.getOrDefault(10, 0)); // Prints 0
    }
}
```

---

## 3. Introduction to HashSet & its Functions

**What is a HashSet?**
If a HashMap is like a dictionary (Key -> Value), a **HashSet** is like a mathematical Set. It is a simple bag of items that **only stores UNIQUE elements**. 

It does not keep track of frequencies, and it does not store values—just the unique keys.

**Why use a HashSet?**
To quickly check if an element exists, or to remove duplicates from a list. Checking if an item is in the set also takes instant **$O(1)$ time**.

**Common Functions:**
* `add(element)`: Adds an item. If it's already there, it does nothing.
* `contains(element)`: Returns `true` if the item is inside.
* `remove(element)`: Removes the item.

**Code Example:**
```java
import java.util.HashSet;

public class SetBasics {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();

        // 1. Insert (add)
        set.add(10);
        set.add(20);
        set.add(10); // Duplicate! Will be ignored.

        // 2. Check if exists (contains)
        System.out.println(set.contains(20)); // Prints true
        System.out.println(set.contains(50)); // Prints false

        // 3. Size (size)
        System.out.println(set.size()); // Prints 2 (only 10 and 20 are in the set)
    }
}
```

---

## 4. Number of Distinct Elements

**The Problem:** Given an array of N elements (e.g., `[5, 2, 5, 2, 8]`), find how many *distinct* (unique) elements there are.

**The HashSet Solution:**
1. Create an empty `HashSet`.
2. Loop through the array and `add()` every element into the HashSet.
3. Because HashSets automatically ignore duplicates, the size of the HashSet at the end will be your answer.
* *Example:* For `[5, 2, 5, 2, 8]`, the HashSet will just hold `{5, 2, 8}`. Its size is 3.

**Complexity:** $O(N)$ time to iterate through the array, $O(N)$ space to store the set.

**Code Example:**
```java
import java.util.HashSet;

public class DistinctCount {
    public static int countDistinct(int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        
        // Dump everything into the set. Duplicates are naturally removed.
        for (int num : arr) {
            set.add(num);
        }
        
        return set.size(); // The size is the number of distinct elements
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 5, 2, 8};
        System.out.println(countDistinct(arr)); // Prints 3 (for elements 5, 2, 8)
    }
}
```

---

## 5. Iterate over HashMap & HashSet

You can easily loop over all the elements inside a HashMap or HashSet.
* **For a HashSet:** You just write a "for-each" loop to go through the items. Note: *They are unordered. You might not get them back in the same order you put them in!*
* **For a HashMap:** You can loop over just the keys (`map.keySet()`), just the values (`map.values()`), or both the keys and values together.

**Code Example:**
```java
// Iterating a HashSet
HashSet<String> set = new HashSet<>();
set.add("Apple"); set.add("Banana");

// Use a For-Each loop
for (String item : set) {
    System.out.println(item); // Note: Order is not guaranteed in HashSets!
}

// Iterating a HashMap
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1); map.put("B", 2);

// Loop through Keys
for (String key : map.keySet()) {
    System.out.println("Key: " + key + ", Value: " + map.get(key));
}
```

---

## 6. Find any pair (i, j) such that A[i] = A[j] & abs(i - j) is minimum

**The Problem:** You have an array (e.g., `A = [7, 1, 3, 7, 1, 7]`). You need to find two identical numbers that are the *closest* to each other in the array. Return the minimum distance (difference in their index). If no identical pairs exist, return `-1`.

**The Logic (from the transcript):**
We want to process the array from left to right. To find out how far the current number is from its *previous occurrence*, we need to remember the last index where we saw each number. What tool is perfect for pairing a "Number" to its "Last Index"? A **HashMap**!

**Step-by-Step Algorithm:**
1. Create `HashMap<Integer, Integer>` to store `Number -> Last Seen Index`.
2. Create a variable `min_distance = Infinity`.
3. Loop through the array with an index `i`. Let the current number be `A[i]`.
4. **Check the HashMap:**
   * If `A[i]` is already in the HashMap (meaning we've seen it before):
     * Calculate distance: `current_distance = i - map.get(A[i])`.
     * If `current_distance < min_distance`, update `min_distance = current_distance`.
   * **Update the HashMap:** Put your current number and its index into the map. (If it was there before, this overwrites it with the newest, closest index—which is exactly what we want!)
5. At the end, if `min_distance` is still Infinity, return `-1`. Otherwise, return `min_distance`.

**Tracing the Example `A = [7, 1, 3, 7, 1, 7]`:**
* `i = 0, A[0] = 7`. Map is empty. Put `(7 -> 0)`.
* `i = 1, A[1] = 1`. Map doesn't have 1. Put `(1 -> 1)`.
* `i = 2, A[2] = 3`. Map doesn't have 3. Put `(3 -> 2)`.
* `i = 3, A[3] = 7`. **Match!** 7 is in map at index 0. Distance = `3 - 0 = 3`. Update `min_distance = 3`. Put `(7 -> 3)` into map.
* `i = 4, A[4] = 1`. **Match!** 1 is in map at index 1. Distance = `4 - 1 = 3`. Distance isn't lower, so `min_distance` remains 3. Put `(1 -> 4)` into map.
* `i = 5, A[5] = 7`. **Match!** 7 is in map at index 3. Distance = `5 - 3 = 2`. `2 < 3`, so update `min_distance = 2`. Put `(7 -> 5)` into map.
* **Final Answer:** `2`. 

**Complexity:**
* **Time Complexity (TC):** $O(N)$ because we loop through the array exactly once, and HashMap lookups are $O(1)$.
* **Space Complexity (SC):** $O(N)$ because, in the worst case (all unique elements), we store all $N$ elements in the HashMap.

**Code Example:**
```java
import java.util.HashMap;

public class MinDistance {
    public static int findMinimumDistance(int[] A) {
        // Map stores: Element Value -> Its latest Index (i)
        HashMap<Integer, Integer> map = new HashMap<>();
        
        int minDistance = Integer.MAX_VALUE; // Start with infinity
        
        for (int i = 0; i < A.length; i++) {
            int currentNum = A[i];
            
            // Have we seen this number before?
            if (map.containsKey(currentNum)) {
                // Calculate distance from current index (i) to the last seen index
                int lastIndex = map.get(currentNum);
                int currentDistance = i - lastIndex;
                
                // Update minimum distance
                minDistance = Math.min(minDistance, currentDistance);
            }
            
            // ALWAYS update the map with the newest, closest index
            map.put(currentNum, i);
        }
        
        // If minDistance never changed, no pair was found
        if (minDistance == Integer.MAX_VALUE) {
            return -1;
        }
        
        return minDistance;
    }

    public static void main(String[] args) {
        int[] A = {7, 1, 3, 7, 1, 7};
        System.out.println("Min Distance: " + findMinimumDistance(A)); // Prints 2
    }
}
```

---
## Practice Problem: Count Distinct Elements
**Problem:** Given an array `A` of `N` integers, return the number of unique elements in the array.

**Solution:**
```java
public class Solution {
    public int solve(int[] A) {
        // Step 1: Create a HashSet
        java.util.HashSet<Integer> uniqueElements = new java.util.HashSet<>();
        
        // Step 2: Iterate through the given array
        for (int i = 0; i < A.length; i++) {
            // Add each element to the HashSet. 
            // It automatically ignores any duplicates!
            uniqueElements.add(A[i]);
        }
        
        // Step 3: The size of the HashSet will be the number of distinct elements
        return uniqueElements.size();
    }
}
```

---
## Practice Problem: Shaggy and Distances
**Problem:** Shaggy has an array `A` consisting of `N` elements. A pair of distinct indices is "special" if elements at those indices are equal. Find a special pair such that the distance between that pair `|i-j|` is minimum. If there is no special pair, return `-1`.

**Solution:**
```java
public class Solution {
    public int solve(int[] A) {
        // Map stores: Element Value -> Its latest Index (i)
        java.util.HashMap<Integer, Integer> map = new java.util.HashMap<>();
        int minDistance = Integer.MAX_VALUE;
        
        for (int i = 0; i < A.length; i++) {
            int currentNum = A[i];
            
            // If we have seen this number before, calculate the difference in indices
            if (map.containsKey(currentNum)) {
                int dist = i - map.get(currentNum);
                minDistance = Math.min(minDistance, dist);
            }
            
            // Always map the number to its most recent index
            map.put(currentNum, i);
        }
        
        // If minDistance was never updated, no special pair exists
        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }
}
```

---
## Practice Problem: First Repeating Element
**Problem:** Given an integer array `A` of size `N`, find the first repeating element in it. We need to find the element that occurs more than once and whose index of the first occurrence is the smallest. If there is no repeating element, return `-1`.

**Solution:**
We can use a Frequency Map (HashMap) to solve this optimally.
1. Build a frequency map by iterating through the array.
2. Iterate through the array a second time, from left to right.
3. The first number we encounter whose frequency in the map is `> 1` is our answer! By reading the array from left to right again, we guarantee we find the repeating element whose *first occurrence* appears earliest in the array.

```java
import java.util.HashMap;

public class Solution {
    public int solve(int[] A) {
        // Step 1: Build the Frequency Map
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        
        for (int i = 0; i < A.length; i++) {
            int num = A[i];
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Step 2: Traverse array again to find the FIRST element with Frequency > 1
        for (int i = 0; i < A.length; i++) {
            int num = A[i];
            if (freqMap.get(num) > 1) {
                return num; // We found the first repeating element!
            }
        }
        
        // If we finish the loop and find nothing, return -1
        return -1;
    }
}
```

---
## Practice Problem: Frequency of Element Query
**Problem:** Given an array `A` representing participants of various contests, and an array `B` containing queries (learners to check), find the frequency of each learner from array `B` in array `A` and return a list containing all these frequencies.

**Solution:**
This directly applies the logic from **Topic 2: Frequency Map**. We map every element in array `A` to how many times it appears. Then, for every query in array `B`, we simply ask the HashMap for the count in instant $O(1)$ time.

```java
import java.util.HashMap;

public class Solution {
    public int[] solve(int[] A, int[] B) {
        // Step 1: Build the Frequency Map from Array A
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        
        for (int i = 0; i < A.length; i++) {
            int num = A[i];
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // Step 2: Prepare the answer array the exact same size as B
        int[] result = new int[B.length];
        
        // Step 3: For every query in B, ask the HashMap for the frequency
        for (int i = 0; i < B.length; i++) {
            int query = B[i];
            // If the query number exists, get its count. If not seen in A, it's 0.
            result[i] = freqMap.getOrDefault(query, 0);
        }
        
        return result;
    }
}
```
