# First approach to finding the leap year
n = int(input(" enter value : "))
if n%4 == 0:
    print("Give year is leap year")
    if n%100 != 0:
        pass
else:
    if n%400 ==0 :
            print("Give year is leap year")
    else:
            print("not a leap year")

# Another approach to finding the leap year
n = int(input(" enter value : "))
if n%400 == 0 and n%100 == 0 :
    print("year is leap year")
elif n%4 == 0 and n%100 != 0:
    print("year is leap year")
else :
    print("year is not a leap year")


