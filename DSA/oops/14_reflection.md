# 14 — Java Reflection

## What is Reflection?

> **Reflection (Wikipedia):** The ability of a process to examine, introspect, and modify its own structure and behaviour.

Two components:

| Component | Description |
|---|---|
| **Introspection** | A program can observe (and reason about) its own state |
| **Intercession** | A program can modify its execution state or alter how it is interpreted |

---

## Simple Reflection — `instanceof`

```java
Employee e = new Manager(...);
if (e instanceof Manager) {
    // e really is a Manager at runtime
}
```

This is a simple form of introspection — checking the runtime type.

**Limitation:** `instanceof` requires the type to be known at compile time.

```java
// CANNOT do this:
if (o instanceof T) { ... }     // T is a type variable — not allowed!
```

---

## The `Class` Object

Every loaded class `C` has a corresponding object of type `Class` that holds metadata about `C`.

### Getting the Class object

```java
// From an existing object
Class c = obj.getClass();

// From the class name (as a String)
Class c = Class.forName("Manager");
```

### Comparing classes

```java
import java.lang.reflect.*;

public static boolean classequal(Object o1, Object o2) {
    return (o1.getClass() == o2.getClass());
}
```

> Each distinct loaded class has **exactly one** `Class` object — so `==` works for comparison.

### Encoding runtime state as data = **Reification**
Representing an abstract idea in a concrete form.

---

## Creating Instances at Runtime

```java
Class c = obj.getClass();
Object o = c.newInstance();   // create new object of same type as obj

// Or more compactly using class name:
Object o = Class.forName("Manager").newInstance();
```

---

## Inspecting Classes: Constructors, Methods, Fields

```java
import java.lang.reflect.*;

Class c = obj.getClass();

Constructor[] constructors = c.getConstructors();
Method[]      methods      = c.getMethods();
Field[]        fields       = c.getFields();
```

Each element carries further detail:

```java
// Get parameter types of each constructor
for (int i = 0; i < constructors.length; i++) {
    Class[] params = constructors[i].getParameterTypes();
    // params is an array of Class objects
}
```

---

## Invoking Methods and Accessing Fields

```java
Method[] methods = c.getMethods();
Object[] args = { /* arguments */ };
methods[3].invoke(obj, args);       // call methods[3] on obj with given args

Field[] fields = c.getFields();
Object val = fields[2].get(obj);    // read fields[2] from obj
fields[3].set(obj, value);          // write value to fields[3] in obj
```

---

## Reflection and Security

By default, `getConstructors()`, `getMethods()`, `getFields()` return **only public** members.

To access **private** members as well, use:

```java
getDeclaredConstructors()
getDeclaredMethods()
getDeclaredFields()
```

> ⚠️ **Security concern:** Allowing arbitrary access to private members can be dangerous.  
> Access to private components can be restricted through **external security policies** in Java.

---

## Real-world Use: BlueJ

BlueJ (a Java learning environment) uses reflection to:
- Create objects of compiled classes
- Invoke methods on those objects interactively
- Examine object state

Without reflection, BlueJ would have to maintain its own internal "debugging" metadata for each class.

---

## Limitations of Java Reflection

| Limitation | Detail |
|---|---|
| Cannot create classes at runtime | `Class c = new Class(...)` — **not possible** |
| Cannot redefine methods at runtime | Unlike Python (`class XYZ:` can run at runtime) |
| BlueJ workaround | Must invoke the Java **compiler** before a new class can be used |

> Contrast: Python and Smalltalk allow more powerful runtime metaclass manipulation.

---

## Summary

| Feature | API / Notes |
|---|---|
| Get class of object | `obj.getClass()` |
| Get class by name | `Class.forName("ClassName")` |
| Create new instance | `c.newInstance()` |
| List constructors | `c.getConstructors()` (public only) |
| List methods | `c.getMethods()` (public only) |
| List fields | `c.getFields()` (public only) |
| Include private | `getDeclaredXxx()` variants |
| Invoke method | `method.invoke(obj, args)` |
| Read/write field | `field.get(obj)` / `field.set(obj, value)` |
