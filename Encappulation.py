class players():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def run(self):
        print('run')
    def fight(self):
        print(f'my name is{self.name} ,and my age is{self.age} year old')
player1 = players('dfdgf',12) 
print(player1.age) 
player2 = {'name':'sdf','age':21}
print(player2['age'])  # this [] way taken value of key     
 
'''  
i f bundling data and methods within a single unit. So,
for example, when you create a class, it means you are implementing encapsulation
'''
player1.fight ='hai'
print(player1.fight)