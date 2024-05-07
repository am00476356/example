"""
WAP to check if the entered character is vowel or not
if the character is a vowel create a dictionary
with character as key and ascii value of the character as value.


ord(character)
"""

character = 'a'
output_dict = {}
if character.lower() in 'aeiou':
    output_dict[character] = ord(character) # dict_name[keyname] = value

print(output_dict)
