def main():
    count = 0
    soma = 0
    for numImpar in range(1, 501, 2):
        if numImpar % 3 == 0:
            count += 1
            soma += numImpar
    print(f'Temos {count} números ímpares divisíveis por 3, entre 1 e 500.')
    print(f'A soma entre todos eles é: {soma}.')

if __name__ == "__main__":
    main()