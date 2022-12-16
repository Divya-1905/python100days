# import math
# def squarroot(numbers):
#     fun =[]
#     for number in numbers:
#         fun.append(math.sqrt(number))
#     return fun   
# numbers = [2,2,4,5]
# squarroot(numbers)
import math
def squareroot(numbers):
    result = []
    for number in numbers:
      result.append(math.sqrt(number))
      result.append(numbers*numbers)
      return result
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]
squareroot(numbers)