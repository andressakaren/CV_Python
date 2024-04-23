import random

def main():
    num_random = random.randrange(6) # randint(0,5)
    num_usuario = int(input('Digite um número inteiro entre 0 e 5: '))
    if num_random == num_usuario:
        print(f'O número escolhido pelo computador foi: {num_random}. Você acertou!!')
    else:
        print(f'O número escolhido pelo computador foi: {num_random}. Você NÃO acertou!!')

if __name__ == '__main__':
    main()