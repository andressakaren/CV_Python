from datetime import date
def categoria(ano_nascimento):
    ano_atual = date.today().year  
    idade = ano_atual - ano_nascimento 
    if idade <= 9:
        print(f'O atleta tem {idade}. Classificação: MIRIM')
    elif idade <= 14:
        print(f'O atleta tem {idade}. Classificação: INFANTIL')
    elif idade <= 19:
        print(f'O atleta tem {idade}. Classificação: JUNIOR')
    elif idade <= 25:
        print(f'O atleta tem {idade}. Classificação: SÊNIOR')
    else:
        print(f'O atleta tem {idade}. Classificação: MASTER')
    
def main():
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    categoria(ano_nascimento)
    
if __name__ == "__main__":
    main()