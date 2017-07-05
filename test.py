do = True
while do:
	try:
		c = "1"
		z = 1/c
		print(z)
	except TypeError:
		c = 1
		print ("Do not divide by a string")
	else:
		print ("Good Job!")
		do = False
	finally:
		print("printing finally")

		