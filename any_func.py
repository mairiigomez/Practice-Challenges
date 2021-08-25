"""To check what kind of string is the one that an user enter
If it's all numeric, or alphabetic, or if in lower casa, or upper"""

str = input('enter: ')

# If any of the items in the string 
# meets the stament it returns True
print(any(c.isalnum()  for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))