#magic methods are: __init__, __add__, __len__, __repr__ ,__str__etc.
#duble under__ function is called dunder methods
#Implementing dunder methods for classes is a good form of Polymorphism


#Operator overloading means provided additional functionality to
#  the operators, the python implicitly invokes the magic methods to 
#  provide additional functionality to it.
class student():
    def __init__(self,name,email):
        self.name = name 
        self.email = email

    def __add__(self,name,email):
        return self.name*email


e = student('saf','de@gmail.com')
e.__add__()