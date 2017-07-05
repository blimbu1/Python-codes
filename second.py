num1 = input("Input number one")
if int(num1) > 100:
	print("A")
	if int(num1) > 500:
		print("1")
	else:
		print("2")
else:
	print("B")
	if int(num1) < 50:
		print ("4")
	else:
		print("3")
