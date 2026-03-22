# 1.How  to create a table:


CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT,
    age INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


# 2.HOW TO ADD COLOMN name "status"


ALTER TABLE users ADD COLUMN status TEXT;


# 3.DELETE TABLE users


DROP TABLE users;


# 4.INSERT DATA INTO A TABLE


SELECT * FROM users;
INSERT INTO users (name,username)
VALUES ('Rajnish', 'bkl_rajnish'),('John Doe', 'jdoe');


# 5. To select a Certaing id:


SELECT * FROM users
WHERE username = 'bkl_rajnish'OR username ='jdoe';


# 6.Add id and add data:


UPDATE users SET email = 'rajnish@sst.scaler.com' WHERE username = 'bkl_rajnish' AND email ='Johndoe@sst.scaler.com' AND username = 'jdoe';
SELECT * FROM users


# 7.FOReign Keys


CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),-- foreign key constraint
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM posts;


# 8. changing or working with foreign keys:


INSERT INTO posts (user_id, title, body)
VALUES (1, 'First Post', 'This is the body of the first post'),
       (2, 'Second Post', 'This is the body of the second post');
SELECT * FROM posts;


# 9.BAckend + DB


# THIS IS THE BASE CODE:


import sqlite3

connection =  sqlite3.connect("gta.db")
cursor = connection.cursor()


connection.close()


# i.Make a DAtabase using python


import sqlite3

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS gta (release_year INTEGER, name TEXT, city TEXT)")

release_list = [
    (1997, "GTA", "State of New Jersey"),
    (1998, "GTA 2", "State of New Jersey"),
    (2001, "GTA III", "Liberty City"),
    (2002, "GTA Vice City", "Vice City"),
    (2004, "GTA San Andreas", "San Andreas"),
    (2008, "GTA IV", "Liberty City"),
    (2013, "GTA V", "San Andreas"),
]

# Insert before selecting
cursor.executemany("INSERT INTO gta VALUES (?, ?, ?)", release_list)

# Commit the changes
connection.commit()
connection.close()


# ii.How to read data:


import sqlite3

connection =  sqlite3.connect("gta.db")
cursor = connection.cursor()

for row in cursor.execute("select * from gta"):
    print(row)

connection.close()


# iii.print a particular:


import sqlite3

connection =  sqlite3.connect("gta.db")
cursor = connection.cursor()

# A specific:
cursor.execute("select * from gta where city='Liberty City'")
gta_search = cursor.fetchall()
print(gta_search)

connection.close()


# iv.Dealing with multiple tables:


import sqlite3
#Adding a new table

connection = sqlite3.connect("gta.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS cities (gta_city TEXT,real_city TEXT)")
city_list = [
    ("State of New Jersey",""),
    ("State of New Jersey",""),
    ("Liberty City",""),
    ("Vice City",""),
    ("San Andreas",""),
    ("Liberty City","New York"),
    ("San Andreas",""),
]

# Insert before selecting
cursor.executemany("INSERT INTO cities VALUES (?, ?)", city_list)

# Commit the changes
connection.commit()
connection.close()


# v.Printing new table:


import sqlite3

connection =  sqlite3.connect("gta.db")
cursor = connection.cursor()

#new table
for i in cursor.execute("select * from cities"):
    print(i)
city_search = cursor.fetchall()
connection.close()


# vi.Manipulate database data


###Changing data using id
###This code is not working you have  todeclare above this then you can use it
import sqlite3

connection =  sqlite3.connect("gta.db")
cursor = connection.cursor()

city_search = cursor.fetchall()

for i in gta_search:
    adjusted = [city_search[5][1] if value==city_search[5][] else value for value in i]
    print(adjusted)
connection.close()