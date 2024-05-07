"""
Question1
name = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']
    1. Reverse the above list.
    2. What is the output of name[2][3]
    3. what is the output of
        a. name[-2:3]
        b. name[-6:5]
        c. name[-1:2:-1]
        d. name[1 + 3]
        e. name[:2] = ['unknown','Unknown']
    4. what is the output of :
        a. name.append(["netflix",'walmart','kroger'])
        b. name.extend(['netflix','walmart','kroger'])
    5. write the extended list into:
        a. ascending order in size of chars
        b. descending order in size of chars

Question2
string  = "Hi welcome to Python"
    a. Create a list with each character of the string as its element.
    b. Create a list with each word of the string as its element.

Question3
WAP to find the second-largest number in a list.

Question4
There's a huge event happening
guest_list = ['Sonu Nigam', 'Ajay-Atul', 'Baadshah', 'Amit Trivedi']
# program is over so the action as below is done
guest_list.clear()
what is the output of bool(guest_list) ?
"""


############## Solutions ##############

# Question 1:
name = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']
# reverse the list
name_copy = name.copy()
name_copy.reverse()
print(name_copy)
print(name)

# name[2][3]
x = name[2]  # yahoo
# x[3] ==> name[2][3]
print(name[2][3])

#     3. what is the output of
# name = ['apple','google','yahoo','amazon','facebook','instagram','microsoft']
# 0  1   2  3  4  5  6 #positive
# -7 -6 -5 -4 -3 -2 -1 #negative

#         a. name[-2:3]
#         b. name[-6:5]
#         c. name[-1:2:-1]
#         d. name[1 + 3]
#         e. name[:2] = ['unknown','Unknown']

print(name[-2:3])
print(name[-6:5])
print(name[-1:2:-1])
print(name[1+3])
# name[:2] = ['unknown','Unknown'] # lhs is removed and rhs is added
# print(name)
name.extend(['netflix','walmart','kroger'])
print(name)

sample = []
string = "Hi welcome to Python"
# print(list(string))
sample.extend(string)
print(sample)

# STRING TO LIST --> string.split()
# list to string?? --> join function

my_list = string.split()
print(my_list)

new_str = "$".join(my_list)
print(new_str)
