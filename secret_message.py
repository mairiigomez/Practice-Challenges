"""Create a program that replaces each letter in a message with its 
corresponding letter in a backwards version of the English alphabet

input Format: A string of your message in its normal form
output format: A string of your message once you have encoded it (lower case)

sample input: Hello World

sample output: svool dliow"""

def encode_message(message):
    """Encode the message by changing the letter for its reverse letter"""

    # To storage the reverse message
    reverse_message = ''
    alphabet = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',]

    # Convert the message to lower case to look for the letter in the alphabet
    message = message.lower()

    # replace the blank space, so there is no blank space to compare if is alpha 
    message_ = message.replace(" ","")
    
    # after taking away any blank spaces compare if is completely if not raise a valueError
    if str.isalpha(message_):

        # working with the original message lower case
        for letter in message: 
            
            # If it's not a blank space 
            if letter != ' ':
                           
                # look for the position of the letter 
                position_letter = alphabet.index(letter)
                
                # if position minor or equal to 12 letter is between a-m
                if position_letter <= 12: 
                    # the position of the rever letter equivalent is 
                    position_reverse_letter = (position_letter + 1)*(-1)
                    # look for that letter in the alphabet 
                    reverse_letter = alphabet[position_reverse_letter]

                # if position of the letter is greater or equal than 13 n-z
                if position_letter >= 13:
                    position_reverse_letter = (position_letter - 25)*(-1)
                    reverse_letter = alphabet[position_reverse_letter]

            # if is a blank space leave it like a blank space 
            else:
                reverse_letter = ' '
            
            # Add the reverse letter to the string with reverse message
            reverse_message += reverse_letter
        return reverse_message
    
    # Raise a value error if the message has something more than alphabetical characters
    else:
        raise ValueError('Your message has to be alphabetical')

def run():
    message = input('Enter your message: ')
    reverse_message = encode_message(message)
    print(reverse_message)

if __name__ == '__main__':
    run()
