def calculadora(valor):
    for num in range(1, 11):
        print(f'{valor} * {num:2} = {num * valor}')

def main():
    valor = int(input('Digite um valor: '))
    calculadora(valor)
    
if __name__ == "__main__":
    main()