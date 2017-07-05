vowel = "QA Consulting"
consonant = "Office for National Statistics"
vowel_check = "aeiou"
for ele in vowel:
	if ele.lower() in vowel_check:
		print(ele,end="")

print("\n")

for ele in consonant:
	if ele.lower() not in vowel_check:
		print(ele,end="")
