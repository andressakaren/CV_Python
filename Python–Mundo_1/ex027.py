def main():
    # Entrada de dados: 
    nome_completo = str(input('Digite seu nome completo: ')).strip()

    # Processamento: 
    nome = nome_completo.split()    
    
    # Saída de dados:
    print(f'O seu primeiro nome é: {nome[0].title()}.')
    print(f'O seu último nome é: {nome[-1].title()}.')
    
if __name__ == '__main__':
    main()