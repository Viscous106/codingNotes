# 01 — The Philosophy of OO Programming

## Structured vs Object-Oriented Design

**Traditional / Structured Programming**:
- Algorithms come first
- Design procedures for specific tasks, combine them for complex systems
- Data structures are designed to suit the procedures

**Object Oriented Design**:
- Reverse the focus: **data first, algorithms second**
- First identify what data you want to maintain and manipulate
- Then identify algorithms to operate on that data

> **Claim:** OO design works better for large systems.
>
> Example – simple web browser:
> - Structured: 2000 procedures manipulating global data
> - OO: 100 classes, each with ~20 methods → much easier to grasp the design
>
> Debugging: an object is in an incorrect state → search among 20 methods, not 2000 procedures.

---

## Designing Objects

Every object has three key properties:

| Property | Description |
|----------|-------------|
| **Behaviour** | What methods are needed to operate on the object? |
| **State** | Information stored in instance variables; controlled via encapsulation |
| **Identity** | Distinguishes different objects of the same class |

These features **interact**:
- State typically affects behaviour  
  e.g., cannot add an item to an order that has already been shipped  
  e.g., cannot ship an empty order

**Encapsulation principle:** state should only change when a method explicitly operates on it.

---

## Example: Order Processing System

Objects involved:
- `Item`, `Order`, `ShippingAddress`, `Payment`, `Account`

Operations (methods):
- Items are added to orders
- Orders are shipped / cancelled
- Payments are accepted / rejected

> **Rule of thumb:** Nouns → objects; Verbs → methods that operate on objects.  
> Associate with each `Order` a method `addItem()`.

---

## Relationships Between Classes

| Relationship | Description | Example |
|---|---|---|
| **Dependence** | One class needs another to function | `Order` needs `Account` to check credit |
| **Aggregation** | One class contains objects of another | `Order` contains `Item` objects |
| **Inheritance** | One class is a specialised version of another | `ExpressOrder` inherits from `Order` |

> **Robust design minimises dependencies (coupling) between classes.**

---

## Summary

- OO approach helps organise code in large projects
- Understanding OO motivation helps explain design choices in Java
