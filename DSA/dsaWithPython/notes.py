# %% [markdown]
# # Special (Magic/Dunder) Methods in Python

# In Python, special methods are a set of predefined methods you can use to enrich your classes. They are also known as "magic" or "dunder" methods (short for "double underscore"). These methods are identified by their names, which start and end with double underscores (e.g., `__init__`, `__str__`).

# %% [markdown]
# ## `__init__()`: The Constructor
# 
# The `__init__` method is one of the most important special methods. It's the constructor for a class. It is called automatically when you create a new instance (object) of a class. Its primary purpose is to initialize the object's attributes.

# %%
class Book:
    def __init__(self, title, author, pages):
        print(f"A new book '{title}' has been created!")
        self.title = title
        self.author = author
        self.pages = pages

# When we create an instance of Book, the __init__ method is called:
my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)

# The attributes are now set on the object
print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
print(f"Pages: {my_book.pages}")

# %% [markdown]
# ## `__str__()`: String Representation
#
# The `__str__` method is called by the `str()` built-in function and, by extension, the `print()` function. It should return a user-friendly string representation of the object. This is useful for displaying information about the object in a readable way.

# %%
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

my_book = Book("1984", "George Orwell", 328)

# Now, when we print the object, the __str__ method is called
print(my_book)

# %% [markdown]
# ## `__add__()`: Operator Overloading
#
# Special methods allow you to overload operators. The `__add__` method, for instance, allows you to define the behavior of the `+` operator for your custom objects. This is a form of operator overloading.

# %%
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Let's imagine adding two books creates a "Book Series" object
    def __add__(self, other):
        # For this example, let's just return a tuple of the book titles
        # A more complex implementation could return a new 'Series' object
        return (self.title, other.title)

book1 = Book("Dune", "Frank Herbert", 412)
book2 = Book("Dune Messiah", "Frank Herbert", 256)

# Use the + operator on Book objects
series = book1 + book2

print(f"The series consists of: {series}")

# Another example: let's use it to combine pages
class PageCounter:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return PageCounter(self.pages + other.pages)

    def __str__(self):
        return f"Total pages: {self.pages}"

book1_pages = PageCounter(412)
book2_pages = PageCounter(256)

total_pages = book1_pages + book2_pages
print(total_pages)

# %% [markdown]
# ### Other Common Special Methods
# - `__len__()`: Returns the length of the object. Called by `len()`.
# - `__repr__()`: Returns an unambiguous, "official" string representation of an object. It's meant to be informative for developers. If `__str__` is not defined, `__repr__` is used as a fallback.
# - `__eq__(self, other)`: Defines behavior for the equality operator, `==`.
# - `__getitem__(self, key)`: Defines behavior for accessing items using subscription (e.g., `obj[key]`).
# - `__setitem__(self, key, value)`: Defines behavior for assigning to items using subscription (e.g., `obj[key] = value`).
