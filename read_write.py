destination = input("Please enter what you want to name you file?")
source = input("Please enter the name of the file you want to copy your file from")
search = input("What do you want to search?")
repalce = input("What do you want to repalce with")
g = open("%s.txt"%source,"r")
h = open("%s.txt"%destination,"w")
reading = g.read()
print(reading)
for i in reading:
	if i==search:
		h.write(repalce)
	else:
		h.write(i)
g.close()
h.close()
