animal = []
birds = []
user = str(input('enter the name'))
print(user)
if user == 'lion':
          animal.append(user)
          print(animal)  
elif user =='sparrow':
        birds.append(user) 
        print(birds)
# print(animal)       

class zoo():
    def __init__(self,name,age):
        self.name =name
        self.age=age
    def run(self):
        print(f'this a {self.name},its age is{self.age}') 
    

                   
x = zoo('python',3)
x.run()       
y = zoo('sparow',2)
y.run()