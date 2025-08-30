"""
Magic Methods/Dunder Methods:
    Dunder short for "Double Underscore" methods a.k.a. are the methods with method name like '__func_name__()'
Why use Dunder/Magic Methods?:
    ~> Almost every thing in Python is Object-Oriented...
    
    ~> Every Data-Type/Collection is basically just a class and similarly every varible is an instance of that class.
    
    ~> So, every function used for am operation on that variable is basically a method.
    
    ~> When you use this functions python calls the dunder methods behind the scenes.

    ~>Magic/Dunder Methods allows us to make/overide(i.e. customise) the operators Arithmetic/Comparison Operators like '+', '-', '*', '<', '>', '==' and almost every method...

    ~> So it's operator overridng 
"""
class Book:
    def __init__(self, title: str="Untitled", author: str="Unknown", total_pages: int=0):
        self.title = title
        self.author = author
        self.total_pages = int(total_pages)
    
    #if we print the object/instance directly we would get the memmory address of it, so we would use magic method __str__
   
    def __str__(self) -> str:
        print("str dunder method called!")
        return f"'{self.title}' by {self.author}\n"

    """
    If there is no str dunder method then, repr dunder method would be used if exists...
    repr method short for represent is used for debuggingg and for more details of the object. 
    """
    def __repr__(self) -> str:
        print("repr dunder method called!")
        return f"Book:'{self.title}',\nAuthor/Writter:{self.author},\nPages:'{self.total_pages}'\n"
    
    
    #Arimetic Operations for Int/float attributes/members
    def __add__(self, other)->int|None:
        try:
            if isinstance(other, Book):
                self.total_pages+=other.total_pages
                return self.total_pages
            elif isinstance(other, int):
                self.total_pages+=other
                return self.total_pages 
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comaparision between {type(self)} and {type(other)}"
            print(TE)
        except Exception:
            print("Unknown Exception: Something Occurred")
            
    def __sub__(self, other)->int|None:
        try:
            if isinstance(other, Book):
                self.total_pages-=other.total_pages
                return self.total_pages
            elif isinstance(other, int):
                self.total_pages-=other
                return self.total_pages 
            else:
                raise TypeError
            
        except TypeError as TE:
            TE=f"TypeError: Invaild comaparision between {type(self)} and {type(other)}"
            print(TE)
        
        except Exception:
            print("Unknown Exception: Something Occurred")
    
    """
    Other arithmetic operators:
        MULTIPLICATION: ___mul___() for *
        DIVISION: __truediv__() for /
    """

    """
    Comparasion operators:
        ~> EQUAL TO: __eq__() for '=='
        ~> NOT EQUAL TO: __ne__() for !=
        ~> LESSER THAN: __lt__() for <
        ~> GREATER THAN: __gt__() for >
        ~> LESSER THAN OR EQUAL TO: __lte__() for <= 
        ~> GREATER THAN OR EQUAL TO: __gte__() for >=
    """
    # ==
    def __eq__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.title==other.title and self.author==other.author
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE
    
    # !=
    def __ne__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.total_pages != other.total_pages
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE
    
    # <
    def __lt__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.total_pages < other.total_pages
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE
    
    # >
    def __gt__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.total_pages > other.total_pages
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE
    
    #>=
    def __gte__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.total_pages > other.total_pages or self.total_pages == other.total_pages
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE

    # <=
    def __lte__(self, other)->bool|str:
        try:
            if isinstance(other, Book):
                return self.total_pages < other.total_pages or self.total_pages == other.total_pages
            else:
                raise TypeError
        except TypeError as TE:
            TE=f"TypeError: Invaild comparison between {type(self)} and {type(other)}"
            return TE
    
        
book1=Book(title="Dune", author="Frank Herbert", total_pages=1000)
book2=Book(title="The Wonderful Wizard Of Oz", author="L. Frank Baum ", total_pages=259)
book3=Book(title="Harry Potter", author="J.K Rowling", total_pages=2000)

#now __str__ will be used 
print(book1)
print(repr(book1))

print("Book 1 + Book 2 =",book1+book2)
#or
print(book1.__add__(other=book2))
print(book1.__add__(other=100))

print("Is book1 == book2?", book1==book2)

print("Is book1 != book2?", book1!=book2)

print("Is book1 < book3?", book1<book3)
print("Is book1 > book3?", book1>book3)

print("Is book1 >= book2?", book1.__gte__(book2))
print("Is book1 <= book2?", book1.__lte__(book2))

"""
EQUIVALENT TO:
print("Is book1 >= book2?", book1 >= book2)
print("Is book1 <= book2?", book1 <= book2)
"""




