bag = ['pencil']
for i in enumerate (bag):
    print(i)  #enumrate is return iterator key  
for i,char in enumerate(bag):
    print(i)   # bag value are index value   
for i in enumerate(list(range(60))):
    print(i)
    # if char == 10:
    #     print(f'correct:{i}')
  
x = list('python')
for i in enumerate(x):
    print(i,end='')  
    
u ={2:3,5:6,8:9}
result = u.pop(5,8)
print(result)          