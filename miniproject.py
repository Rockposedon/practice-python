# Step 1: Writing student marks to marks1.txt
marks = open("marks1.txt", "w")  # Open the file marks1.txt for writing

student_name = input("Enter student name: ")  
english_marks = int(input("Enter marks obtained in English: "))  
hindi_marks = int(input("Enter marks obtained in Hindi: "))  
maths_marks = int(input("Enter marks obtained in Maths: "))  

details = "{},{},{},{}".format(student_name, english_marks, hindi_marks, maths_marks)  # Format student details

marks.write(details)  # Write student details to the file

marks.close()  # Close the file


# Step 2: Reading marks from marks1.txt and calculating average and total marks
data_file = open("marks1.txt", "r")  # Open marks1.txt for reading

data = data_file.read()  # Read data from the file

data_file.close()  # Close the file

record = data.split(",")  # Split data into individual elements

total = 0

for i in range(1, len(record)):  
    total = total + int(record[i])  
average = total / (len(record) - 1) 


# Step 3: Writing data to results.txt
file = open("results.txt", "w")  # Open results.txt for writing

record.append(str(total))  # Add total marks to the record

record.append(str(average))  # Add average marks to the record

details = record[0]  # Initialize details with student name

for i in range(1, len(record)):  # Loop through record elements
    details = details + "," + record[i]  # Concatenate elements with commas

file.write(details)  # Write student details, total, and average marks to the file

file.close()  # Close the file
