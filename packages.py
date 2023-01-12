# import time as t
#import time
from time import *


def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x* fact(x-1)
var1 = int(input("enter value : "))
start_time = time()
result = fact(var1)
print("factorial of {} is {}".format(var1,result))

end_time = time()
total = end_time - start_time
print("total time for execution of program : ",total)