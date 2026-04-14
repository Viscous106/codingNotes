# 07 — Abstract Classes and Interfaces

## Motivation — Grouping Related Classes

Suppose `Circle`, `Square`, and `Rectangle` are all shapes.  
We want to ensure every shape has a `perimeter()` method.

**Bad approach — rely on programmer discipline:**
```java
public class Shape {
    public double perimeter() { return -1.0; }  // fake implementation
}
```
If a subclass doesn't override it, we silently get `-1.0`.

---

## Abstract Classes

**Better approach — force subclasses to implement the method:**

```java
public abstract class Shape {
    public abstract double perimeter();   // no body!
}
```

Rules:
- A method declared `abstract` has **no body**
- Any class with an `abstract` method **must itself be declared `abstract`**
- You **cannot create objects** of an abstract class (`new Shape()` is illegal)
- You **can** declare variables of an abstract type: `Shape s;`

```java
Shape[] shapearr = new Shape[3];
shapearr[0] = new Circle(...);      // OK — Circle is concrete
shapearr[1] = new Square(...);
shapearr[2] = new Rectangle(...);

for (int i = 0; i < shapearr.length; i++) {
    System.out.println(shapearr[i].perimeter());
    // dynamic dispatch calls the correct perimeter()
}
```

---

## Abstract Classes for Generic Capabilities

Use abstract classes to describe **capabilities** needed by generic functions:

```java
public abstract class Comparable {
    public abstract int cmp(Comparable s);
    // returns -1 if this < s, 0 if equal, +1 if this > s
}

public class SortFunctions {
    public static void quicksort(Comparable[] a) {
        // ... uses a[i].cmp(a[j]) for comparisons
    }
}
```

Any class that `extends Comparable` and implements `cmp()` can now be sorted generically.

---

## The Multiple Inheritance Problem

```java
// Circle already extends Shape
public class Circle extends Shape { ... }

// What if we also want to sort circles?
// Circle would need to extend Comparable too — BUT Java forbids multiple class inheritance!
```

Solution: **Interfaces**

---

## Interfaces

An **interface** is like an abstract class with **no concrete components** (no instance variables, no method bodies).

```java
public interface Comparable {
    public abstract int cmp(Comparable s);
}
```

A class **implements** an interface (instead of extending it):

```java
public class Circle extends Shape implements Comparable {
    public double perimeter() { ... }
    public int cmp(Comparable s) { ... }
}
```

Key rules:
- A class can **extend only one class** (single inheritance)
- A class can **implement multiple interfaces** (multiple interface implementation)

```java
public class Circle extends Shape implements Comparable, Serializable { ... }
```

---

## Abstract Class vs Interface

| Feature | Abstract Class | Interface |
|---|---|---|
| Can have concrete methods | ✅ Yes | ❌ No (originally) |
| Can have instance variables | ✅ Yes | ❌ No |
| A class can `extends` | Only **one** | — |
| A class can `implements` | — | **Multiple** |
| Use when | Shared code + IS-A relationship | Shared capability / contract |

---

## Summary

| Concept | Key Point |
|---|---|
| `abstract` method | No body; subclass *must* implement |
| `abstract` class | Cannot be instantiated; can still be used as a type |
| Interface | Purely abstract class — describes capabilities |
| `implements` | A class provides concrete code for all interface methods |
| Multiple interfaces | A class can implement any number of interfaces |
