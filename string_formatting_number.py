"""" 
134567 when the number < 7 10 11 12 13 

octal if the number is < than 7 is the same number
hexadecimal if the number is < that 9 is the same number


"""

def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))

    for i in range(1, number+1):
        b = bin(int(i)).replace('0b','').rjust(w, ' ')
        o = oct(int(i)).replace('0o','').rjust(w, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print(j, o, h, b)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)