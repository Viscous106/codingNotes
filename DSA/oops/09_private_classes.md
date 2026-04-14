# 09 — Private (Inner) Classes

## Nested Objects

An instance variable can be of a user-defined type:

```java
public class Employee {
    private String name;
    private double salary;
    private Date joindate;    // nested object
}

public class Date {
    private int day, month, year;
}
```

Here `Date` is a **public class**, so it's accessible to everyone.  
But does every helper class need to be public?

---

## Motivation for Private Classes

Consider a `LinkedList` built using `Node`:

```java
public class Node {
    public Object data;
    public Node next;
}

public class LinkedList {
    private int size;
    private Node first;

    public Object head() {
        if (first != null) {
            Object val = first.data;
            first = first.next;
            return val;
        }
        return null;
    }
}
```

**Why should `Node` be `public`?**
- External users don't need to know about `Node`
- If we want to change to a doubly-linked list (add `prev`), `Node`'s structure changes — but `LinkedList`'s interface doesn't

---

## Private Inner Class

Move `Node` inside `LinkedList` and make it `private`:

```java
public class LinkedList {
    private int size;
    private Node first;

    public Object head() { ... }
    public void insert(Object newdata) { ... }

    private class Node {           // inner class — NOT visible outside LinkedList
        public Object data;
        public Node next;
        // could add: public Node prev;  for doubly-linked list
    }
}
```

Key properties of inner classes:
- **Not visible outside** the enclosing class
- Also called an **inner class**
- Objects of the private class can **see private components of the enclosing class**

---

## Private Class + Interface Pattern

Combine private inner classes with interfaces for **controlled, typed access**:

```java
public interface QIF {
    public abstract int getStatus(int trainno, Date d);
}

public class RailwayBooking {
    private BookingDB railwaydb;     // private database

    // login returns an object whose capabilities are defined by interface QIF
    public QIF login(String username, String password) {
        if (valid_login(username, password)) {
            return new QueryObject();
        }
        return null;
    }

    private class QueryObject implements QIF {
        public int getStatus(int trainno, Date d) {
            // Can access railwaydb because it's in the enclosing class
            return railwaydb.lookup(trainno, d);
        }
    }
}
```

- The user sees only `QIF` — the interface — not the private `QueryObject`
- The implementation details are completely hidden

---

## Summary

| Concept | Key Point |
|---|---|
| Nested object | An instance variable of a user-defined type |
| Private class | Inner class hidden from outside the enclosing class |
| Inner class access | Can access private members of the enclosing class |
| Pattern: private class + interface | Expose controlled capabilities through an interface; hide implementation in a private class |
| Benefit | Additional degree of data encapsulation |
