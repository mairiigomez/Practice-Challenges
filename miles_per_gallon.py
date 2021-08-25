"""Prompt the user for gallons used for each tankful and 
miles driven and calculate and display miles/gallon for 
each tankful and also calculate for all tankful, exit the 
program entering -1 """

total_miles = 0
total_gallons = 0 

while True:

    miles_driven = input('Enter total miles driven (-1 to end): ')
    if miles_driven == '-1':
        break
    gallons_per_tankfull = input('Enter total of gallons used (-1 to end): ')
    if gallons_per_tankfull == '-1':
        break

    miles_per_gallon = float(miles_driven)/float(gallons_per_tankfull) 
    print(f"The miles per gallon for this tank was: {miles_per_gallon}\n")

    # Add the information enter to the variables to calculate the average
    # after exciting the program
    total_miles += float(miles_driven)
    total_gallons += float(gallons_per_tankfull)

try:
    total_miles_per_gallon = total_miles/total_gallons
    print(f"\nThe total miles per gallon was: {total_miles_per_gallon}")
except ZeroDivisionError:
    print('No enough data to calculate total miles per gallon')

