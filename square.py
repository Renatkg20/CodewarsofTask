import math
# def is_square(n):
#   if n < 0:
#     output = (f"{n}: Negative numbers cannot be square numbers")
#   else:
#     result = math.sqrt(n)
#     if len(str(result).split('.')[-1]) > 2:
#       output = f"{n} is not a square number"
#     elif len(str(result).split('.')[-1]) == 1:
# 	    output = f"{n} is a square number"   
    
#   return output

def is_square(n):    
    return n>=0 and math.sqrt(n).is_integer()

print(is_square(-1))

#result = math.sqrt(n)