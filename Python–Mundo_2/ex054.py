import datetime
def main():
    contMaior = 0
    contMenor = 0
    anoAtual = datetime.date.today().year
    
    for n in range(8):
        ano = int(input(f'Digite o ano de nascimento da {n+1}° pessoa: '))
        if (anoAtual - ano) >= 18:
            contMaior += 1
        else:
            contMenor += 1
            
    print(f'{contMenor} pessoas ainda não atingiram a maioridade.')
    print(f'{contMaior} pessoas já atingiram a maioridade.')         

if __name__ == '__main__':
    main()