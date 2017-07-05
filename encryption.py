
def decimal_binary(n):
	ans=""
	while n>0:
		rem = n%2
		n//=2
		ans =  str(rem) + ans
	return ans.zfill(8)
	
original = input("Enter the name of the file you want to encrypt: ")
encrypted = input("Name you want to give the encrypted file: ")
salt = {'a':'*','e':' ','i':'+','o':'^','u':'/','b':'1','n':'3','y':'7','l':'£','m':'|','q':'¬'}
salt_two = {'a':'@','e':'~','i':'=','o':'2','u':'1','b':'b','n':'z','y':'"','l':'{','m':'}','q':'#'}
g = open("%s.txt"%original,"r")
h = open("%s.txt"%encrypted,"w")
reading = g.read()
for i in reading:
	if i in salt:
		cha = salt[i]
		cha1 = salt_two[i]
		val = ord(cha)+73
		val1 = ord(cha1)+73
		streeng = decimal_binary(val)
		streeng1 = decimal_binary(val1)
		h.write(streeng)
		h.write(streeng1)
	else:
		value = ord(i) + 73
		put = decimal_binary(value)
		h.write(put)
g.close()
h.close()



