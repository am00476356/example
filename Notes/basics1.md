# Basics of Python - Part 1

## Comments

Inline comment:

```python
# This is a comment
```

Multiline comment:

```python
# This is a
# multiline comment
```

Code with a comment:

```python
a = 1  # initialization
```

Please note the two spaces in front of the comment.

Function docstring:

```python
def foo():
    """
    This is a function docstring
    You can also use:
    ''' Function Docstring '''
    """
```

## The print() Function

The `print()` function writes the value of the argument(s) it is given.<br>It handles multiple arguments, floating point-quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely:

```python
>>> print('Hello world!')
# Hello world!

>>> a = 1
>>> print('Hello world!', a)
# Hello world! 1
```

### The end keyword

The keyword argument `end` can be used to avoid the newline after the output, or end the output with a different string:

```python
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
>>> for word in phrase:
...     print(word, end='-')
...
# printed-with-a-dash-in-between-
```

### The sep keyword

The keyword `sep` specify how to separate the objects, if there is more than one:

```python
print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice
```

## The input() Function

This function takes the input from the user and converts it into a string:

```python
>>> print('What is your name?')   # ask for their name
>>> my_name = input()
>>> print('Hi, {}'.format(my_name))
# What is your name?
# Martha
# Hi, Martha
```

`input()` can also set a default message without using `print()`:

```python
>>> my_name = input('What is your name? ')  # default message
>>> print('Hi, {}'.format(my_name))
# What is your name? Martha
# Hi, Martha
```


## Data Types

| Data Type              | Examples                                  |
|------------------------|-------------------------------------------|
| Integers               | `-2, -1, 0, 1, 2, 3, 4, 5`                |
| Floating-point numbers | `-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25` |
| Strings                | `'a', 'aa', 'aaa', 'Hello!', '11 cats'`   |
| Complex Numbers        | `2+3j, 1+5j, 0j, 0+0j, 2+3J`              |


## Math Operators

From **Highest** to **Lowest** precedence:

| Operators | Operation         | Example         |
|-----------|-------------------|-----------------|
| \*\*      | Exponent          | `2 ** 3 = 8`    |
| %         | Modulus/Remainder | `22 % 8 = 6`    |
| //        | Integer division  | `22 // 8 = 2`   |
| /         | Division          | `22 / 8 = 2.75` |
| \*        | Multiplication    | `3 * 3 = 9`     |
| -         | Subtraction       | `5 - 2 = 3`     |
| +         | Addition          | `2 + 2 = 4`     |

Examples of expressions:

```python
>>> 2 + 3 * 6
# 20

>>> (2 + 3) * 6
# 30

>>> 2 ** 8
#256

>>> 23 // 7
# 3

>>> 23 % 7
# 2

>>> (5 - 1) * ((7 + 1) / (3 - 1))
# 16.0
```
## Augmented Assignment Operators

| Operator   | Equivalent      |
|------------|-----------------|
| `var += 1` | `var = var + 1` |
| `var -= 1` | `var = var - 1` |
| `var *= 1` | `var = var * 1` |
| `var /= 1` | `var = var / 1` |
| `var %= 1` | `var = var % 1` |

Examples:

```python
>>> greeting = 'Hello'
>>> greeting += ' world!'
>>> greeting
# 'Hello world!'

>>> number = 1
>>> number += 1
>>> number
# 2

>>> my_list = ['item']
>>> my_list *= 3
>>> my_list
# ['item', 'item', 'item']
```