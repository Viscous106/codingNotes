# 06 — Java Modifiers

## Overview

Java modifiers control encapsulation and sharing:

| Modifier | Applies To | Purpose |
|---|---|---|
| `public` | class, field, method | Accessible from anywhere |
| `private` | field, method | Accessible only within the class |
| `static` | field, method | Exists without creating objects |
| `final` | field, method, class | Cannot be changed / cannot be overridden |

---

## `public` vs `private`

Encapsulation rule of thumb:
- **Instance variables → `private`**
- **Accessor/mutator methods → `public`**

```java
public class Stack {
    private int[] values;   // private data
    private int tos;        // top of stack
    private int size;

    public void push(int i)    { ... }
    public int  pop()          { ... }
    public boolean is_empty()  { return (tos == 0); }
}
```

### Private methods — do they make sense? ✅

Yes! Helper methods that are internal implementation details should be `private`.

```java
public class Stack {
    public void push(int i) {
        if (stack_full()) {
            extend_stack();        // private helper
        }
        // normal push logic
    }

    private boolean stack_full() { return (tos == size); }
    private void extend_stack()  { /* allocate more space */ }
}
```

---

## Accessor and Mutator Methods

Provide individual `get` + `set` methods per instance variable — but be careful:

```java
public class Date {
    private int day, month, year;

    // Separate setters allow INCONSISTENT state (bad!)
    public void setDay(int d)   { ... }
    public void setMonth(int m) { ... }
    public void setYear(int y)  { ... }
}
```

**Problem:** caller could set an invalid combination like `day=31, month=2`.

✅ **Better:** Use a combined update method that validates the entire state:

```java
public void setDate(int d, int m, int y) {
    // Validate d-m-y combination first
    ...
}
```

---

## `static` Components

`static` fields and methods **belong to the class, not to any particular object**.

Use cases:
- Library / utility functions: `Math.sqrt()`, `Arrays.sort()`
- Constants: `Math.PI`, `Integer.MAX_VALUE`
- Internal bookkeeping shared across all objects

### Private static — internal counter example

```java
public class Order {
    private static int lastorderid = 0;  // shared across all Order objects
    private int orderid;

    public Order(...) {
        lastorderid++;
        orderid = lastorderid;           // unique id per order
    }
}
```

> ⚠️ **Watch out for concurrent updates** to `static` fields in multithreaded programs!

---

## `final` Components

`final` means the value **cannot be changed after initialisation**.

| Usage | Meaning |
|---|---|
| `final` field | Constant — e.g., `Math.PI`, `Integer.MAX_VALUE` |
| `final` method | **Cannot be overridden** by a subclass |
| `final` class | Cannot be subclassed |

```java
public final double bonus(float percent) {
    return (percent / 100.0) * salary;
    // No subclass can override this
}
```

> Unlike Python, Java does not allow redefining methods at runtime — `final` makes this explicit.

---

## Summary

| Modifier | Key Behaviour |
|---|---|
| `private` | Field/method hidden outside the class |
| `public` | Field/method accessible from anywhere |
| Private methods | Valid! Used as internal helpers |
| `static` | Exists at class level, without objects |
| Private `static` | Common for counters/serial numbers across objects |
| `final` field | Constant, cannot change |
| `final` method | Cannot be overridden by subclasses |
