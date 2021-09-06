"""" 
134567 when the number < 7 10 11 12 13 

octal if the number is < than 7 is the same number
hexadecimal if the number is < that 9 is the same number


"""

dict_octal = {8:10, 9:11, 10:12, 11:13, 12:14, 13:15, 14:16, 15:17, 16:20, 17:21}
dict_hexa = {8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'1F', 17:'2F'}
dict_binary = {1:1, 2:10, 3:11, 4:100, 5:101, 6:110, 7:111, 8:1000, 9:1001, 10:1010, 11:1011, 12:1100, 13:1101, 14:1110, 15:1111, 16:10000, 17:10001}

def print_formatted(number):
    for i in range(1, number+1):
        if i <= 7:
            i_ = str(i)
            binary_number = dict_binary.get(i)
            b_ = str(binary_number)
            print(i_.rjust(4), i_.rjust(4), i_.rjust(4), b_.rjust(5))
        else:
            i_ = str(i)
            octal_number = dict_octal.get(i)
            hexa_number = dict_hexa.get(i)
            binary_number = dict_binary.get(i)
            
            print(i_.rjust(4), str(octal_number).rjust(4), str(hexa_number).rjust(4), str(binary_number).rjust(5))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)