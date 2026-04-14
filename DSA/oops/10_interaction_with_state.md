# 10 — Controlled Interaction with Objects

## Encapsulation Revisited

Encapsulation: internal data is `private`; access is through `public` methods.

```java
public class Date {
    private int day, month, year;

    public void setDate(int d, int m, int y) {
        // Validate the d-m-y combination here
    }
    public void getDay()   { ... }
    public void getMonth() { ... }
    public void getYear()  { ... }
}
```

But does standard encapsulation always provide **sufficient control**?

---

## The Railway Booking Problem

Consider an object that stores train reservation info:

```java
public class RailwayBooking {
    private BookingDB railwaydb;

    public int getStatus(int trainno, Date d) {
        // Returns number of available seats
    }
}
```

**Problem:** To prevent bots from spamming queries, we want users to log in first — and *connect the query to the login status*.

Simply making `getStatus()` public doesn't track who is logged in.

---

## Solution: Return an Object on Login

**Idea:** When a user logs in successfully, give them an **object** that can perform queries.  
This object is created from a **private class** (so its internal structure is hidden).

```java
public interface QIF {
    public abstract int getStatus(int trainno, Date d);
}

public class RailwayBooking {
    private BookingDB railwaydb;

    // Returns an object with querying capability — typed as interface QIF
    public QIF login(String username, String password) {
        if (valid_login(username, password)) {
            return new QueryObject();
        }
        return null;
    }

    private class QueryObject implements QIF {
        public int getStatus(int trainno, Date d) {
            // Accesses railwaydb from enclosing class
            return railwaydb.lookup(trainno, d);
        }
    }
}
```

**Flow:**
1. User calls `login()` → receives a `QIF` object (actually a `QueryObject`)
2. User can call `getStatus()` using that object
3. User has **no idea** `QueryObject` exists — they only see the `QIF` interface

---

## Interaction with State — Limiting Queries

The object returned at login can **remember the interaction state** using its own instance variables:

```java
private class QueryObject implements QIF {
    private int numqueries = 0;
    private static final int QLIM = 10;   // max 10 queries per login

    public int getStatus(int trainno, Date d) {
        if (numqueries < QLIM) {
            numqueries++;
            return railwaydb.lookup(trainno, d);
        } else {
            // Return error / throw exception
        }
    }
}
```

The **state of the interaction** (how many queries have been made) is tracked inside the returned object.

---

## Design Pattern Summary

```
CLIENT                RAILWAYBOOKING              QUERYOBJECT
  |                        |                           |
  | login(u, p) ---------> |                           |
  |                        | --- new QueryObject() --> |
  | <-- QIF object ------  |                           |
  |                        |                           |
  | getStatus(t, d) -------------------------------------> |
  |                                                    |----> railwaydb.lookup()
  | <-- result -------------------------------------------   |
```

Key points:
- External user interacts only through the `QIF` interface
- The private `QueryObject` class is invisible to the client
- The `QueryObject` can access the enclosing class's private `railwaydb`
- Instance variables in `QueryObject` track the state of the session

---

## Summary

| Concept | Key Point |
|---|---|
| Standard encapsulation | `private` fields + `public` methods |
| Controlled interaction | Return an object (of a private class) on authentication |
| Interface + private class | Caller sees only the interface; implementation is hidden |
| Interaction with state | The returned object maintains session state in its own fields |
