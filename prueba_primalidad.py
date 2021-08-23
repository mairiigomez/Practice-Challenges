"""Determine if a number is prime or not, a number is prime when is divisible
only by 1 and itself"""

def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        # if i is 1 or the number continue skip
        # do not do the division because is going to be divisible 
        # we need to verify with the other numbers
        if i == 1 or i == numero:
            continue

        # if the number is divide by any of the interactions (numbers)
        # and its module is 0 count 1 
        if numero % i == 0:
            contador += 1
    # if contador is 0 is because the number is not divisible for any number
    # but 1 and itself (so it is a prime number)
    if contador == 0:
        return True
    # if contador es diferent from 0 so no es primo
    else:
        return False


def run():
    numero = int(input('Escribe un número: '))
    # if the function returns True show es primo if not no es primo
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
