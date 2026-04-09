# def before(func):
#     def exec():
#         print("calling before test")
#         func()
#     return exec

# def after(func):
#     def exec():
#         func()
#         print("calling after test")
        
#     return exec


# @after
# @before
# def test():
#     print("Test function calling")
# test()

# def add(func):
#     def exec(*k):
#         func(*k)
#         print(f"addtion of {k[0]} and {k[1]} is {k[0]+k[1]}")
#     return exec


# def mul(func):
#     def exec(*k):
#         func(*k)
#         print(f"multiplication of {k[0]} and {k[1]} is {k[0]*k[1]}")
#     return exec

# @add
# @mul
# def calc(a,b):
#     pass

# calc(10,20)

def numonly(func):
    def exec(v):
        if not str(v).isdigit():
            print("Invalid value")
        else:
            func(v)
    return exec

def charonly(func):
    def exec(v):
        if not str(v).isalpha():
            print("Invalid value")
        else:
            func(v)
    return exec
        
@charonly
def get(value):
    print(value)

get("sds")