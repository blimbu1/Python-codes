user = input("Please input your string: ")
length = len(user)
print("length is: %d" %length)
save = {}
buff = {}
for j,i in enumerate(user):
	count = 1
	val = ord(i)
	if val>64 and val<91:
		val = (val+32)
	print (val)
	#print (i,val,second)
	for p in range(j+1,length):
		third = ord(user[p])
		if third>64 and third<91:
			third = (third+32)
		if val== third:
			count = count +1
			#print("count for %s is %d"%(i,count))
	
	if val not in save.keys():save[val] = count
#print (save)
for m in save:
	print("%s: %d"%(chr(m),save[m]))