# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))

class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #The class method takes cls (class) as first argument

    @classmethod
    def profiledetails(cls,name,year,date) :
        return cls(name, date.today().year - year)
 # The static method does not take any specific parameter.
    @staticmethod
    def check(age):
        return age>18
student1 = student('daffdds',34)
student2 = student.profiledetails('derw',2000)
print(student1.name)
print(student2.age)


















# from datetime import date
# class student():
#     def profile(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def page(cls,name,year):
#         return cls(name, date.today().year - year) 
#     @staticmethod
#     def check(age):
#         return age>18 
# student1=student.page('dart',22)
# print(student1.name)
        