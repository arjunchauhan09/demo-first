password = "secure3p@"

password_lenth = len(password)

if len(password) < 60:
    strenth = "week"
elif len(password) <= 10:
    strenth = "medium"
else:

    strenth ="strong"

    print("password strenth is:",strenth)