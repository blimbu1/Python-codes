tax = 0.00
bonus = 0.00
salary = input("Plese enter your salary? ")
if not salary.isdigit():
        print ("Please input YOUR CORRECT SALARY")
        salary = 0.00
else:
        salary = float(salary)
#print ("Salary is %.2f"%salary)
dept =input("Please enter your dept? ")
if dept.upper() != "IT" or dept.upper()!="HR":
        print("Please input either IT or HR")
grade = input("Please enter your grade ")
if not grade.isdigit():
        if grade.upper()!="CTO":
                print("Please input CORRECT GRADE")
        
if(dept.upper() == "IT"):
	bonus = 0.05*salary
	if int(grade) >=1 and int(grade)<=10:
		tax = float(0.09 * salary)
	elif int(grade)>=11 and int(grade)<=20:
		tax = float(0.15 * salary)
	elif grade.upper() == "CTO":
		tax = 0
	#else:
	#	print("Please enter the correct GRADE category")
elif (dept.upper() == "HR"):
	bonus = 0
	if int(grade)>=1 and int(grade)<=10:
		tax = float(0.09 * salary)
	elif int(grade)>=11 and int(grade)<=20:
		tax = float(0.17 * salary)
	elif grade.upper() == "CTO":
		tax = float(0.02 * salary)
	#else:
	#	print("Enter the correct GRADE category please!")
#else:
#	print("Please enter the correct DEPARTMENT")
print("your dept is:%s"%dept)
print("your tax is: %.2f"%round(tax,2))
print("Your bonus is: %.2f"%round(bonus,2))
