# Python magic (dunder) methods are special methods with double underscores __ 
# that enable operator overloading and custom object behavior.

        # They are autoatically called by many of python's built-in operations
        # They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages


    def __str__(self):
        return f"'{self.title}' by {self.author}"


    def __eq__(self, value):
        return self.title == value.title and self.author == value.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages


    def __gt__(self, other):
        return self.num_pages > other.num_pages


    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"


    def __contains__(self, item):
        return item in self.title or item in self.author


    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"key {key} was not found"

book1 = Book('The Hobbit','J.R.R Tolkien',310)
book2 = Book('Harry Potter and the Philosophers Stone','J.K. Rowling',223)
book3 = Book('The Lion, The witch and the Wardrobe','C.S. Lewis',172)

# print(book1) #we are given memory address
#After adding __str__ method we can customize this behaviour

print(book1)
print(book2)
print(book3)

# print(book1== book2) # before it everytime gives false....!
#we can customize it by __eq__ method

print(book1 == book2) #now if the books are equal we will get true.

print(book2 < book3)
print(book2 > book3)


print(book2 + book3)

print("Lion" in book3)

print(book1['title'])
print(book1['author'])
print(book1['audio'])

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age} years old."

p1 = Person('Abdul Rafay',22)
print(p1)


class Banana:
    def __init__(self,cost,length):
        self.cost = cost
        self.length = length


    def __len__(self):
        return self.length
    
b = Banana(9.4,5)
print(len(b))