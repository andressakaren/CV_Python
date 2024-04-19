def main():
    #Entrada de dados
    nome = input("Digite seu nome completo: ").strip()
    
    # Processamento
    maisc = nome.upper()
    minusc = nome.lower()
    qntd_total = len(nome) - nome.count(' ')
    primeiro_nome = nome.split()
    primeiro_nome = len(primeiro_nome[0])
     
    # Saída de dados
    print(f'O seu nome completo com todas letras maiúsculas é: {maisc}!!')
    print(f'O seu nome completo com todas letras minúsculas é: {minusc}!!')
    print(f'O seu nome completo tem: {qntd_total} letras!!')
    print(f'O seu primeiro nome tem {primeiro_nome} letras!!')

if __name__ == '__main__':
    main()