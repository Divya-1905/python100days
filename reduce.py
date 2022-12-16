from functools import reduce
def fun(a,d):
    return a+d
res = reduce(fun,('hai','python'))
print(res)    
# reduce function is not return a mulitple value retun a single value
