#Magic Methods a.k.a Dunder methods(double underscore)
#They are automatically called by python's libraries
#They allow us to define or customize the behavior of the objects.

class book:
    def __init__(self, title="", author="", totalPages=0):
        self.title = title
        self.author = author
        self.totalPages = int(totalPages)
    
    #if we print the object/instance directly we would get the memmory address of it, so we would use magic method __str__
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    #now if we need to check that other instance are equal to each other or not
    def __eq__(self, other):
        return self.title==other.title and self.author==other.author
    #now if need to compare two objects/instances
    def __lt__(self, other):
        return self.totalPages < other.totalPages
    
    def __gt__(self, other):
        return f" gt {self.totalPages > other.totalPages}"
    
    #Arimetic Operations for Int/float attributes/members
    def __add__(self, other):
        self.totalPages+=other.totalPages
        return self.totalPages
     #or
    #def add_by_list(Book_list):
        for Book in Book_list:
            total_pages +=Book.totalPages
            total_authors+=Book.author
            total_titles+=Book.title
        return book(title=total_titles, author=total_authors, totalPages= total_pages)
    
        
book1=book(title="Dune", author="Frank Herbert", totalPages="1000")
book2=book(title="Dune", author="Frank Herbert", totalPages="500")
book3=book(title="Harry Potter", author="J.K Rowling", totalPages="2000")
book4 = book("ABC", "NO", 0)

#now __str__ will be used 
print(book1)
print(book2)
print(book3)
print(book4)

print("Are they equal (book1==book2) ?", book1==book2)#they should be equal accoring to __eq__ conditions 
print("Are they equal (book1==book3)?", book1==book3)

print("Is book1 < book3?", book1<book3)#will return a boolean value
print("Is book1 > book3?", book1>book3)#will return a boolean value

print("book 1 + book 2 =",book1+book3)






