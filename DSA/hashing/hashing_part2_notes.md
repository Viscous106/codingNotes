# Hashing Part 2: Pair Sums and Subarrays

Welcome to Part 2! This guide covers advanced hashing techniques focusing on two classic problem types: **Pair Sums** and **Subarray Sums with Prefix Arrays**.

---

## 1. Check if Pair Sum exists

**The Problem:** Given an array `A` and a target sum `K`, check if there exists any pair of distinct indices `(i, j)` such that `A[i] + A[j] == K`. Return `true` if it exists, otherwise `false`.

**The Logic:**
Instead of using two nested loops ($O(N^2)$), we can use a **HashSet**. As we iterate through the array, for any number `A[i]`, we need its pair partner to be exactly `K - A[i]`. We can check if we've already seen this partner by looking in our HashSet! 
1. Loop through the array. 
2. Let the required partner be `target = K - A[i]`.
3. If `target` is in the set, we found our pair! Return `true`.
4. If not, add `A[i]` to the set and continue.

**Code Example:**
```java
import java.util.HashSet;

public class PairSum {
    public static boolean checkPairExists(int[] A, int K) {
        HashSet<Integer> seen = new HashSet<>();
        
        for (int i = 0; i < A.length; i++) {
            int partner = K - A[i];
            
            // Check if we've seen the partner before
            if (seen.contains(partner)) {
                return true;
            }
            // Add current number to our seen list
            seen.add(A[i]);
        }
        
        return false;
    }
}
```

---

## 2. Count of Pair Sums

**The Problem:** Instead of just checking if a pair exists, count *how many* distinct pairs `(i, j)` add up to `K`.

**The Logic:**
If we just want to count, a HashSet isn't enough because duplicates matter here. We must use a **Frequency Map (HashMap)**.
If we need `K - A[i]` and we've seen that number 3 times before, it means we can form 3 valid pairs right now!
1. Initialize a `count = 0` and a HashMap for frequencies.
2. For each element, find `partner = K - A[i]`.
3. If the partner exists in the map, add its frequency to `count`.
4. Then, add the current element `A[i]` to the map (update its frequency).

**Code Example:**
```java
import java.util.HashMap;

public class CountPairSum {
    public static int countPairs(int[] A, int K) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        int count = 0;
        
        for (int i = 0; i < A.length; i++) {
            int partner = K - A[i];
            
            // If the partner exists, we can form 'freq' number of pairs
            count += freqMap.getOrDefault(partner, 0);
            
            // Update the frequency of the current element
            freqMap.put(A[i], freqMap.getOrDefault(A[i], 0) + 1);
        }
        
        return count;
    }
}
```

---

## 3. Check if there exists a Subarray with Sum = 0

**The Problem:** Given an array, check if any contiguous subarray adds up to 0.

**The Magic of Prefix Sums:** 
A **Prefix Sum** is the running sum of the array from the beginning up to the current index. 
*Rule 1:* If the running sum becomes `0` at any point, the subarray from index 0 to current is 0.
*Rule 2:* If the running sum **repeats** a value we've seen before, it means the elements perfectly canceled each other out in between to sum back to that value. Thus, the subarray in between has a sum of `0`!

**The Logic:** 
1. Keep a running track of the `prefix_sum`.
2. Use a **HashSet** to remember the prefix sums we've seen.
3. If `prefix_sum == 0` or we've seen this `prefix_sum` before, return `true`.
4. Else, add the `prefix_sum` to the set.

**Code Example:**
```java
import java.util.HashSet;

public class SubarraySumZero {
    public static boolean hasZeroSumSubarray(int[] A) {
        HashSet<Long> seenPrefixes = new HashSet<>();
        long currentSum = 0;
        
        for (int i = 0; i < A.length; i++) {
            currentSum += A[i];
            
            // If sum is 0, or we've seen this exact sum before
            if (currentSum == 0 || seenPrefixes.contains(currentSum)) {
                return true;
            }
            
            seenPrefixes.add(currentSum);
        }
        
        return false;
    }
}
```

---

## 4. Longest Subarray with Sum = 0

**The Problem:** Find the *length* of the longest contiguous subarray that adds up to 0.

**The Logic:**
Instead of just remembering *if* we've seen a prefix sum, we need to remember *where* we first saw it so we can calculate the distance (length). So, we use a **HashMap** storing: `Prefix Sum -> First Index`.
1. Keep track of the `currentSum`.
2. If `currentSum == 0`, the length so far is `i + 1`. This is because the whole array up to `i` sums to 0. Update our `maxLength`.
3. If we've seen the `currentSum` before, the subarray between the first index and the current index `i` has sum 0. The length is `i - map.get(currentSum)`. Update `maxLength`.
4. **Important:** Only add the `currentSum` to the map if it's NOT already there. We want to keep the *earliest* index to get the longest possible length!

**Code Example:**
```java
import java.util.HashMap;

public class LongestZeroSum {
    public static int longestSubarray(int[] A) {
        // Map stores: Prefix Sum -> Earliest Index
        HashMap<Long, Integer> firstSeen = new HashMap<>();
        long currentSum = 0;
        int maxLength = 0;
        
        for (int i = 0; i < A.length; i++) {
            currentSum += A[i];
            
            if (currentSum == 0) {
                // If sum from START is zero, length is i + 1
                maxLength = i + 1;
            } else if (firstSeen.containsKey(currentSum)) {
                // If we've seen this sum before, calculate the length of the subarray in between
                int length = i - firstSeen.get(currentSum);
                maxLength = Math.max(maxLength, length);
            } else {
                // Only put it in the map if it's the first time we're seeing this sum!
                firstSeen.put(currentSum, i);
            }
        }
        
        return maxLength;
    }
}
```

---

## 5. Check if there exists a Subarray with Sum = K

**The Problem:** Check if any subarray adds up to a specific target `K`.

**The Logic:**
This is the generalized version of Topic 3.
If our current prefix sum is `currentSum`, and we want a subarray that sums to `K` ending exactly where we are, it means we need to chop off a prefix that equals `currentSum - K`.
Have we seen a prefix sum equal to `currentSum - K` before? We can check our **HashSet**!

**Code Example:**
```java
import java.util.HashSet;

public class SubarraySumK {
    public static boolean hasSubarrayWithSumK(int[] A, int K) {
        HashSet<Long> seenPrefixes = new HashSet<>();
        long currentSum = 0;
        
        for (int i = 0; i < A.length; i++) {
            currentSum += A[i];
            
            // 1. Is the sum exactly K from the beginning?
            if (currentSum == K) {
                return true;
            }
            
            // 2. Have we seen a prefix sum of (currentSum - K)?
            long targetPrefix = currentSum - K;
            if (seenPrefixes.contains(targetPrefix)) {
                return true;
            }
            
            // 3. Add current prefix sum to the set for future elements to use
            seenPrefixes.add(currentSum);
        }
        
        return false;
    }
}
```
