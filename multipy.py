num1 = input("Table from: ")
num2 = input("Table to: ")
if int(num1)<int(num2):
	start = int(num1)
	end = int(num2)+1
	step = 1
else:
	start = int(num1)
	end = int(num2)-1
	step = -1
	print("%d, %d,%d" %(start,end,step))
for i in range(start,end,step):
	for j in range(1,11):
		print ("%d x %d = %d" %(i, j, (i*j)))
	print ("\n",end = "")
		
