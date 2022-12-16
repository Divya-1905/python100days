
# default parameter is selff  accecs the current  
# object = (class instistance )variable here 
# the take and number is instatance

class student():
    def __init__(self,name ,section,registernumber,address):
        self.name = name
        self.section = section
        self.registernumber = registernumber
        self.address = address
        self.pincode = 62505
        self.phonenumber = 45352398
         # the defult value assign parameter is not called 
        

    def run(self):
        print(f'name is {self.name},registernumber is{self.registernumber},section is {self.section},address is {self.address},pincode is {self.pincode} the phone number is {self.phonenumber}')
        
class regbook(student):
    def __init__(self, name, section, registernumber,address):
        self.name = name
        self.section = section
        self.registernumber = registernumber
        super().__init__(name,section,registernumber,address)
        self.pincode = 625034
take = student('rio','e',19034,'madurai')  
print(take.name) 
take.run()

number = student('user','f',180336,'dsfs')
number.run() 
y = regbook('ssd','er',5689,'fdge')
print(y.pincode)


class libiary():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def run(self):
        print(f'this a {self.name},this type is {self.type}')


y = libiary('bio','science')
y.run()




