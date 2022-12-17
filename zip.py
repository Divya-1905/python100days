x =[[1,2,3],[4,6,7,],[7,8]]
for y in zip(*x):
    print(y,end='')
    
    
    #zip is give (1,4,7),(2,6,8)(3,7)