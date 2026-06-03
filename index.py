a=int =(input("press 1 for burger press 2 for pizza;"))
if a==1:
    price=30
    quantity=int(input("enter quantity;"))
    total=price*quantity
    print(total)

elif a==2:
    price=65
    quantity=int(input("enter quantity;"))
    total=price*quantity
    print(total)
else:
    print("invalid")    
