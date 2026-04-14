# 15 — Java Generics at Runtime (Type Erasure)

## Type Erasure

Java generics are a **compile-time feature only**.  
At runtime, **type variables are erased** (removed).

| At compile time | At runtime |
|---|---|
| `LinkedList<T>` | `LinkedList<Object>` |
| `LinkedList<? extends Shape>` | `LinkedList<Shape>` |

**Consequence:** You cannot use generics in `instanceof` checks:

```java
// ILLEGAL — type info is gone at runtime:
if (s instanceof LinkedList<String>) { ... }
if (o instanceof T)                  { ... }
```

---

## Erasure and `getClass()`

Because all versions of `LinkedList<T>` become `LinkedList<Object>` at runtime:

```java
LinkedList<Employee> o1 = new LinkedList<>();
LinkedList<Date>     o2 = new LinkedList<>();

if (o1.getClass() == o2.getClass()) {
    // TRUE — they are both just LinkedList at runtime
}
```

---

## Erasure and Overloading

Because the types are erased, you **cannot overload** using different generic instantiations:

```java
// ILLEGAL — both signatures become printlist(LinkedList) after erasure:
public class Example {
    public void printlist(LinkedList<String> strList) { }
    public void printlist(LinkedList<Date>   dateList) { }
}
```

---

## Arrays and Generics

Arrays are **covariant** in Java:

```java
ETicket[] elecarr   = new ETicket[10];
Ticket[]  ticketarr = elecarr;    // OK at compile time (ETicket[] is subtype of Ticket[])
ticketarr[5] = new Ticket();      // RUNTIME ERROR! ticketarr[5] is actually an ETicket slot
```

To avoid similar issues with generics, Java allows declaring but **not instantiating** generic arrays:

```java
T[] newarray;              // Declaration is OK
newarray = new T[100];     // COMPILE ERROR — cannot create generic array
```

**Workaround (generates a compiler warning but works):**

```java
T[] newarray = (T[]) new Object[100];   // ugly but accepted
```

---

## Wrapper Classes

Because of type erasure, all type variables become `Object` at runtime.  
But **primitive types** (`int`, `double`, etc.) are **not compatible with `Object`**.

Therefore, you **cannot use primitives in generics directly**:

```java
LinkedList<int>    list;   // ILLEGAL
LinkedList<double> list;   // ILLEGAL
```

Use **wrapper classes** instead:

| Primitive | Wrapper Class |
|---|---|
| `byte` | `Byte` |
| `short` | `Short` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |
| `boolean` | `Boolean` |
| `char` | `Character` |

> All numeric wrappers (`Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`) extend the class `Number`.

---

## Autoboxing

Java automatically converts between primitive types and their wrappers — this is called **autoboxing**:

```java
// Manual boxing/unboxing:
int x = 5;
Integer myx = new Integer(x);    // boxing
int y = myx.intValue();           // unboxing

// Autoboxing — Java does this implicitly:
int x = 5;
Integer myx = x;    // auto-boxed
int y = myx;         // auto-unboxed
```

This allows primitives to be used in generic data structures:

```java
LinkedList<Integer> intlist = new LinkedList<>();
intlist.insert(42);     // 42 is auto-boxed to Integer
int val = intlist.head();  // auto-unboxed back to int
```

---

## Summary

| Topic | Key Point |
|---|---|
| Type erasure | Generic info is stripped at runtime; `T` becomes `Object` (or bound) |
| `instanceof` with generics | **Not possible** — type info is gone |
| `getClass()` equality | `LinkedList<Employee>` and `LinkedList<Date>` have the same class |
| Overloading restriction | Cannot overload using different generic instantiations |
| Generic arrays | Can declare `T[]` but cannot do `new T[n]` |
| Array workaround | `(T[]) new Object[n]` — works with a warning |
| Primitives in generics | Not allowed — use wrapper types |
| Autoboxing | Implicit primitive ↔ wrapper conversion |
