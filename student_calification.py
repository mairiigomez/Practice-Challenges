"""Give 3 notes of one student, all of them in the same line 
split() storage them in the appropriate variable 
*variable: can storage many values in a list 
Convert all the elements to float with the map function and storage to a list

storage to a super dictionary , with the name as a key and the score as values

Then ask for a student that they would like to note the score of"""

if __name__ == '__main__':
    n = int(input('Range for the function: '))
    #open a empty dictionary
    student_marks = {}
    for _ in range(n):

        # The first input goes to line and if there are more the 
        # get storage in line 
        name, *line = input('Give name a 3 scores: ').split()

        #map convert all the values in the variable line in float
        #this is save in a list
        scores = list(map(float, line))

        #Way to assing key and values to the dictionary
        #name are the keys and score the values 
        student_marks[name] = scores

    query_name = input("Query name: ")
    
    # Looking for the student in the dictionary
    if query_name in student_marks:

        namelookupfor = query_name
        #the key within [] looks for the value and store it in the variable
        scores_query = student_marks[namelookupfor]
        totalsq = sum(scores_query)
        percentage = totalsq/3
        #print the result with 2 decimals
        print('%.2f' %percentage)
    else:
        print('That student is not in this school')
        
        