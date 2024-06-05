def main():
    soma = 0
    for i in range(1,7):
        valor = int(input('Digite um número: '))
        if valor % 2 == 0:
            soma += valor
            continue
    print(f'A soma dos valores pares digitados é: {soma}.')

if __name__ == "__main__":
    main()