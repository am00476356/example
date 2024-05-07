"""
WAP to check if the string is starting with a vowel?

"""

name = 'Ehreya'
# if name.lower().startswith(('a', 'e', 'i', 'o', 'u')):
#     print('Printed if condition')
#     print('Starts with a vowel')
# elif name.upper().startswith(('a', 'e', 'i', 'o', 'u')):
#     print('Printed elif condition')
#     print('Starts with a vowel')
# else:
#     print('Printed else condition')
#     print('Does not start with a vowel')

# name.lower().startswith(('a', 'e', 'i', 'o', 'u'))
# Ahreya - name
# ahreya - name.lower()
# True - name.lower().startswith(('a', 'e', 'i', 'o', 'u'))
# if code executed

# name.upper().startswith(('a', 'e', 'i', 'o', 'u'))
# Ahreya - name
# AHREYA - name.upper()
# False



# if name.startswith(('a', 'e', 'i', 'o', 'u')):
#     print('Printed if condition')
#     print('Starts with a vowel')
# elif name.startswith(('A', 'E', 'I', 'O', 'U')):
#     print('Printed elif condition')
#     print('Starts with a vowel')
# else:
#     print('Printed else condition')
#     print('Does not start with a vowel')

if name.lower().startswith(('a', 'e', 'i', 'o', 'u')):
    print('starts with vowel')
else:
    print('starts with something else')

