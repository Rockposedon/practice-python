def marks():
    markss = open("marks2.txt", "a")
    student_name = input("enter student name : ")
    roll_no = input("enter roll number of student : ")
    first_internal = int(input("enter marks obtained in 1st internal : "))
    second_internal = int(input("enter marks obtained in 2nd internal : "))
    third_internal = int(input("enter marks obtained in 3rd internal: "))

    if (first_internal > second_internal):
        if (second_internal >third_internal):
            total = first_internal + second_internal
        else:
            total = first_internal + third_internal
    elif (first_internal > third_internal):
        total = first_internal + second_internal
    else:
        total = second_internal + third_internal

    if total > 35:
        print("grade : A+ ")
    elif total > 30:
        print("grade : A ")
    elif total > 25 :
        print("grade : B ")
    elif total > 20 :
        print("grade : C ")
    elif total > 0 :
        print("grade : D")

    details = "{},{},{},{},{},{}\n".format(student_name, roll_no, first_internal, second_internal, third_internal,total)
    markss.write(details)
    markss.close()
student_no = int(input("enter number of students :"))
for i in range(0,student_no):
    marks()




