"""
collection datatype:
--------------------
undefined-ordered-heterogenous ==> list
unordered-unique-(hashable) ==> set
ordered-undefined-fixed in size
order - key-value pair



LIST
1. to add data
    - append --> last me
    - insert --> given index
    - extend --> adds the individual elements of iterable
2. to remove data
    - pop --> last element removed and returns
    - remove --> removes the elements
    - clear --> makes the list empty

SET
1. to add data
    - add --> randomly adds data
    - update --> add set into set (un-hashable)
    - union --> creates a copy and provides aUb

2. modify a set
    - symmetric_update
    - difference_update

2. to remove data
    - pop --> random removal and returns
    - remove(key) --> given value if value not present KeyError
    - discard(key) --> given value if value not present No error is thrown
    - clear --> return empty set

TUPLE
1. count
2. index


mutable --> objects that can be modified/or can change themselves are mutable example list/set/dict
immutable --> tuple/string/int/float/complex/boolean

tuple

DRY :: Don't Repeat Yourself

word1 -- I dont the meaning ?? -- dictionary meanings
word1 -- meaning1
word2 -- meaning1/2

dictionary
dict

In order to store data in terms of key-value pair.
a = create_dict() # something that gives me dictionary
a[key] = value at key in dict a

a = {key:value, key1:value1, key2:value2}

value1
a[key1]

value2
a[key2]

[]
{}
()

- get ==> returns the value of key passed
- items ==> returns key, value pairs in form of tuple
- keys ==> returns list of keys in the dict
- values ==> returns list of values in the dict
- pop ==> removes the key from the dict and returns the value
- popitem ==> removes the last added item and returns tuple of (key, value)
- setdefault ==> when key is known but value is unknown || sets the value as None
- update ==> dict in dict
- fromkeys ==> creates a new dictionary from iterable elements as key and given value as value

Question 1

sample_dict = {"flowers":["Rose","lily","lotus"],"animals" : ["cat","dog"]}
add "sunflower" to the flowers list and "lion" to the animal list.

Question 2
needed_keys = ["a","b","c","d"]
Create a dictionary with "no value" as value for all the keys.


Question 3
a. points = {'a':1, 'b':2, 'c':3}
    increment the value of b to 3

b. points = {'a':1,'b':2,'c':3}
    add one more key as 'd' with value 4

    [], update, setdefault

    dict[]
    dict.something()
    dict --> {}

"""
capitals = {
    'Gujarat': 'GandhiNagar',
    'Karnataka': 'Bangalore',
    'Punjab': 'Chandigarh',
    'Canada': 'Ottawa',
    'Australia': 'Canberra'
}

# new_added = ('MP', 'UP', 'Rajasthan', 'Bihar')
# value = [1, 2, 3, 4]
# new_dict = {}.fromkeys(new_added, value)
# print(new_dict)

sample_dict = {
    "flowers": ["Rose", "lily", "lotus"],  # key is string and value is list of strings
    "animals": ["cat", "dog"]
}

# sample_dict['flowers']  # list
sample_dict['flowers'].append('sunflower')
sample_dict['animals'].append('lion')
print(sample_dict)

# value change --> list k operation
# value k individual element ko change --> string

# change all the flower names to lower case
# dict --> flowers ==> values --> list of strings ==> each element of list and convert the case
# a = [[1, 3], [1, 2, 3]] # list of list
