def convercao(num):
    escolha = int(input('Digite a base que deseja converter: [1] - Binário, [2] - Octal, [3] - Hexagonal: '))
    if escolha == 1:
        num_bin = bin(num)[2:]
        print(f'O número {num} em binário é {num_bin}')
    elif escolha == 2:
        num_oct = (oct(num))[2:]
        print(f'O número {num} em octal é {num_oct}')
    elif escolha == 3:
        num_hex = hex(num)[2:]
        print(f'O número {num} em hexadecimal é {num_hex}') 
    else:
        print('Opção inválida!!')   

def main():
    num = int(input('Digite um número inteiro: '))
    convercao(num)
    
if __name__ == "__main__":
    main()