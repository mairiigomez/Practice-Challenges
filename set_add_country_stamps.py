""" HACKERRANK
Using the s.add() method of set
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

*** sick solution
print(len({input() for x in range(int(input()))}))
"""
# Ask for the total amount of stamps she has
number_of_stamps = int(input("Enter number of stamps: "))

# create an empty set
set_stamps = set()

for i in range(number_of_stamps):
    # Ask for each stamp country
    stamp_country = input("Country Stamp: ")

    # Add each country to the set
    set_stamps.add(stamp_country)

# Lenght of the set repeated elements count like ONE
amount_countries = len(set_stamps)
print(amount_countries)