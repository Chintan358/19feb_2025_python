l = [4,5,7,8,9,40,6,13,17]
# c = []

# def checkodd(a):
#     if a%2==0:
#         return a
    
# for i in l:
#     k = checkodd(i)
#     if k is not None:
#         c.append(k)
# print(c)

# # c = filter(checkodd,l)
# c = filter(lambda k : k%2==0 ,l)
# print(list(c))


# sub = ["python","php","java","node","android"]
# k =filter(lambda x:"a" in x,sub)
# print(list(k))

import math

l = [2,5,9,8,25,49,45,81,144,22,33]

# def sqrt(a):
# #    k =  a**0.5
#     k = math.sqrt(a)
#     if k.is_integer():
#       return k
   
# k = filter(sqrt,l)
# k = filter(lambda a : math.sqrt(a).is_integer() ,l)
# print(list(k))
   


