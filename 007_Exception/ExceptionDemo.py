
print("Program started")

try :
    # a = 10
    # b = a/0
    # print(b)
    print(10+"dsds")
except Exception as e:
    print("exception")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

else:
    print("sucess")
finally:
    print("always executable")

print("Program ended")
