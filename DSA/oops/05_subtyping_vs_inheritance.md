# 05 — Subtyping vs Inheritance

## Two Distinct Concepts

Although Java's class hierarchy implements **both**, they are conceptually different:

| Concept | Definition |
|---|---|
| **Subtyping** | Compatibility of *interfaces* — a subtype can be used wherever the supertype is expected |
| **Inheritance** | Reuse of *implementations* — subtype's code is written in terms of supertype's code |

---

## Subtyping

> B is a subtype of A if **every function that can be invoked on an object of type A can also be invoked on an object of type B**.

In other words, the capabilities of the subtype are a **superset** of the main type.

**Example in Java:**
```java
Employee e = new Manager(...);   // Legal: Manager is a subtype of Employee
```

This works because `Manager` supports *at least* everything `Employee` supports (plus more).

---

## Inheritance

> B inherits from A if **some functions for B are written in terms of functions of A**.

This is about *code reuse*, not interface compatibility.

**Example:**
```java
// Manager.bonus() is written using Employee.bonus()
double bonus(float percent) {
    return 1.5 * super.bonus(percent);
}
```

---

## Subtyping ≠ Inheritance — The Classic Example

Consider:
- `Queue`: methods `insertRear`, `deleteFront`
- `Stack`: methods `insertFront`, `deleteFront`
- `Deque`: methods `insertFront`, `deleteFront`, `insertRear`, `deleteRear`

**Subtyping relationships:**
- `Deque` has **more functionality** than `Queue` or `Stack`
- Therefore `Deque` is a **subtype of both** `Queue` and `Stack`

**Inheritance relationships:**
- `Queue` can suppress two functions of `Deque` and use it as a queue
- `Stack` can suppress two functions of `Deque` and use it as a stack
- So both **`Queue` and `Stack` inherit from `Deque`**

> This means **subtyping goes in the opposite direction from inheritance** in this case!  
> Deque is a subtype of Queue, but Queue *inherits* from Deque.

---

## The Blur in Java

Using a single class hierarchy to represent both subtyping and inheritance **blurs the distinction**.

In Java:
- A subclass is automatically a subtype
- A subclass automatically inherits code

These two ideas are tied together even when they conceptually shouldn't be.

---

## Summary

| Topic | Key Point |
|---|---|
| Subtyping | About interface compatibility — "can be used in place of" |
| Inheritance | About code reuse — "written in terms of" |
| Java class hierarchy | Implements *both* simultaneously |
| Risk | Conflating the two can lead to incorrect designs |
