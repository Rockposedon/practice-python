'''
      list formatting with respect to student details
'''

# Get student details for three students
student_1 = [input("Enter name: "), input("Enter course: "), input("Enter email: ")]
student_2 = [input("Enter name: "), input("Enter course: "), input("Enter email: ")]
student_3 = [input("Enter name: "), input("Enter course: "), input("Enter email: ")]

# Print student details using string formatting
print("I am {}. I am a student of {}. My email is {}.".format(student_1[0], student_1[1], student_1[2]))
print("I am {}. I am a student of {}. My email is {}.".format(student_2[0], student_2[1], student_2[2]))
print("I am {}. I am a student of {}. My email is {}.".format(student_3[0], student_3[1], student_3[2]))
