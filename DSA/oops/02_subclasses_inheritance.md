# 02 — Subclasses and Inheritance

## A Java Class (Recap)

```java
public class Employee {
    private String name;
    private double salary;

    // Constructors
    public Employee(String n, double s) { name = n; salary = s; }
    public Employee(String n)           { this(n, 500.00); }  // calls the above

    // Mutator methods
    public boolean setName(String s)   { ... }
    public boolean setSalary(double x) { ... }

    // Accessor methods
    public String getName()   { ... }
    public double getSalary() { ... }

    // Other methods
    public double bonus(float percent) {
        return (percent / 100.0) * salary;
    }
}
```

Key points:
- Instance variables are **private**
- `setXxx` = **mutator** (updates state)
- `getXxx` = **accessor** (reads state)

---

## Subclasses — `extends`

Managers are a special type of employee with additional features.

```java
public class Manager extends Employee {
    private String secretary;

    public boolean setSecretary(String s) { ... }
    public String  getSecretary()         { ... }
}
```

- `Manager` is a **subclass** of `Employee` (i.e., a *subset* of employees who are also managers)
- Manager objects **inherit** all fields and methods of `Employee`
- Every `Manager` automatically has `name`, `salary`, and their associated methods

---

## Constructor Chaining with `super`

Subclasses **cannot access private fields** of the parent class directly.  
Use `super(...)` to call the parent constructor.

```java
public class Manager extends Employee {
    private String secretary;

    public Manager(String n, double s, String sn) {
        super(n, s);         // calls Employee(String, double)
        secretary = sn;
    }
}
```

> `super(...)` **must be the first statement** in the subclass constructor.

---

## Inheritance Rules

| Statement | Validity | Explanation |
|---|---|---|
| `Employee e = new Manager(...)` | ✅ Legal | A Manager *is-an* Employee |
| `Manager m = new Employee(...)` | ❌ Illegal | An Employee is not necessarily a Manager |

Subclass has **more features** than the parent. Every `Manager` is an `Employee`, but not vice versa.

---

## Multiple Constructors (`this(...)`)

A constructor can call another constructor of the *same* class:

```java
public Employee(String n) {
    this(n, 500.00);   // delegates to Employee(String, double)
}
```

---

## Summary

| Feature | Detail |
|---|---|
| `extends` | Keyword to create a subclass |
| Subclass inherits | Instance variables + methods of parent |
| `super(...)` | Calls parent constructor |
| Private fields | **Not visible** in subclass — use parent's constructor or accessors |
| Subclass > parent | Subclass can add more instance variables and methods |
| Can also override | Methods can be redefined (covered in Polymorphism) |
