import re

# r = re.match("in","sun rises in east")
# r = re.search("in","sun rises in in east")
# r = re.findall("in","sun in rises in east")
# r = re.finditer("in","sun in rises in east")
# print(next(r))
# print(next(r))

# r = re.sub("s","T","sun rises in east")

# r = re.split("","sun rises in east")
# print(r)



# k = re.findall("s.n","sun rese skn in east")

# k = re.search("^sun","k sun rises in east")
# k = re.search("east$","k sun rises in east")

# k = re.findall("su*n","k sun rises sn suuun in east")
# k = re.findall("su+n","k sauaun rises sn suuun in east")
# k = re.findall("su?n","k sun rises sn suuun in east")

# k = re.findall("[0-9a-z]","k  @ sun rises 898 sn suuun in east 898")
# print(k)


# k = re.findall(r"\d","k sun 89  @$ rises sn suuun 898  in east")

# k = re.findall(r"\D","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\W","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\S","k sun 89  @$ rises sn suuun 898  in east")


# k = re.findall(r"\Bses","k sun 89  @$ rises sn suuunses 898  in east")
# print(k)


# number = input("enter number : ")
# k = re.match("^[0-9]{10}$",number)
# if k is None:
#     print("Invalid number")
# else:
#     print(number)

email = "chintan@gmail.com"

k = re.match("^[a-z0-9_-]+@[a-z]+\\.[a-z]{2,4}$",email)
print(k)