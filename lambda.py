#the lambda is Anonimous function
#no need to given def name 
add = lambda c,t:c+t
print(add(3,5))
string ='python'
result = string.center(10,"*")
print(result) # 8 lettes are here total =10 balance 2 back and front replace by *
y = string.replace('p','*',2)
print(y)
#string.replace(oldvalue, newvalue, count)
s = '12:34:45'
result = s.replace(s[0],'9',2)
print(result)
