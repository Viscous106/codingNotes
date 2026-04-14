# 08 — Interfaces (Advanced)

## Recap: What is an Interface?

- A purely abstract class — all methods are abstract (originally)
- A class **implements** an interface by providing concrete code for each abstract method
- A class can implement **multiple interfaces**
- Interfaces describe a specific "slice" of capabilities

```java
public interface Comparable {
    public abstract int cmp(Comparable s);
    // return -1 if this < s, 0 if equal, +1 if this > s
}
```

---

## Exposing Limited Capabilities

Interfaces let you say: "I only care that this type supports *these* operations."

```java
public class SortFunctions {
    public static void quicksort(Comparable[] a) {
        // Only needs to call a[i].cmp(a[j])
        // All other details of the element type are irrelevant
    }
}
```

**Limitation:** Cannot express the *intended behaviour* of `cmp()` in code — just the signature.

---

## Java Later Added Concrete Methods to Interfaces

### 1. Static Functions

```java
public interface Comparable {
    public static String cmpdoc() {
        return "Return -1 if this < s, 0 if equal, +1 if this > s.";
    }
    public abstract int cmp(Comparable s);
}
```

- Cannot access instance variables (no object needed)
- Called as `Comparable.cmpdoc()` — directly on the interface name

### 2. Default Functions

```java
public interface Comparable {
    public default int cmp(Comparable s) {
        return 0;   // default: treat all as equal
    }
}
```

- Provides a **default implementation** that implementing classes may override
- Called like a normal method on an object: `a[i].cmp(a[j])`

---

## Conflicts from Multiple Interface Implementation

When two interfaces both define a `default` method with the same name, a conflict arises:

```java
public interface Person {
    public default String getName() { return "No name"; }
}
public interface Designation {
    public default String getName() { return "No designation"; }
}
public class Employee implements Person, Designation {
    // MUST provide its own getName() to resolve conflict
    public String getName() { return "Alice"; }
}
```

**Resolution rule: The implementing class must provide a fresh implementation.**

---

## "Class Wins" Rule

If a conflict exists between a **superclass method** and a **default interface method**, the class method wins:

```java
public class Person {
    public String getName() { return "No name"; }
}
public interface Designation {
    public default String getName() { return "No designation"; }
}
public class Employee extends Person implements Designation {
    // getName() is inherited from class Person — no conflict resolution needed
}
```

> This rule exists for **backward compatibility** — adding default methods to interfaces shouldn't break existing code that extends a class.

---

## Summary

| Feature | Description |
|---|---|
| Abstract method | Must be implemented by any class implementing the interface |
| Static method | Belongs to the interface; invoked as `Interface.method()` |
| Default method | Provides a fallback; may be overridden by implementing class |
| Interface-interface conflict | Implementing class must resolve by providing its own implementation |
| Class-interface conflict | **Class wins** — method inherited from the class is used |
| Design concern | Adding `default` methods reintroduces complexity similar to multiple inheritance |
