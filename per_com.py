# import  sample_one_fact
# import sample_one_fact as s
from sample_one_fact import *


#calculating permutation :
n,r = int(input("enter value of n :")) , int(input("enter value of r :"))
if n > r :
    result = facto(n)/facto(n-r)
    print("permutation is : ",result)
elif n == r :
    r1 = facto(n)
    print("permutation is : ",r1)
else :
    print("n will be always greater ,so enter new value ")


#calculating combination :
if n > r:
    result2 = facto(n)/facto(r)*facto(n-r)
    print("combination is : ", result2)
elif n == r :
    print("combination is : ",1)
else :
    print("n will be always greater then r ")

