"""You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)"""

def print_rangoli(size):
    alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ]
    rangoli = ''
    for i in range(size):
        #print(((size*2)-2)*'-' + alphabet[size-i] + ((size*2)-2)*'-')
        letter = str(alphabet[size-i-1])
        sequence = (letter.center((size*4)-3,'-'))+('\n')
        rangoli += sequence
    
    
    print(rangoli)
    print(len(rangoli))
    print(type(rangoli))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)