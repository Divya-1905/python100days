# row = ('r','e','r','t','y','u')
# duplicate =[]
# for i in row:
#     if row.count(i)>1:
#         duplicate.append(i) 
# print(duplicate) 
row = ('r','e','e','r')
p = []
for i in row:
    if row.count(i)>1:
        if i not in p : #this line not repeate the value give only duplicate value
         p.append(i)
print(p)        
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)       