def main():
    # Entrada de dados:
    nome_cidade = str(input('Digite o nome da cidade: ')).title().strip()

    # Processamento:
    primeiro_nome = nome_cidade[:5].upper()
        
    # Saída de dados: 
    print(f'A cidade {nome_cidade} começa com o nome \'Santo\' ?\nResposta: {primeiro_nome == 'SANTO'}!!')

if __name__ == '__main__':
    main()