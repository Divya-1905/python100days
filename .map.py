def add(x):
    return x*x
num =[2,4,5,67,] 
num1=[5,7,8,9]   
# result = map(add,num)
# print(list(result))
print(list(map(add,num)))
# map() function returns a map object(which is an iterator) 
# of the results 


def onlyeven(y):
    return y%2!=0
print(list(filter(onlyeven,num)))
print(list(zip(num,num1)))
print(list())

