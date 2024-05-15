def condicoes(media):
    if media < 5:
        print(f'Sua média é {media:.1f}. Você está REPROVADO!')
    elif media >= 5 and media < 7:
        print(f'Sua média é {media:.1f}. Você está de RECUPERAÇÃO!')
    elif media >= 7:
        print(f'Sua média é {media:.1f}. Você está APROVADO!')

def main():
    nota1 = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))

    media = (nota1 + nota2) / 2
    condicoes(media)
    
if __name__ == "__main__":
    main()