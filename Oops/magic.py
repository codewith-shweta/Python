#magic method (dunder) = __(double underscore on both sides) called automaticatly built- in func

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title 
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}'|| by {self.author} in  || {self.num_pages} pages "

    
    def __add__(self,other):
        return self.num_pages + other.num_pages

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __lt__(self,other):
        return self.num_pages > self.num_pages

                       

book1 = Book   ("Loved", "J.K", 50)
book2 = Book   ("Crossed", "Raedly", 57)
book3 = Book   ("Harry Potter", "Henry", 3453)

#print(book1)
#print(book2)
#print(book3)
#print(book1 == book2) 
#print(book1 + book3)
print(book2 < book3)
print(book1 > book2)