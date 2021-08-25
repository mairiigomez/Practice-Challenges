def run():
    # Skip print the number if is not divisible y 2 
    # go back to the star of the for loop 
    for contador in range(100):
        if contador % 2 != 0:
            continue
        print(contador)

    # Break the for loop when i == 56
    for i in range(100):
        print(i)
        if i == 56:
            break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
