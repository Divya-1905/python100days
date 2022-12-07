x = [4,5,6,7,8]
# print(x.insert(4,100))
# y = x.extend([4,5,78])
y = x.pop(4)  #pop remove the specific ()
# list can mention only list not a () this type
print(x)
print(y)
# y = x.remove(2)
# print(y)
d = [45,6,56,7]
d.remove(45)
print(d)
r = [56,67,8,6,89]
r.pop(1)#pop is remove the index based value
print(r)
r.clear()
print(r)
# index
t = [3,4,'df','ert',4]
w = t.index('df')
print(3 in t)
print(56 in t)
q = t.count(4)
print(q)