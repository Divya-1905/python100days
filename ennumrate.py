bag = ['pencil']
for i in enumerate (bag):
    print(i)  #enumrate is return a index value of the bag 
for i,char in enumerate(bag):
    print(i)   # bag value are index value   
for i,char in enumerate(list(range(60))):
    if char == 10:
        print(f'correct:{i}')
        