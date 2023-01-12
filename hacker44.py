# # if __name__ == '__main__':
# #     N = int(input())
# #     list1 = [ ]
# #     i=list1.index()
# #     element=input("enter inserting value :")
# #     list.insert(i,element)
#
# # numb=int(input("enter any number"))
# # facts=[]
# # for a in range(1,numb):
# #     if numb%a==0:
# #        facts.append(a)
# # print ("Factors of {} = {}".format(numb,facts))
# # a=facts
# # print(a)
#
# import math
# def prime_factors(num):
#     while num % 2 == 0:
#         print(2, )
#         num = num / 2
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         while num % i == 0:
#             print(i, )
#             num = num / i
#     if num > 2:
#         print(num)
# num = int(input("enter no:"))
# prime_factors(num)
# num1 = list(num)
# print(num1)


list1= ['2','3','5','7','11','13','17','19']
number = int(input("enter value : "))
square_root = number**(1/2)
print(square_root)
