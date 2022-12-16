def add_book(fun):
    def index(a,b):
        print('add a,b')
        if b == 0:
            print('cannot add')
            return  a,b 
        return index   
@add_book
def add(a,b):
    print(a,b)

add(3,5)