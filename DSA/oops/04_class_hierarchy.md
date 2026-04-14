# 04 — The Java Class Hierarchy

## Multiple Inheritance Problem

**Can a subclass extend multiple parent classes?**

```
C1          C2
public int f();  public int f();
      \        /
       C3 extends C1, C2
```

Problem: if `f()` is not overridden in `C3`, which `f()` to use?

- **Java:** does NOT allow multiple inheritance (class `extends` only one parent)
- **C++:** allows it, if there is no conflict

---

## Java Class Hierarchy

- No multiple inheritance → class hierarchy forms a **tree**
- Every class implicitly inherits from a universal root: **`Object`**

```
          Object
         /  |   \
   Employee Date  ...
       |
    Manager
```

### Useful methods in `Object`

```java
public boolean equals(Object o)   // defaults to pointer equality (==)
public String  toString()         // converts instance variables to String
```

- For Java objects `x` and `y`, `x == y` invokes `x.equals(y)`
- `System.out.println(o + "")` implicitly calls `o.toString()`

---

## Using `Object` for Generic Functions

Because all classes inherit from `Object`, you can write functions that work on any object:

```java
public int find(Object[] objarr, Object o) {
    for (int i = 0; i < objarr.length; i++) {
        if (objarr[i] == o) return i;   // == calls .equals() via dynamic dispatch
    }
    return -1;
}
```

> If a class overrides `equals()`, dynamic dispatch will use the redefined version.

---

## Overriding `equals()` Correctly

⚠️ Common mistake:

```java
// WRONG — this does NOT override Object.equals(Object o)
public boolean equals(Date d) { ... }
```

This has a different signature and only *overloads*, not *overrides*.

✅ Correct way:

```java
@Override
public boolean equals(Object d) {
    if (d instanceof Date) {
        Date myd = (Date) d;
        return (this.day == myd.day &&
                this.month == myd.month &&
                this.year == myd.year);
    }
    return false;
}
```

Key steps:
1. Accept `Object` parameter (not `Date`) to match the parent signature
2. Use `instanceof` to check runtime type
3. Cast to `Date` to access its fields

---

## Overriding Picks the "Closest" Match

If `Employee` defines `equals(Employee e)` and `Manager` inherits it without overriding:

```java
Manager m1 = new Manager(...);
Manager m2 = new Manager(...);
if (m1.equals(m2)) { ... }
```

- Both `equals(Employee e)` and `equals(Object o)` are compatible
- Java uses the **closest match** → `equals(Employee e)` is chosen

---

## Summary

| Topic | Key Point |
|---|---|
| Multiple inheritance | **Not allowed** in Java (only single class `extends`) |
| Class hierarchy | Forms a tree rooted at `Object` |
| `Object.equals()` | Default = pointer equality; override for value equality |
| `Object.toString()` | Called implicitly by `println` |
| Correct override | Match signature exactly: `equals(Object o)` |
| Overriding resolution | Java picks the closest matching signature |
