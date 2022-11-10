# 1 - Print The Greatest Number

# x = int(input("Please Enter First Number: "))
# y = int(input("Please Enter Second Number: "))
# if x > y:
#     print("The Greatest Number is ", x)
# elif x < y:
#     print("The Greatest Number is ", y)
# else:
#     print("!!! Two Numbers Are Equal !!!")

# ======================================================================

# 2 - Print the Corresponding Grade

# mark = int(input("Please Enter Your Mark in Range of (0 to 100): "))
# if 0 < mark <= 100:
#     if mark < 25:
#         print("Your Grade is: F")
#     elif 25 <= mark < 45:
#         print("Your Grade is: E")
#     elif 45 <= mark < 50:
#         print("Your Grade is: D")
#     elif 50 <= mark < 60:
#         print("Your Grade is: C")
#     elif 60 <= mark < 80:
#         print("Your Grade is: B")
#     elif 80 <= mark <= 100:
#         print("Your Grade is: A")
# else:
#     print("!!!! Enter Number In The Range !!!!")

# ======================================================================

# 3 - The Oldest and Youngest Age

# # print("Enter The Three Ages From ")

x = int(input("Plz Enter 1st Age: "))
y = int(input("Plz Enter 2cd Age: "))
z = int(input("Plz Enter 3rd Age: "))
if y < x > z:
    print("The Oldest Age is:", x)
    if y > z:
        print("The Youngest Age is:", z)
    elif y == z:
        print("The Other 2 Persons are Equal")
    else:
        print("The Youngest Age is:", y)
elif x < y > z:
    print("The Oldest Age is:", y)
    if x > z:
        print("The Youngest Age is:", z)
    elif x == z:
        print("The Other 2 Persons are Equal")
    else:
        print("The Youngest Age is:", x)
elif y < z > x:
    print("The Oldest Age is:", z)
    if y > x:
        print("The Youngest Age is:", x)
    elif y == x:
        print("The Other 2 Persons are Equal")
    else:
        print("The Youngest Age is:", y)
elif x == y == z:
    print("The 3 Persons are the Same Age")
else:
    print("!!!! Please Enter Valid Number !!!!")


print('hello from stash')
a = 50
b = 70
c = 20
d = 10
e = 5
b = 70
f = 5