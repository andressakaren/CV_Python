def comparacao(num1, num2):
    if num1 > num2:
        print(f'O PRIMEIRO valor é maior.')
    elif num1 < num2:
        print(f'O SEGUNDO valor é maior.')
    else: 
        print(f'Os dois números são IGUAIS.')

def main():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    
    comparacao(num1, num2)    

if __name__ == "__main__":
    main()