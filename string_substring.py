"""
Given a String verify how many time a substring is found in the string

Part 0. While substring is within the string 
Part 1. Find the index where the sustring was found
Part 2. Take out that index by slicing the string:
        From the beginning until is found **remember that 
        the last one is not taken and the from where is found 
        plus 1 until the end
"""

string, sub = input(), input()
count = 0

# Part 0
while sub in string:
    # Part 1 
    i = string.find(sub)
    print(i)
    # Part 2
    string = string[:i] + string[i + 1:]
    print(string)
    count += 1

print('Times that is found: ',count)