import random
from time import sleep
def jogo(a,b):
    if b == 1:
        print(f'O computador escolheu: PAPEL')
        if a == 1:
            print('Você escolheu PAPEL')
            print('-='*15)
            print('Resultado: EMPATE')
        elif a == 2:
            print('Você escolheu PEDRA')
            print('-='*15)
            print('Resultado: Computador venceu')
        elif a == 3:
            print('Você escolheu TESOURA')
            print('-='*15)
            print('Resultado: Você VENCEU!!!')
            
    elif b == 2:
        print(f'O computador escolheu: PEDRA')
        if a == 1:
            print('Você escolheu PAPEL')
            print('-='*15)
            print('Resultado: Você VENCEU!!!')
        elif a == 2:
            print('Você escolheu PEDRA')
            print('-='*15)
            print('Resultado: EMPATE')
        elif a == 3:
            print('Você escolheu TESOURA')
            print('-='*15)
            print('Resultado: Computador venceu')
            
    elif b == 3:
        print(f'O computador escolheu: TESOURA')
        if a == 1:
            print('Você escolheu PAPEL')
            print('-='*15)
            print('Resultado: Computador venceu')
        elif a == 2:
            print('Você escolheu PEDRA')
            print('-='*15)
            print('Resultado: Você VENCEU!!!')
        elif a == 3:
            print('Você escolheu TESOURA')
            print('-='*15)
            print('Resultado: EMPATE')

def main():
    opcao_usuario = int(input('''Escolha entre:
[1] - PAPEL
[2] - PEDRA
[3] - TESOURA
Qual sua opção: '''))
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    sleep(0.5)
    print('-='*15)
    opcao_computador = random.randint(1,3)   
    jogo(opcao_usuario, opcao_computador)

if __name__ == "__main__":
    main()