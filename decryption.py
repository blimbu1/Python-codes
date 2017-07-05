
import math
def dec_to_binary(streng):
	trim = streng.lstrip('0')
	power = 0
	sum = 0
	trim = trim[::-1]
	#print(trim)
	#print(len(trim))
	while power<len(trim):
		if trim[power] == '1':
			sum += int(math.pow(2,power))
		power = power + 1
	return sum

#st = '00001010'
#print(dec_to_binary(st))


salt = {'a':'*','e':' ','i':'+','o':'^','u':'/','b':'1','n':'3','y':'7','l':'£','m':'|','q':'¬'}
salt_two = {'a':'@','e':'~','i':'=','o':'2','u':'1','b':'b','n':'z','y':'"','l':'{','m':'}','q':'#'}

def desalt(dic):
	desalted = {}
	for i in dic.keys():
		desalted[dic[i]] = i
	return desalted
	
reverse_salt = desalt(salt)
reverse_salt_two = desalt(salt_two)


		

source = input("Enter the file name you want to decrypt")
destination = input("What do you want to name the decrypted file")
f = open("%s.txt"%source,"r")
g = open("buffer.txt","w")
binaries = f.read()
for i in range(0,len(binaries),8):
	number=0
	character = binaries[i:i+8]
	number = dec_to_binary(character)
	number = number - 73;
	character_salted = chr(number)
	g.write(character_salted)

g.close()
f.close()

buffer_r = open("buffer.txt","r")
final = open("%s.txt"%destination,"w")
z = buffer_r.read()
for i in z:
	if i in reverse_salt.keys():
		final.write(reverse_salt[i])
	else:
		final.write(i)
		
final.close()
buffer_r.close()
		




	