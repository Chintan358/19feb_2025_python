number = 153
l = len(str(number))
temp = number
sum =0
while number !=0:
    rem = number%10
    sum+=pow(rem,l)
    # number = number//10
    number//=10

if temp==sum:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")


    