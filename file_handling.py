'''
	Write a Python program that takes student details (name, English marks, Hindi marks, and Maths marks) 
 	as input, calculates the total and average marks, stores these details in a file, reads the data from 
  	the file, and displays the student's results including their marks and average. (file handling)
'''
# Step 1: Taking input and writing data to marks.txt
marks = open("marks.txt", "w")  # Open marks.txt in write mode
student_name = input("Enter student name: ")
english_m = int(input("Enter marks of English: "))
hindi_m = int(input("Enter marks of Hindi: "))
maths_m = int(input("Enter marks of Maths: "))
details = "{},{},{},{}".format(student_name, english_m, hindi_m, maths_m)
marks.write(details)  # Write student details to the file
marks.close()  # Close the file


# Step 2: Reading marks from marks.txt, calculating average and total marks
data_file = open("marks.txt", "r")  # Open marks.txt in read mode
data = data_file.read()  # Read the content of the file
record = data.split(",")  # Split the data into a list
total = 0
for i in range(1, len(record)):
    total += int(record[i])  # Calculate total marks

average = total / (len(record) - 1)  # Calculate average marks
data_file.close()  # Close the file


# Step 3: Writing data to results.txt
file = open("results.txt", "w")  # Open results.txt in write mode
record.append(str(total))
record.append(str(average))
details = record[0]
for i in range(1, len(record)):
    details += "," + record[i]  # Prepare data to write to results.txt
file.write(details)  # Write data to the file
file.close()  # Close the file


# Step 4: Reading result data and displaying to the user
file = open("results.txt", "r")  # Open results.txt in read mode
data = file.read()  # Read the content of the file
record = data.split(",")  # Split the data into a list


# Display the student's result
print("=========================")
print("Welcome to Our Portal")
print("=========================")
print("Here is your Result")
print("Student name:", record[0])
print("English marks: {} out of {}".format(record[1], 100))
print("Hindi marks:", record[2])
print("Maths marks:", record[3])
print("Total marks:", record[4])
print("Average marks:", record[5])
file.close()  # Close the file
