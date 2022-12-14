booksavailable=[['Action','the call of the wild',123456789,'Jack London'],['Action','The Three Musketeers',234567890,'Alexandre Dumas'],['Comic','Watchmen',345678901,'Alan Moore'],['Comic','The walking dead',456789012,'Robert Kirkman'],['Mystery','The Adventures of Sherlock Holmes',567890123,'Sir Arthur Canon Doyle'],['Mystery','The night fire',678901234,'Michael Conelly']]
# User ID: 
class books:
    def __init__(self,booksavailable):
        self.books = booksavailable
    def borrow_book(self):
        a=input('Enter the book name:')
        if a in self.books:
            print('Book Issued!')
            self.books.remove(a)
    def return_book(self):
        a= input("Enter the book you want to return:")

        if a not in self.books:
            print('Thank You for the return!')

        else:
            print('Books has already been submitted!')

    def reserve_book(self):
        a=input('Enter the book name:')
        if a in self.books:
            print('Book is reserved!')
        else:
            print('Book is not available')
#let the list of books in the form of: a=[[Genre, Book name, ISBN no., Author]]
a=[['Action','the call of the wild',123456789,'Jack London'],['Action','The Three Musketeers',234567890,'Alexandre Dumas'],['Comic','Watchmen',345678901,'Alan Moore'],['Comic','The walking dead',456789012,'Robert Kirkman'],['Mystery','The Adventures of Sherlock Holmes',567890123,'Sir Arthur Canon Doyle'],['Mystery','The night fire',678901234,'Michael Conelly']]
class shelf:
    def display(self):
        m=[]
        b= input('Enter the genre:')
        for i in a :
            if b in i:
                l=[i[1],i[2],i[3]]
                m.append(l)
        for i in m:
            print(i)

    def add_book(self):
        e = input('Enter the genre:')
        b = input('Enter the book name:')
        c = int(input('Enter the Isbn NO.:'))
        d= input('Enter the Author name:')
        j=[e,b,c,d]
        a.append(j)
    def remove_book(self):
        c = int(input('Enter the Isbn NO.:'))

        for i in a:
            if c == i[2]:
                a.remove(i)

k = books()
l = shelf()
r= input('Enter (User/Admin):')
g = int(input("Enter your ID:"))
f = input("Enter your password:")
if r.lower()=='user' and g== and f.lower()=='':
    print('1. Issue a book\n2. Return a book\n3.Reserve a book')
    v= int(input('Enter your choice:\t'))
    if v==1:
        k.borrow_book()
    if v==2:
        k.return_book()
    if v==3:
        k.reserve_book()


if r.lower()=='admin' and g== and f.lower='':
    print('1. Display the books\n2. Add a book\n3. Remove a book ')
    v = int(input('Enter your choice:\t'))
    if v == 1:
        l.display()
    if v==2:
        l.add_book()
    if v==3:
        l.remove_book()












