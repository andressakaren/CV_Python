def main():
    soma = 0
    cont = 0
    for i in range(1,7):
        valor = int(input(f'Digite o {i}° número: '))
        if valor % 2 == 0:
            soma += valor
            cont += 1
    print(f'Você digitou {cont} números pares. A soma dos valores pares digitados é: {soma}.')

if __name__ == "__main__":
    main()