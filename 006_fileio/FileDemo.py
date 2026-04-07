# f = open("D://test.txt",'w')
# f.write("This my first io practical")
# f.close()

f = open("test.txt",'r')
# data = f.read()
# data = f.readlines()

# while True:
#     data = f.readline()
#     print(data)
#     if not data:
#         break
   
# f = open("test.txt",'a')
# f.write("Hello java")
# f.close()


# f = open("test.txt",'w')
# f.writelines(['Hello python','Hello java','Hello php'])
# f.close()


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'Hello' in data:
#         print(data)
#     if not data:
#         break
# f.close()


# with open("test.txt",'r') as f:
#     data = f.read()
#     print(data)


# with open("test.txt",'r') as f:   
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)


# with open("home.txt",'r+') as f:
#     f.write("Hello python")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open('img.jpg','rb') as f:
#     data = f.read()
#     print(data)

import json

d = {"name":"priyanshu","email":"priyanshu@gmail.com"}
with open("data.json",'w') as f:
    json.dump(d,f)
