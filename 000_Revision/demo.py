# l = [10,20,30,40,50]

# for i in l:
#     print(i)

# it = iter(l)

# print(next(it))
# print(next(it))
# print(list(it))


# def square(a):
#     for i in range(1,a):
#         yield i*i

# k = square(5)
# print(next(k))
# print(next(k))
# print(list(k))



# l = [10,20,30,40]
# k = ["python","java","php","android"]

# a = zip(l,k)
# # print(dict(a))
# print(list(a))


# k = [(10, 'python'), (20, 'java'), (30, 'php'), (40, 'android')]

# t = zip(*k)
# print(next(t))
# print(next(t))


a = [10,20,30]
b = [40,50,60]

# k = [x+y for x,y in zip(a,b)]
# print(k)

# k = map(lambda x,y:x+y,a,b)
# print(list(k))

# l = [5,4,8,9,6,4,2,7,4,9]

# l.sort()
# k = sorted(l)
# print(k)


d = {10:"krish",9:"priyanshu",11:"manish",8:"yash",78:"abc"}

# k = list(d.values())
# k.sort()
# dk = {}

# for i in k:
#     for x,y in d.items():
#         if y==i:
#             dk.update({x:i})
# print(dk)

# k = dict(sorted(d.items(),key=lambda item: item[1]))
# print(k)


def square(a):
    print(a*a)
    a+=1
    if a<=20:
        square(a)

square(1)