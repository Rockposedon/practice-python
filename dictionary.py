d1 ={"name":"paritosh","name":"don", "class":"mca", "subject":"science"}
print(d1)
#print keys only
#for i in d1:
	#print(i)
	#print values only
	#print(d1[i])
#print items(both)
for i,j in d1.items():
	print(i)
	print(j)
# print(d1.values())	
# print(d1.items())
# print(d1.keys())
d2 ={1:"21",2:"31",3:"41",3:"2121"}
print(d2)
for i,j in d2.items():
	print(i,j)
d1["name"]="paritosh verma"
print(d1)	
d1["school"]="TKS"
print(d1)
#delete values using there key
d1.pop("school")
print(d1)
d1.remove()
