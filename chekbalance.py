ch=int(input('''enter your choice:
             1 for deposite
             2 for withrawal
             3 for chekbalance'''))
if ch==1:
    a=20000
    d=eval(input("enter your amount to deposite:"))
    f=d+a
    print("print final amount is:",f)
elif ch==2 :
    a=20000
    w=eval(input("enter your amount to widral:"))
    if w<a:
        print(a-w)
    else :
        print("you dont have a appropriate amount")

else:
    a=20000
    print("your final prise to pay is :",a)