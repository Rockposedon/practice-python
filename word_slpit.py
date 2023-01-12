# a = "paritosh verma"
# for i in a:
# 	print(i)
# word_list = list(a)
# print(word_list)

inp1 = input("enter value : ")
word_list = [ ]
temp_word = " "
for i in range(len(inp1)):
	if inp1[i] == " ":
		word_list.append(temp_word)
		temp_word = " " 
	else:
		temp_word = temp_word + inp1[i]
word_list.append(temp_word)
print("user defined sentence is ", inp1)
print("word list is",word_list )


print(inp1.split( ))















