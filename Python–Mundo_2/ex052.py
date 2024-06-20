def main():
    numDigitado = int(input('Digite um número inteiro: '))
    cont = 0
    for num in range(1, numDigitado + 1):
        divisao = numDigitado % num
        if divisao == 0:
            cont += 1
    if cont == 2:
        print('É primo')
    else:
        print('Não é primo')
if __name__ == "__main__":
    main()