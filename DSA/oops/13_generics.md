# 13 — Java Generics

## Motivation: Structural Polymorphism

Some operations work the same way regardless of the element type:

| Operation | Requirement |
|---|---|
| Reverse an array/list | Works for **any** type |
| Find an element | Needs **equality check** (`equals()`) |
| Sort an array/list | Needs **comparison** (`cmp()`) |
| Copy an array | Source type must be compatible with target type |

**Problem with using `Object` as a parameter type:**
1. **Type information is lost** — need explicit casts on retrieval
2. **List is not homogeneous** — can accidentally mix types

```java
LinkedList list = new LinkedList();
list.insert(new Ticket());
list.insert(new Date());    // accidentally mixed types!
Ticket t = (Ticket) list.head();    // Requires ugly cast
```

---

## Java Generics — Type Variables

Type variables allow functions and classes to be **parameterised by type**.

### Generic reverse

```java
public <T> void reverse(T[] objarr) {
    T tempobj;
    int n = objarr.length;
    for (int i = 0; i < n/2; i++) {
        tempobj = objarr[i];
        objarr[i] = objarr[(n-1)-i];
        objarr[(n-1)-i] = tempobj;
    }
}
```

- `<T>` before the return type means: **"for every type T..."**
- The same code works for `String[]`, `Integer[]`, `Date[]`, etc.

### Generic find

```java
public <T> int find(T[] objarr, T o) {
    for (int i = 0; i < objarr.length; i++) {
        if (objarr[i] == o) return i;
    }
    return -1;
}
```

Now searching for a value of an incompatible type is a **compile-time error**.

### Generic arraycopy (same type)

```java
public static <T> void arraycopy(T[] src, T[] tgt) {
    int limit = Math.min(src.length, tgt.length);
    for (int i = 0; i < limit; i++) tgt[i] = src[i];
}
```

### More generous arraycopy (subtype relationship)

```java
public static <S extends T, T> void arraycopy(S[] src, T[] tgt) {
    int limit = Math.min(src.length, tgt.length);
    for (int i = 0; i < limit; i++) tgt[i] = src[i];
}

// Example:
Ticket[] tktarr   = new Ticket[10];
ETicket[] etktarr = new ETicket[10];   // ETicket extends Ticket
arraycopy(etktarr, tktarr);   // OK: S=ETicket, T=Ticket
arraycopy(tktarr, etktarr);   // Compile-time ERROR!
```

---

## Generic Classes (Polymorphic Data Structures)

```java
public class LinkedList<T> {
    private int size;
    private Node first;

    public T head()              { ... }
    public void insert(T newdata){ ... }

    private class Node {
        private T data;
        private Node next;
    }
}
```

- `T` applies to the **entire class**
- `Node.data`, `head()`'s return type, `insert()`'s argument — all use the **same T**

### Instantiation

```java
LinkedList<Ticket> ticketlist = new LinkedList<Ticket>();
LinkedList<Date>   datelist   = new LinkedList<Date>();

ticketlist.insert(new Ticket());   // type-safe
datelist.insert(new Date());       // type-safe

Ticket t = ticketlist.head();      // NO cast needed!
```

---

## Wildcard Type Variable `?`

When you don't need to name the type variable explicitly, use `?`:

```java
// Print any LinkedList regardless of its element type
public static void printlist(LinkedList<?> l) {
    Object o;
    Iterator i = l.get_iterator();
    while (i.has_next()) {
        o = i.get_next();
        System.out.println(o);
    }
}
```

`?` = "some unknown type" — avoids unnecessary type quantification.

### Bounded wildcards

```java
// Upper bound — accept any LinkedList whose elements are Shape subtypes
public static void drawAll(LinkedList<? extends Shape> l) { ... }

// Lower bound — accept any LinkedList whose elements are supertypes of T
public static <T, ? super T> void listcopy(LinkedList<T> src, LinkedList<?> tgt) { ... }
```

---

## Generics are NOT Covariant

Unlike arrays, generic classes do **not** follow covariance:

```java
// Arrays — covariant (can cause runtime issues)
ETicket[] elecarr    = new ETicket[10];
Ticket[]  ticketarr  = elecarr;   // OK at compile time, risky!

// Generics — NOT covariant (safe)
LinkedList<ETicket> elist  = new LinkedList<>();
LinkedList<Ticket>  tlist  = elist;   // COMPILE ERROR!
```

Use `<? extends Ticket>` to get covariant-like behaviour safely.

---

## Hiding Type Variables — Watch Out!

```java
public class LinkedList<T> {
    // WRONG: <T> here creates a NEW T that shadows the class's T
    public <T> void insert(T newdata) { ... }

    // CORRECT: no type quantifier — uses the class's T
    public void insert(T newdata) { ... }
}
```

Contrast with a static method (which has no class T to use):
```java
public static <T> void arraycopy(T[] src, T[] tgt) { ... }   // OK here
```

---

## Summary

| Feature | Description |
|---|---|
| `<T>` on method | Type quantifier: "for every type T" |
| `<T>` on class | Type parameter: all uses of `T` in the class refer to the same type |
| `?` wildcard | Unknown type; avoids naming it when not needed |
| `? extends T` | Upper bounded wildcard — subtypes of T |
| `? super T` | Lower bounded wildcard — supertypes of T |
| Not covariant | `LinkedList<String>` is NOT compatible with `LinkedList<Object>` |
| Benefit over `Object` | No casts; compile-time type safety; homogeneous collections |
