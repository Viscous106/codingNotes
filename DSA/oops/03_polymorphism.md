# 03 — Dynamic Dispatch and Polymorphism

## Method Overriding

A subclass can **redefine** (override) a method from its parent class.

```java
public class Manager extends Employee {
    // Overrides Employee.bonus()
    double bonus(float percent) {
        return 1.5 * super.bonus(percent);   // calls parent's bonus() via super
    }
}
```

- `super.method()` explicitly invokes the parent class version of the method.

---

## Dynamic Dispatch (Late Binding)

```java
Employee e = new Manager(...);   // e is declared Employee, but holds a Manager
e.bonus(5.0);                    // Which bonus() runs?
```

| Approach | Which `bonus()` is used? |
|---|---|
| **Static binding** | `Employee.bonus()` (based on declared type) |
| **Dynamic binding** | `Manager.bonus()` (based on actual runtime type) ✅ |

**Java uses dynamic dispatch by default.**  
(In C++, you must explicitly declare `virtual` to get dynamic dispatch.)

> Static type-checking still applies: `e.setSecretary()` is **rejected** at compile time because `e` is declared as `Employee`.

---

## Polymorphism (Runtime / Inheritance Polymorphism)

```java
Employee[] emparray = new Employee[2];
emparray[0] = new Employee(...);
emparray[1] = new Manager(...);

for (int i = 0; i < emparray.length; i++) {
    System.out.println(emparray[i].bonus(5.0));
    // Each element "knows" its correct bonus() implementation
}
```

Every object in the array "knows" how to compute its bonus correctly — this is **polymorphism**.

> Also called *runtime polymorphism* or *inheritance polymorphism*.

---

## Overloading vs Overriding vs Dynamic Dispatch

| Concept | # Method Definitions | Same Signature? | Choice Made At |
|---|---|---|---|
| **Overloading** | Multiple | No (different args) | Compile time (static) |
| **Overriding** | Multiple | Yes | Compile time (static choice of definition) |
| **Dynamic Dispatch** | Multiple | Yes | **Run time** ✅ |

```java
// Overloading example (Java Arrays class)
class Arrays {
    public static void sort(double[] a) { ... }
    public static void sort(int[] a)    { ... }
}
Arrays.sort(darr);  // compiler picks sort(double[]) statically
Arrays.sort(iarr);  // compiler picks sort(int[]) statically
```

---

## Type Casting

When `e` is declared as `Employee` but actually holds a `Manager`:

```java
Employee e = new Manager(...);

// Calling Manager-specific method requires a cast:
((Manager) e).setSecretary(s);

// If e is NOT a Manager at runtime, this throws a ClassCastException
```

### `instanceof` check before casting

```java
if (e instanceof Manager) {
    ((Manager) e).setSecretary(s);
}
```

> `instanceof` is a simple form of **reflection** in Java — the program examines its own runtime state.

### Casting primitive types

```java
double d = 29.98;
int nd = (int) d;   // truncates to 29
```

---

## Summary

| Concept | Key Point |
|---|---|
| **Method overriding** | Subclass redefines same-signature method |
| **`super.method()`** | Call parent class version of a method |
| **Dynamic dispatch** | Runtime method selection — default in Java |
| **Polymorphism** | Each object responds with its own correct method |
| **Overloading** | Same name, different signatures — static choice |
| **Type casting** | Manually tell compiler to treat object as a subclass |
| **`instanceof`** | Runtime type check before casting |
