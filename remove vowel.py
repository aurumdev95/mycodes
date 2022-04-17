#consonant and vowel remover
#import re


final_str = None
def vowelRemover(given_str):
	vowels = 'aeiouAEIOU'
	final_str = given_str
	for c in given_str:
	       	if c in vowels:
	       		final_str = final_str.replace(c,"")
	print(final_str)
        	
def consRemover(given_str):
	consonant = "qwrtypsdfghjklxzcvbnmQWRTYPSDFGHJKLZXCVBNM"
	final_str = given_str
	for c in given_str:
	       	if c in consonant:
	       		final_str = final_str.replace(c,"")
	print(final_str)


while True:
	option = input("choose c to remove consonant \n and choose v to remove vowel:").lower()
	if option == "c":
		given_str = input("Enter a string : ")
		
		consRemover(given_str)
		continue
	elif option == "v":
			given_str = input("Enter a string : ")
			vowelRemover(given_str)
			

#print(final_str)