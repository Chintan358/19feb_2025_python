# s = {10,20,30,40,50,50,1,True,False,0}
# print(s)
# print(type(s))
# print(len(s))

# s = {10}
# print(s)
# print(type(s))

# l = set()
# print(type(l))

s = {10,20,30,40,50,60}

# for i in s :
#     print(i)

# print(10 in s)

# s.add(800)
# print(s)

# s.remove(100)
# s.discard(100)
# print(s)

# s.pop()
# print(s)

# s.clear()
# del s
# print(s)


a = {10,20,30,40,50,True}
b = {40,50,60,70,80,1}

# a.update(b)
# c = a.union(b)
# c = a|b
# print(c)

# a.intersection_update(b)
# c = a.intersection(b)
# c  =a & b
# print(c)

# a.difference_update(b)
# c = a.difference(b)
# c = b-a
# print(c)

# a.symmetric_difference_update(b)
# c = a.symmetric_difference(b)
# c = a^b
# print(c)

# k = frozenset({10,20,30})
# print(k)

# k = a.copy()
# print(k)



# a = {10,20,30,40}
# b = {100,500}

# print(b.issubset(a))
# print(a.issuperset(b))
print(a.isdisjoint(b))