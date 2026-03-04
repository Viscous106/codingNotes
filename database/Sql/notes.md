# Interactive SQL Tutorial for Complete Beginners

Welcome to the world of SQL! Since you're completely new to this, we will take it step by step. We have set up a safe, local environment for you right on your machine!

We will be using **SQLite**, a lightweight database engine pre-installed on your system, so you don't have to configure any heavy database servers.

---

## Step 0: Set Up Your Database Workspace

First, open your terminal. I have automatically generated a file named [university_schema.sql](file:///home/viscous/.gemini/antigravity/brain/3da4912a-2907-4ec0-8f6e-8dce12c8f885/university_schema.sql) that contains a dummy "University" database (with tables for departments, instructors, and classrooms). 

To start your interactive session and load this data, run this command in your terminal exactly as written:

```bash
sqlite3 university.db -init /home/viscous/.gemini/antigravity/brain/3da4912a-2907-4ec0-8f6e-8dce12c8f885/university_schema.sql
```

You should see an `sqlite>` prompt appear. 
*(If you ever want to leave, just type `.quit` and press Enter).*

---

## Step 1: The Basics (`SELECT`, `FROM`)

SQL is like telling the database exactly what information you want out of it. It reads almost like plain English.

Let's say we want to see the names of **all** the instructors in our database. 

Type this into your `sqlite>` prompt and press Enter:
```sql
SELECT name FROM instructor;
```

**What happened?**
- `SELECT` told the database what column (attribute) to fetch.
- `FROM instructor` told it which table to look inside.

What if we want to see **everything** about the instructors (their ID, name, department, and salary)? We use the `*` wildcard, which means "all columns".

Try this:
```sql
SELECT * FROM instructor;
```

---

## Step 2: Filtering Data (`WHERE`)

Usually, we don't want to see *everything*; we want specific things. The `WHERE` clause filters the rows.

Let's find all the instructors who work in the **Physics** department.

Try this:
```sql
SELECT name, salary FROM instructor WHERE dept_name = 'Physics';
```

Let's find all instructors who make a **salary strictly greater than $80,000**.

Try this:
```sql
SELECT name, dept_name, salary FROM instructor WHERE salary > 80000;
```

---

## Step 3: Removing Duplicates (`DISTINCT`)

Sometimes, data holds duplicates. For example, if we ask for the departments our instructors belong to:
```sql
SELECT dept_name FROM instructor;
```
You'll notice `Comp. Sci.`, `Physics`, and `History` appear multiple times. To remove these duplicates, we use `DISTINCT`.

Try this:
```sql
SELECT DISTINCT dept_name FROM instructor;
```

---

## Step 4: Connecting Tables (`JOIN` and Cartesian Products)

This is a very powerful concept! Our `instructor` table knows the instructor's department and salary, but the `department` table holds the department's building and budget. What if we want to know the *building* an instructor works in?

We need to combine the two tables. 

Let's tell the database to match them where the *department names* are the same:

Try this:
```sql
SELECT instructor.name, department.building 
FROM instructor, department 
WHERE instructor.dept_name = department.dept_name;
```

### The Explicit Join
A more modern way to write the exact same thing is by using the word `JOIN`:
```sql
SELECT instructor.name, department.building 
FROM instructor JOIN department ON instructor.dept_name = department.dept_name;
```

---

## Step 5: Summarizing Data (Aggregations)

What if you are the university administrator and want to know the **Average Salary** of all your instructors? SQL has built-in math functions!

Try this:
```sql
SELECT AVG(salary) FROM instructor;
```

What if you want to know the **Maximum Capacity** of all classrooms?
```sql
SELECT MAX(capacity) FROM classroom;
```

### Grouping Data
It gets cooler. What if you want to know the average salary, but you want it separated **per department**? You use `GROUP BY`.

Try this:
```sql
SELECT dept_name, AVG(salary) FROM instructor GROUP BY dept_name;
```

---

## Step 6: Modifying Data (`INSERT`, `UPDATE`, `DELETE`)

It's time to play God with the data. 

### Inserting
Let's hire a new instructor!
```sql
INSERT INTO instructor (ID, name, dept_name, salary) VALUES ('99999', 'Viscous', 'Comp. Sci.', 150000);
```
*Verify it worked:* `SELECT * FROM instructor WHERE name = 'Viscous';`

### Updating
Let's give all instructors in `Comp. Sci.` a massive raise!
```sql
UPDATE instructor SET salary = salary + 20000 WHERE dept_name = 'Comp. Sci.';
```
*Verify it worked:* `SELECT * FROM instructor WHERE dept_name = 'Comp. Sci.';`

### Deleting
Sadly, we have to fire the instructor 'Mozart'.
```sql
DELETE FROM instructor WHERE name = 'Mozart';
```
*Verify it worked:* `SELECT * FROM instructor;`

---

## Ready for more? 
Try playing around with the tables! When you're done, remember you can exit by typing `.quit`. Let me know when you finish this sequence, and we can move on to triggers, complex sub-queries, and creating views!
