def fun(x,y=[20,50]):
    y.append(x)
    return y
print(fun(2,[50,20]))
# y have value of [50,20] append 2 return is [50,20,2]
set ={43,66,{12,35}}
print(set[2][1])
#o/p errotr set is immutable unchanged 
y = [12,56]
z = 'hai'

y+=z
print(y)
#[12, 56, 'h', 'a', 'i'] z is string we 
# can concantate after add but += we add the values
y =[12,34]
z = [95,67] #y+=z is a y =y +z
y+=z
print(y)
list =[2<5,16<9]
print(any(list))
#any is function 2<5 is true 6<9 is true so it return true
#if any one conditions is false is return its return is True
list2 =[2>5,6<9]
print(all(list2)) # all is return a fasle of the conditons
#if any one of conditon is false retun false
