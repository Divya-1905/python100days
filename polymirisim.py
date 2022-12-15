""" polymoriphism 
"""
""" the same function take different work is called polymoriphism"""
class bag():
    def quanity(selff):
        print('2.6')
class paper(bag):
    def quanity(selff):
        print('5.7kg') 
books = paper()
books.quanity()  
fun = bag()
fun.quanity()



