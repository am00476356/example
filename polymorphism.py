"""
Polymorphism

"""

a = 1+1
print(a)  # 2 --> Addition of number

b = "Hello" + " world"
print(b)  # Hello world --> concatenation of strings

c = [1, 2, 3] + [4, 5]
print(c)  # [1, 2, 3, 4, 5] --> extend

# + operand shows different behaviour based on the datatypes its acting on
# this changing behaviour is called polymorphic behaviour

# len

aa = "Hello"  # string --> number of characters including spaces , and spcl chars
ab = (1, 2, 3,)  # tuple elements?
ac = {
    "a": "apple",
    "b": "bada apple",
    "c": "chup karo apple"
} # dict -- no of keys

x = [aa, ab, ac]
for item in x:
    # iteration1 --> item = aa
    # iteration2 --> item = ab
    print(len(item))  # Shreya -- 5, 7, 40+ || ~~~~2, 2, 2~~~~
                      # Palak -- 5, 3, 35+ || 5, 3, 3

print('#############################')
# polymorphic behaviour --> +, len, *

ma = 3 * 3 # multiply
mb = "T" * 3 # int time same string replica
md = [1, 2, 3] * 3 # extended the same list n number of time
for item in (ma, mb, md):
    print(item)

# Shreya -- 9, T3, pass/break/continue
# Palak -- 9, T3, [3, 6, 9]
# Sanjit -- pass

# packing
start_value, *mid, end_value = md
print("#"*30)
print(start_value)
print(end_value)
print(mid)

# packing --> *
# **

