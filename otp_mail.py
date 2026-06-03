import random
otp=random.randrange(0000,9999)
print(otp)


a=int(input("enter otp:"))
if a==otp:
    a=int(input("enter value:"))
    b=int(input("enter value:"))
    print(a+b)
else:
    print("invalid otp")
