"""Enter an user and the score that the user got
the program prints the user with the second lowest score

0. We choose  the amount of people-score we want to enter
1. We store them as a list inside a list
2. We are the score to the the tuple set
3. We organize them from the lowest to the highest and pick
   the second lowest
4. Loop over the superlist and if the score is like the second lowest
    append the namme to second lowest names
5. Organize the names by alphabetical and print them
"""

l = []
second_lowest_names = []
scores = set()

# Part 0
for _ in range(int(input('Range: '))):
    name = input('Enter name: ')
    score = float(input('Enter the score: '))
    # Part 1
    l.append([name, score])
    # Part 2
    scores.add(score)

# Part 3    
second_lowest = sorted(scores)[1]

# Part 4
for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

# Part 5
for name in sorted(second_lowest_names):
    print(name, end='\n')
    