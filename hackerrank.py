# if __name__ == '__main__':
#     n = int(input("enter the value : "))
#     for i in range(1,n+1):
#         print(i,end="")
#!/bin/python3

import math
import os
import random
import re
import sys
# n = int(input("enter the no. : "))
# if n%2 == 0 :
#     print("Weird")
# elif n%2 == 0 and range(2,6):
#     print("Not Weird")
# elif n%2 == 0 and range(6,20):
#     print("Weird")
# elif n%2 == 0 and n>20:
#     print("Not Weird")
# else :
#     print("Weird")
# n = int(input("enter the numbers of element of tuple :"))
# t1 = (n)
# print(t1)
str1 = input("enter string : ")
def a():
    if str1 == str1.upper():
        print(str1.lower())
    elif str1 == str1.lower():
        print(str1.upper())
str2 = str1.upper()
str3 = str1.lower()
print(str2,str3)
a()


#-----------------------------------------------------------------------
# num_chr=["0","1","2","3","4","5","6","7","8","9"]
# num_count=0
# dot_count=0
# other_count=0

# def a():
#     user_value = input("enter value:")
#     num_chr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     num_count = 0
#     dot_count = 0
#     other_count = 0
#     for i in user_value:
#         if i in num_chr:
#             num_count += 1
#         elif i == "." :
#             dot_count += 1
#         else:
#             other_count += 1
#     if other_count==0 and dot_count==0:
#         user_value=int(user_value)
#     elif other_count==0 and dot_count==1:
#         user_value=float(user_value)
#     else:
#         user_value=str(user_value)
#     print("user_value = ", user_value)
#     print("user_value_type = ", type(user_value))
#
# a()