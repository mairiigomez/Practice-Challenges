"""Determine if a word is Palidrom or not """

def palindromo(palabra):
    """Function to check if its palindrome receive word return True or False"""
    # Delete blank spaces and converted to lowercase
    palabra = palabra.strip().lower()
    # Invert the word 
    palabraalreves = palabra[::-1]
    if palabraalreves == palabra:
        return True
    else: 
        return False

def run():
    """Main function"""
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else: 
        print("No es palindromo")

if __name__ == '__main__':
    run()

