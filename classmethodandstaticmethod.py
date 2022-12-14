from abc import abstractclassmethod ,ABC
class computers(ABC):
	@abstractclassmethod
	def dell(self):
		pass
	@abstractclassmethod
	def lenovo(self):
		pass
	# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.


class user():
	@staticmethod
	def dell():
		print('hai user')
	@classmethod	
	def lenovo(self):
		print('this is lenovo')
	def __hash__(self):
		return hash(3465)
log = user()
log.dell()
log.lenovo()
print(log.__hash__())

user.dell()






























# from abc import ABC, abstractclassmethod
 

# class library(ABC):
# 	@abstractclassmethod
# 	def s():
# 		pass 


# 	@abstractclassmethod
# 	def add_book():
# 		pass 


# 	@abstractclassmethod
# 	def view_books():
# 		pass


# 	@abstractclassmethod
# 	def remove_book():
# 		pass


# 	@abstractclassmethod
# 	def take_book():
# 		pass


# class school(library):# the add_book abstact is pre-define the function 
# 	def __init__(self,book=None):
# 		self.book=book
# 	# def check(self):
# 	# 	print('this a books') 
 

# 	def add_book(self):
# 		if self.book ==[]:
# 			count = int(input('enter the book numbers'))
# 			for i in range(count):
# 				b_name = input()
# 				self.book.append(b_name)
# 		else:
# 			print('enter the book')	
# 			self.book.append(input)	

# 	def view_books():
# 		pass
# 	def remove_book():
# 		pass 
# 	def take_book():
# 		pass 

# book =[]
# pro = school(book)
# pro.add_book()
# # while True:
# # 	print("1.add book")
# # 	print("2.view book")
# # 	print("3.remove book")
# # 	print("4.take book")
# # 	data = input('enter the opertion')     
# # 	if(data==1):
# # 		pro.add_books()
# # 	elif(data==2):
# # 		pro.view_books()
# # 	elif(data==3):
# # 		pro.issue_books()
# # 	elif (data == 4):
# # 		pro.remove_book()
# # 	else:
# # 		 quit()
