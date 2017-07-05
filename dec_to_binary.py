def decimal_binary(n):
	ans=" "
	while n > 0:
		rem = n%2
		ans = str(rem)+ans
		n//=2
	return ans
	
z = int(input("Number please: "))
val = decimal_binary(z)
print ("The binary equivalent is: %s"%val.zfill(8))