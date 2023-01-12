def cal():
    print("welcome to my claculator ")
    var1 = int(input("enter value 1 : "))
    var2 = int(input("enter value 2 : "))
    choice = input("enter 1 for addition : \n enter 2 for subtraction : \n enter 3 for multiplication : \n enter 4 for division : \n enter 5 for power : \n")
    if choice == '1':
        result = var1 + var1
        print("result = ", result)
    elif choice == '2':
        result = var1-var2
        print("result = ", result)
    elif choice == '3':
        result = var1* var2
        print("result = ", result)
    elif choice == '4':
        result = var1/var2
        print("result = ", result)
    elif choice == '5':
        result = var1**var2
        print(result)
    else:
        print("entered wrong choice ")
        cal()



