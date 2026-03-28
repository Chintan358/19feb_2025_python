# l = [10,20,30,40,50,60]
# it = iter(l)
# print(next(it))
# print("Hello")
# print("python")
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def test():
#     yield "Hello"
#     yield "Python"

# k = test()
# print(next(k))
# print(next(k))


def calc(a):
    for i in range(1,a):
        yield i*i
    
k = calc(10)
print(next(k))
print(next(k))
print(next(k))
print(next(k))