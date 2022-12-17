# """ polymoriphism 
# """
# """ the same function take different work is called polymoriphism"""
class bag():
    def quanity(self):
        print('2.6')
class paper(bag):
    def quanity(self):
        print('5.7kg') 
books = paper()
books.quanity()  
fun = bag()
fun.quanity()

class addition1:
    def add(self,a,b):
        y = a+b
        print(y)
class addtions(addition1):
    def add (self,a,b):
        y = a+b+34
        print(y)
obj = addtions()
obj.add(2,4)                



