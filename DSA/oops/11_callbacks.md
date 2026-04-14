# 11 — Callbacks

## What is a Callback?

A **callback** is when object A creates object B to run in parallel, and B **notifies A when it's done**.

Scenario:
1. `Myclass m` creates a `Timer t`
2. `m` starts `t` to run in parallel (m continues running)
3. When `t` finishes, it calls back to `m` using a pre-agreed method (e.g., `timerdone()`)

---

## Naïve Implementation (Timer specific to Myclass)

```java
public class Myclass {
    public void f() {
        Timer t = new Timer(this);   // pass self as owner
        t.start();
        // continues doing other work...
    }

    public void timerdone() {
        // Called back by Timer when it finishes
    }
}

public class Timer implements Runnable {
    private Myclass owner;

    public Timer(Myclass o) {
        owner = o;
    }

    public void start() {
        // ... do timer work ...
        owner.timerdone();   // callback!
    }
}
```

**Problem:** `Timer` is tightly coupled to `Myclass`. Can't reuse it for other classes.

---

## Generic Timer Using `Object`

Make the owner parameter of type `Object` (universal supertype):

```java
public class Timer implements Runnable {
    private Object owner;

    public Timer(Object o) { owner = o; }

    public void start() {
        // ...
        ((Myclass) owner).timerdone();   // requires a cast!
    }
}
```

**Problem:** Still requires casting to `Myclass`, so it's not truly generic.

---

## Generic Timer Using an Interface ✅

Define an interface that specifies the callback method:

```java
public interface Timerowner {
    public abstract void timerdone();
}
```

Modify `Myclass` to implement `Timerowner`:

```java
public class Myclass implements Timerowner {
    public void f() {
        Timer t = new Timer(this);
        t.start();
    }

    public void timerdone() {
        // Called when timer finishes
    }
}
```

Modify `Timer` so that `owner` is typed as `Timerowner`:

```java
public class Timer implements Runnable {
    private Timerowner owner;

    public Timer(Timerowner o) {
        owner = o;
    }

    public void start() {
        // ...
        owner.timerdone();   // no cast needed!
    }
}
```

**Now `Timer` works with ANY class that implements `Timerowner`.**

---

## Interaction Diagram

```
Myclass m            Timer t
    |                    |
    | new Timer(this) -> |
    |                    |
    | t.start() -------> |
    |                    |  (runs in parallel)
    |                    |
    | <-- timerdone() -- |  (callback when done)
```

---

## Summary

| Concept | Key Point |
|---|---|
| Callback | Spawned object notifies its owner (or another object) when done |
| Naïve approach | Timer tied to specific class — not reusable |
| Using `Object` owner | Generic but requires unsafe cast |
| Using interface | **Cleanest solution** — no cast, fully generic |
| `Timerowner` interface | Defines the contract for receiving a callback |
| Extra flexibility | The object notified doesn't have to be the one that created the Timer |
