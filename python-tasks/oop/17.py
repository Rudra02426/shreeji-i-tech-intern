### Task 17: Implement Abstract Method
from abc import ABC,  abstractmethod
class Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
class dog(Animal):
	def sound(self):
		print("dog is bark")
class cat(Animal):
	def sound(self):
		print("cat meows")
d=dog()
c=cat()
d.sound()
c.sound()
