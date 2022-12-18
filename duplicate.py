row = ('r','e','r','t','y','u')
duplicate =[]
for i in row:
    if row.count(i)>1:
        duplicate.append(i) 
print(duplicate) 
row = ('r','e','e','r')
p = []
for i in row:
    if row.count(i)>1:
        if i not in p : #this line not repeate the value give only duplicate value
         p.append(i)
print(p)     
some = ('sd','sdf','sf') 
o = []
for i in some :
    if some.count(i)>1:
        o.append(i)
print(o)        
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9,55,33,66,44,33,66,77,]
x =[] #unque list 
y = []# duplicate
for i in lis:
    if i not in x:
        x.append(i)
    elif  i not in  y:
        y.append(i)
print(x)
print(y)

team = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9 ]
uniquelists =[]
duplicateList = []
for i in team:
    if i not in uniquelists:
        uniquelists.append(i)
    elif i not in duplicateList:
        duplicateList.append()
print(uniquelists)
print(duplicateList)        






lis = [ 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
uniqueList = []
duplicateList = []
 
for i in lis:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in uniqueList:
        duplicateList.append(i)
 
print(duplicateList)
print(uniqueList)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)    
   