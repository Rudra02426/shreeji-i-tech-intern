### Task 16: Abstract Class

from abc import ABC,  abstractmethod
class Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
class dog(Animal):
	def sound(self):
		print("dog is bark")
d=dog()
d.sound()