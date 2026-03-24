from functools import reduce

k = [10,20,50,40,50,60]

# def add(a,b):
#     print(a,b)
#     return a+b

# r = reduce(lambda a,b:a+b,k)
# print(r)

r = reduce(lambda a,b: a if a<b else b,k)
print(r)

