# OOP Notes (Java)

Notes based on lectures from *Programming Concepts using Java* by **Madhavan Mukund** (CMI).

## Contents

| File | Topics Covered |
|------|----------------|
| [01_oo_design.md](01_oo_design.md) | OO Philosophy, object design, class relationships |
| [02_subclasses_inheritance.md](02_subclasses_inheritance.md) | Subclasses, `extends`, `super`, inheritance |
| [03_polymorphism.md](03_polymorphism.md) | Dynamic dispatch, overloading vs overriding, type casting |
| [04_class_hierarchy.md](04_class_hierarchy.md) | Java class hierarchy, `Object` class, multiple inheritance |
| [05_subtyping_vs_inheritance.md](05_subtyping_vs_inheritance.md) | Subtyping vs inheritance distinction |
| [06_modifiers.md](06_modifiers.md) | `public`, `private`, `static`, `final` |
| [07_abstract_classes_interfaces.md](07_abstract_classes_interfaces.md) | Abstract classes, interfaces, `implements` |
| [08_interfaces_advanced.md](08_interfaces_advanced.md) | Interface static/default methods, conflict resolution |
| [09_private_classes.md](09_private_classes.md) | Inner classes, nested objects, private classes |
| [10_interaction_with_state.md](10_interaction_with_state.md) | Controlled object access, private class + interface pattern |
| [11_callbacks.md](11_callbacks.md) | Callbacks, `Timerowner` interface pattern |
| [12_iterators.md](12_iterators.md) | Iterator pattern, inner class iterators |
| [13_generics.md](13_generics.md) | Java generics, type variables, wildcards, subtyping |
| [14_reflection.md](14_reflection.md) | Java reflection, `Class`, introspection, `getClass()` |
| [15_generics_erasure.md](15_generics_erasure.md) | Type erasure, wrapper classes, autoboxing |

---

## Summary

1. **[01_oo_design.md](01_oo_design.md)**
   - Objects bundle state (fields) + behaviour (methods)
   - Class relationships: *uses*, *creates*, *extends*
   - Encapsulation: keep fields `private`, expose a minimal public API

2. **[02_subclasses_inheritance.md](02_subclasses_inheritance.md)**
   - `extends` keyword; subclass inherits all non-private members
   - Constructor chaining with `super(...)`
   - `@Override` — subclass redefines a parent method

3. **[03_polymorphism.md](03_polymorphism.md)**
   - Dynamic dispatch: method resolved at **runtime** based on actual object type
   - Overloading (same name, different params) vs Overriding (same signature)
   - Downcasting with `(Type)` and safe check with `instanceof`

4. **[04_class_hierarchy.md](04_class_hierarchy.md)**
   - Every class implicitly extends `Object` (`toString()`, `equals()`, `hashCode()`)
   - Java forbids `extends` from multiple classes (diamond problem)
   - Solution: single class inheritance + multiple interface implementation

5. **[05_subtyping_vs_inheritance.md](05_subtyping_vs_inheritance.md)**
   - **Subtyping** = type compatibility (`B` can be used where `A` is expected)
   - **Inheritance** = code reuse (`B` reuses `A`'s implementation)
   - A subclass gives you both; they are independent concepts

6. **[06_modifiers.md](06_modifiers.md)**
   - Access: `public` > `protected` > *(package)* > `private`
   - `static`: belongs to the class, not an instance
   - `final`: immutable variable / non-overridable method / non-extendable class

7. **[07_abstract_classes_interfaces.md](07_abstract_classes_interfaces.md)**
   - `abstract` method: no body; subclass *must* implement it
   - `abstract` class: cannot be instantiated; used as a base type
   - `interface`: all methods abstract; a class `implements` multiple interfaces

8. **[08_interfaces_advanced.md](08_interfaces_advanced.md)**
   - `static` interface methods: called as `Interface.method()`, no `this`
   - `default` methods: provide a fallback implementation; subclass may override
   - Conflict rule: if two interfaces clash → implementing class must resolve; if class vs interface → **class wins**

9. **[09_private_classes.md](09_private_classes.md)**
   - `private class Node { ... }` declared inside another class — invisible outside
   - Inner class objects can access `private` members of the enclosing class
   - Pattern: `private` inner class `implements` a `public` interface → hides implementation, exposes only the contract

10. **[10_interaction_with_state.md](10_interaction_with_state.md)**
    - Controlled state access via the *private class + interface* pattern
    - Mutable state wrapped behind methods; no direct field exposure
    - `login()` returns an interface type — caller gets limited, typed access

11. **[11_callbacks.md](11_callbacks.md)**
    - Callback = pass an object (implementing an interface) to be called later
    - `TimerOwner` interface: `timerdone()` method invoked by `Timer` when it fires
    - Decouples the caller from the callee; callee only knows the interface

12. **[12_iterators.md](12_iterators.md)**
    - `Iterator<T>` interface: `hasNext()` + `next()`
    - Implement as a **private inner class** to access internal data structure fields
    - `Iterable<T>` + `iterator()` enables `for (T x : collection)` syntax

13. **[13_generics.md](13_generics.md)**
    - Type variable syntax: `class Box<T> { T value; }`
    - Bounded params: `<T extends Comparable>` restricts what types are allowed
    - Wildcards: `?` (any), `? extends T` (upper bound), `? super T` (lower bound)
    - Generic methods: `public static <T> void swap(T[] arr, int i, int j)`

14. **[14_reflection.md](14_reflection.md)**
    - `obj.getClass()` / `Class.forName("pkg.Foo")` — get a `Class` object at runtime
    - `getDeclaredFields()`, `getDeclaredMethods()` — inspect structure dynamically
    - `Method.invoke(obj, args)` — call a method by name at runtime
    - Used in: serialization, test frameworks (JUnit), dependency injection

15. **[15_generics_erasure.md](15_generics_erasure.md)**
    - Java erases generic types at compile time → `List<String>` becomes `List` at runtime
    - Cannot do `new T()` or `instanceof T` inside generic code
    - Primitive types not allowed as type params — use wrapper classes (`int` → `Integer`)
    - Autoboxing: `Integer x = 5;` / Unboxing: `int y = x;` handled automatically
