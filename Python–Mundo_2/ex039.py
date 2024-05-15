from datetime import date

def se_alistar(ano_nascimento):
    ano_atual = date.today().year
    idade_verificar = ano_atual - ano_nascimento
    if idade_verificar == 18:
        print(f'Você tem {idade_verificar} anos. Já é hora de se alistar.')
    elif idade_verificar < 18:
        print(f'Você tem {idade_verificar} anos. Ainda faltam {18 - idade_verificar} anos. Seu alistamento será em {ano_atual + (18 - idade_verificar)}')
    else:
        print(f'Você tem {idade_verificar} anos. Já deveria ter se alistado há {idade_verificar - 18} anos. O ano do seu alistamento foi em {ano_atual - (idade_verificar - 18)}!!')
    
def main():
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    se_alistar(ano_nascimento)
    
if __name__ == "__main__":
    main()