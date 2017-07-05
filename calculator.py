def addition(a,b):
	return a + b
	
def subtraction(a,b):
	return a-b
	
def division(a,b):
	return a/b
	
def multiplication(a,b):
	return a * b
	
def inputs():
	done = True
	while done:
		num1 = input("Enter first number?")
		num2 = input("Enter second number?")
		done = check_input(num1,num2)
	return float(num1),float (num2)
	
def check_input(num1,num2):
	if num1.isdigit() and num2.isdigit():
		return False
	else:
		print("Please enter TWO NUMBERS to perform MATHEMATICAL CALCULATION")
		return True

def timesTable(start, end, step):
	for i in range(int(start),int(end),int(step)):
		for j in range(1,11):
			print ("%d x %d = %d" %(i, j, (i*j)))
		print ("\n",end = "")
		
def options():
	print ("Options")
	print ("1-addition")
	print ("2-subraction")
	print ("3-division")
	print ("4-multiplication")
	print ("5-timesTable")
	print ("6-quit")
	


def operation(val):
	#options()
	#val = input("Enter you choice")
	mini = True
	if val==1:
		while mini:
			a,b = inputs()
			print ("The result is: %.2f"%(addition(a,b)))
			select = input("Do you want to Repeat the process? Y/N")
			mini = True if select.upper() == 'Y' else False
			
	if val==2:
		while mini:
			a,b = inputs()
			print ("The result is: %.2f"%(subtraction(a,b)))
			select = input("Do you want to Repeat the process? Y/N")
			mini = True if select.upper() == 'Y' else False
			
	if val==3:
		while mini:
			a,b = inputs()
			print ("The result is: %.2f"%(division(a,b)))
			select = input("Do you want to Repeat the process? Y/N")
			mini = True if select.upper()=='Y' else False
			
	if val==4:
		while mini:
			a,b = inputs()
			print ("The result is: %.2f"%(multiplication(a,b)))
			select = input("Do you want to Repeat the process? Y/N")
			mini = True if select.upper()=='Y' else False
			
	if val==5:
		while mini:
			a,b = inputs()
			b,step = (b+1,1) if a<b else (b-1,-1)
				
			print ("Multiplication table \n")
			timesTable(a,b,step)
			select = input("Do you want to Repeat the process? Y/N")
			mini = True if select.upper() == 'Y' else False
	
condition = True
option = True		
while condition:
	while option:
		options()
		value_final = input("Enter your choice?: ")
		if not value_final.isdigit() or int(value_final)<1 or int(value_final)>6:
			print("Please LIMIT your SELECTION BETWEEN 1 AND 6")
		elif int(value_final) == 6:
			option = False
			condition = False
		else:
			operation(int(value_final))
	#condition = False

