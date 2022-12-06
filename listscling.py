# the list can be easy add and remove and and scling the value easily
store = ['toys','books','pen','bags','laptops']
print(store[0:4:2])
# [startvalue:endvalue:different]
# add the value
# the index value is replace the toys to phone
store[1]='phone'
print(store[1])
newbox = store[0:2]
# it create new copy of store to new box
newbox[0]='paper'
print(newbox)
# copying vs modifiy
# this line is show a store value is copy to the new box
newbox = store[:]
print(newbox)
# ['toys', 'phone', 'pen', 'bags', 'laptops'] copy the original store value
newbox[0] = 'stap'
# replace the value of the 0 th index
print(newbox)