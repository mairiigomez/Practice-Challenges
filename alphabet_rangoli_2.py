
alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ]

def print_rangoli(size):
    letters = alphabet[size-1::-1]
    # middle position of the figure 
    middle_figure = (size*2)-1
    full_size_row = (size*4)-3
    string_full_size = "-" * full_size_row
    rangoli = [string_full_size] * size

    position_array = 0
    
    for letter in letters:
        position_letter = 0
        print(position_array)
        for position in range(position_array, size):
            # Convert to a list so we can write in an specific index
            list_write_on = list(rangoli[position])
            list_write_on[(middle_figure-1) + position_letter] = letter
            list_write_on[(middle_figure-1) - position_letter] = letter

            # convert back to string to add it to rangoli
            new_string = "".join(list_write_on)
            rangoli[position] = new_string

            print(list_write_on)
            position_letter += 2
        position_array += 1

    if size != 1:
        for string in rangoli:
            print(string)

        for string_ in rangoli[size-2::-1]:
            print(string_)
    
    else: 
        for string in rangoli:
            print(string)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
