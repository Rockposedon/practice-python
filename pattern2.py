# num = int(input("enter number : "))
# for n in range(1, num+1 ):
#     for i in range( n,0, -1):
#         print(i, end=" ")
#     print("")


# num = int(input("enter number : "))
# for n in range(1, num+1 ):
#     for i in range(0, n+1):
#         for j in range(0,i+1,-1):
#             print(j, end=" ")
#         print("")
#


# num = int(input("enter number : "))
# for n in range(1, num+1):
#     print(" " * (num - n) + str(n) * n)

rows = int(input("enter value : "))
for row in range(1, rows+1):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num += 1
    print(" ")