#step:1
marks = open("marks.txt","w")
student_name = input("enter student name : ")
enlgish_m= int(input("enter marks of english : "))
hindi_m= int(input("enter marks of hindi : "))
maths_m= int(input("enter marks of maths : "))
details = "{},{},{},{}".format(student_name,enlgish_m,hindi_m,maths_m)
marks.write(details)
marks.close()


#step:2 reading marks from marks.txt and calculating average and total marks
data_file = open("marks.txt","r")
data = data_file.read()
#print(data)
record =data.split(",")
#print(record)
total = 0
for i in range(1,len(record)):
	total = total + int(record[i])

average = total/(len(record)-1)
#print(total,average)
data_file.close()


#step:3 writing data in result.txt
file = open("results.txt","w")
record.append(str(total))
record.append(str(average))
#print(record)

details = record[0]
for i in range(1,len(record)) :
	details = details + "," + record[i]
print(details)
file.write(details)
file.close()

#step:4 read result data and display to the user 
file = open("results.txt","r")
data = file.read()
record = data.split(",")
print("=========================")
print("Welcome to Our Portal")
print("=========================")
print("Here is your Result")
print("student name :", record[0])
print("english marks :{} out of {}".format( record[1],100))
print("hindi marks :", record[2])
print("maths marks :", record[3])
print("total marks :", record[4])
print("average marks :", record[5])
file.close()