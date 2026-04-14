# 12 — Iterators

## The Problem: Traversing a List

A generic `Linearlist` may have different internal implementations:

```java
// Array-based
public class Linearlist {
    private Object[] data = new Object[100];
    private int size;
    ...
}

// Linked list-based
public class Linearlist {
    private Node head;
    private int size;
    private class Node { ... }
    ...
}
```

We want to loop through all elements — but:
1. Internal data is **private** (no direct access)
2. We **don't know which implementation** is in use

---

## The Iterator Interface

Abstractly, traversal looks like:

```
start at the beginning of the list;
while (there is a next element) {
    get the next element;
    do something with it;
}
```

Encapsulate this in an **interface**:

```java
public interface Iterator {
    public abstract boolean has_next();
    public abstract Object  get_next();
}
```

---

## Implementing Iterator Inside Linearlist

The iterator needs to **remember its current position** — but position depends on the implementation:
- Array: an index `i`
- Linked list: a `Node` pointer

**Key insight:** Create an `Iterator` as an **inner class object** and export it.

```java
public class Linearlist {
    private Node head;
    ...

    // Export a fresh iterator object
    public Iterator get_iterator() {
        return new Iter();
    }

    private class Iter implements Iterator {
        private Node position = head;   // starts at the beginning

        public boolean has_next() {
            return (position != null);
        }
        public Object get_next() {
            Object val = position.data;
            position = position.next;
            return val;
        }
    }

    private class Node { ... }
}
```

---

## Using the Iterator

```java
Linearlist l = new Linearlist();
// ... fill the list ...

Iterator i = l.get_iterator();
while (i.has_next()) {
    Object o = i.get_next();
    // do something with o
}
```

---

## Nested Loops — Multiple Iterators

Each call to `get_iterator()` returns a **fresh, independent** iterator object:

```java
Iterator i = l.get_iterator();
while (i.has_next()) {
    Object oi = i.get_next();
    Iterator j = l.get_iterator();   // new iterator for inner loop
    while (j.has_next()) {
        Object oj = j.get_next();
        // do something with oi and oj
    }
}
```

---

## Java's Built-in For-Each

Java's enhanced for loop implicitly uses an iterator:

```java
for (Type x : collection) {
    // do something with x
}
```

The collection must implement `java.lang.Iterable`, which requires a `iterator()` method.

---

## Summary

| Concept | Key Point |
|---|---|
| Problem | Need to traverse a list without exposing its internal structure |
| `Iterator` interface | Defines `has_next()` and `get_next()` |
| Inner class `Iter` | Remembers position; implements Iterator |
| `get_iterator()` | Returns a fresh iterator; enables nested loops |
| Interaction with state | Iterator holds position — classic example of stateful interaction |
| Java for-each | Implicitly uses iterator (`Iterable` interface) |
