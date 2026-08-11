class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return f'{self.title} Issued Successfully!'
        else:
            return f'{self.title} is currently not Available!'

    def return_book(self):
        if self.is_available == False:
            self.is_available = True
            return f'{self.title} is Returned Successfully!'
        else:
            return f'{self.title} was not borrowed!'

    def __str__(self):
        return f"{self.title} by {self.author} - {'Available' if self.is_available else 'Borrowed'}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"



#----------------------------------------------------------------------


class Member:
    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self,book):
        if book.is_available: 
            msg = book.borrow_book()
            self.borrowed_books.append(book)
            return msg
        
            
        else:
            return 'This book is Not Available right now!'

    def return_book(self,book):
        if book in self.borrowed_books:
            msg = book.return_book()
            self.borrowed_books.remove(book)
            return msg
        else:
            return "You didn't borrow this book!"
        

#----------------------------------------------------------------------


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)

    def register_member(self,member):
        self.members.append(member)

    def find_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def issue_book(self,member_id,isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member is None:
            return "Incorrect Member ID !"
        if book is None:
            return "No Book Found!"

        return member.borrow_book(book)
        
    
    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member is None:
            return "Incorrect Member ID !"
        if book is None:
            return "No Book Found!"

        return member.return_book(book)

book = Book('Jawab e Shikwa','Allama Iqbal','1234')
book2 = Book('Iblees ki majlis e shuraa','Allama Iqbal','6789')
print(book.is_available)
# print(book.borrow_book())
# print(book.return_book())
print(book.__str__())


m1 = Member('AbdulRafay','121')
m1.borrow_book(book)
m1.borrow_book(book2)


m1.return_book(book2)
print(m1.borrowed_books)

l1 = Library()
l1.add_book(book)
l1.add_book(book2)

l1.register_member(m1)
print(l1.issue_book('121','6789'))