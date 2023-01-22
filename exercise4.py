x = int(input("Enter a number: "))
div=[]
for y in range(1,x+1):
	a=int(x/y)
if x-a*y==0:
	div.append(y)

print(div)