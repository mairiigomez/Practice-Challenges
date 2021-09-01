"""A palindrome is a number or a text phrase that reads the same backwards or forwards. For
example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611.
Write a program that reads in a five-digit integer and determines whether it is a palindrome. (Hint:
Use the division and modulus operators to separate the number into its individual digits.)"""

palindromo = ''
number = int(input('Enter a number: '))

# When we get the module 10 of a number we obtain the last digit
module = number % 10
# We convert the number to string to add it to palindromo
palindromo += str(module)
# we divide by 2 to remove the last digit that is going to be as a float
division = int(number/10)

module = division%10 
palindromo += str(module)
division = int(division/10)

module = division%10 
palindromo += str(module)
division = int(division/10)

module = division%10 
palindromo += str(module)
division = int(division/10)

module = division%10 
palindromo += str(module)
division = int(division/10)

if str(number) == palindromo:
    print("It is palindrome")
else:
    print("It is not palindrome")