source = input("Please enter the name of the file you want to open:")
g = open("%s.txt"%source,"r")
reading = g.read()
print(reading[0:10])
g.close()