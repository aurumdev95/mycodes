import json


ay = "ay"
way = "way"

consonant = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
vowel = ["A","E","I","O","U"]

user_word = input("Enter a word to translate to Pig Latin: ")
# getting first letter and making sure its a string and setting it to uppercase
first_letter = user_word[0]
first_letter = str(first_letter)
first_letter=first_letter.upper()
if first_letter in consonant:
   print(first_letter,"is a consonant")
   
   length_of_word = len(user_word)
   remove_first_letter = user_word[1:length_of_word]
   pig_latin=remove_first_letter+first_letter+ay
   print("The word in Pig Latin is:",pig_latin)
elif first_letter in vowel:
   print(first_letter, "is a vowel")
   pig_latin=user_word+way
   print("The word in Pig Latin is:",pig_latin)
else:
   print("I dont know what",first_letter,"is")