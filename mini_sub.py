'''
        problem statement :
        
        Write a Python program to collect the internal marks of students and 
        calculate their total marks based on the best two internals out of three. 
        The program should also assign grades based on the total marks and save 
        the student details along with their marks and grades to a file named "marks2.txt" 
'''
# Creating function named marks to calculate the marks of the students
def marks():
    markss = open("marks2.txt", "a")  # Open "marks2.txt" in append mode
    student_name = input("Enter student name: ")
    roll_no = input("Enter roll number of student: ")
    first_internal = int(input("Enter marks obtained in 1st internal: "))
    second_internal = int(input("Enter marks obtained in 2nd internal: "))
    third_internal = int(input("Enter marks obtained in 3rd internal: "))

    # Calculate total marks based on the highest two internals
    if first_internal > second_internal:
        if second_internal > third_internal:
            total = first_internal + second_internal
        else:
            total = first_internal + third_internal
    elif first_internal > third_internal:
        total = first_internal + second_internal
    else:
        total = second_internal + third_internal

    # Assign grades based on total marks
    if total > 35:
        grade = "A+"
    elif total > 30:
        grade = "A"
    elif total > 25:
        grade = "B"
    elif total > 20:
        grade = "C"
    elif total > 0:
        grade = "D"

    # Create details string and write to the file
    details = "{},{},{},{},{},{}\n".format(student_name, roll_no, first_internal, second_internal, third_internal, grade)
    markss.write(details)
    markss.close()  # Close the file after writing

student_no = int(input("Enter number of students: "))
for i in range(student_no):
    marks()  # Call the marks() function for each student
