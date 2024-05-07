# Identifiers

An identifier is a name used to identify a variable, function, class, module, or any other object.

In simple terms the name assigned to any programmable entity is called an Identifier.

## Rules for naming identifiers:
- It can contain letters (both uppercase and lowercase), digit and underscore(_)
```python
# good identifier
>>> bahubali_actor = "Prabhas"

# this is also good identifier
>>> bahubali2 = "Blockbuster"
```
- It can't start with numbers.
```python
# this won't work
>>> 21_century = "Gen Z"
```
- It is case-sensitive.
```python
# hello and Hello are not same
```
- Certain reserved words (keywords) cannot be used as identifiers because they have special meanings in Python
```python
# if, else , type, print etc. can't be used as identifiers.
```
- To verify if a given string can be used as an identifier or not we can use "isidentifier()"
```python
# valid identifier
>>> bahubali_actor = "Prabhas"
>>> "bahubali_actor".isidentifier()
True

# invalid identifier
>>> "21_century".isidentifier()
False
```

## Conventions for naming Identifiers:
Python follows the PEP8 style guide for naming conventions.
- Variables, functions, and methods should be named in lowercase, with words separated by underscores (snake_case)
- Constants should be named in uppercase, with words separated by underscores (UPPER_CASE)
- Class names should follow the CapWords convention, also known as CamelCase, where the first letter of each word is capitalized
```python
# -- examples --
# variables: 'my_variable', 'total_amount'
# constants: 'CAPITAL_OF_STATE', 'HUMBLENESS'
# function/method names: 'calculate_area', 'get_user_input'
# class names: 'Employee', 'PersonWithSuperPowers'
# module names: 'math', 'day1', 'mark'
```

