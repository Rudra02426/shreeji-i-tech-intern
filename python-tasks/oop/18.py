
### Task 18: Library Management

class Book:
	def __init__(self, name):
		self.name=name
class library:
	def __init__(self):
		self.books= []
	def add(self, book):
		self.books.append(book)
	def display(self):
		if not self.books:
			print("no books available in library")
		else:
			print("books in library: ")
			for book in self.books:
				print("-" , book.name)
lib=library()
n=int(input("enter how many books will add: "))
for i in range(n):
	name=input("enter book name:")
	lib.add(Book(name))
lib.display() 