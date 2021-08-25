"""Look for a substring within a string My solution"""

def run():
    string = input('Enter a string: ').strip()
    sub_string = input('String to look for: ').strip()
    count = count_substring(string, sub_string)
    print(count)

def count_substring(string, sub_string):
    times_found = 0
    for i in range(len(string)):
        if string[i : i+len(sub_string)] == sub_string:
            times_found += 1 
    return times_found
    
if __name__ == '__main__':
    run()