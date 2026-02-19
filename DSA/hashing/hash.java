import java.util.*;

public class hash {
	public static void main(String[] args) {
		// HashMap:
		HashMap<String, Integer> map = new HashMap<>();
		map.put("one", 1);
		map.put("two", 2);
		System.out.println(map.get("one")); // Output: 1
		System.out.println(map.get("two")); // Output: 2
		System.out.println(map.get("three")); // Output: null
		// HashMap functions:
		System.out.println(map.containsKey("one")); // Output: true
		System.out.println(map.containsKey("three")); // Output: false
		System.out.println(map.size()); // Output: 2
		map.remove("one");
		System.out.println(map.containsKey("one")); // Output: false
		map.isEmpty(); // Output: false
		map.clear();
		System.out.println(map.isEmpty()); // Output: true

		// HashSet:
		HashSet<String> set = new HashSet<>();
		set.add("apple");
		set.add("banana");
		System.out.println(set.contains("apple")); // Output: true
		System.out.println(set.contains("orange")); // Output: false
		System.out.println(set.size()); // Output: 2
		set.remove("apple");
		System.out.println(set.contains("apple")); // Output: false
		set.isEmpty(); // Output: false
		set.clear();
		System.out.println(set.isEmpty()); // Output: true
	}
}
