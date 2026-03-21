# d = {
#     "name":"krish",
#     "email":"krish@gmail.com",
#     "name":"yash",
#     123 : "abc",
#     12.33 : "gffdf",
#     True:"fdfdfdf",
#     (10,20,30):"fddfdfd",
#     # [10,20,30]:"ffdfdf",
#     # {10,20,30}:"ffdgf",
#     # {"a":"fdfd"} : "dffgf"
# }

# print(d)
# print(type(d))
# print(len(d))

# student = {
#     "name":"mohit",
#     "email":"mohit@gmail.com",
#     "phone":"9585748596"
# }

# student["name1"] ="xyz"
# print(student["name1"])
# print(student.get("name1"))
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student)


# for i,j in student.items():
#     print(i,j)

# student.update({"age":30})

# student.pop("name")
# student.popitem()
# student.clear()
# del student
# print(student)


# k = student.copy()
# k = dict(student)
# k = student
# print(k)

# student = {
#     "name":"mohit",
#     "email":"mohit@gmail.com",
#     "phone":"9585748596",
#     "address" : {
#         "city":"surat",
#         "state":"gujarat",
#         "country":"India"
#     },
#     "lang":["gujarati","Hindi","English"]
# }

# print(student['address']['country'])
# print(student['lang'][0])


# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }  


# for i,j in myfamily.items():
#     print(i)
#     for x,y in j.items():
#         print(x,y)


# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x,y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# y = ("abc","xyz","pqr")
# d = dict(zip(x,y))
# print(d)

d = {
    "subject":"python",
    "marks":"123"
}

# d['subject']="ffsd"
d.setdefault("subject","fddff")
print(d)