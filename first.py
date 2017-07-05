no1 = input("First number ")
no2 = input("Second number ")
no3 = int(no1) + int(no2)
print("First Number: %s\n"%no1)
print("Second Number: %s\n"%no2)
print ("The total is: %d\n" %no3)
if no3>10:
	print("%d > 10: Good" %no3)
else:
	print("%d < 10: Very bad" %no3)
