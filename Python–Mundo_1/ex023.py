def main():
    # Entrada de dados
    num = int(input('Digite um número entre 0 e 9999: '))
    
    # Processamento 
    unidade = num % 10
    num //= 10
    dezena = num % 10
    num //= 10
    centena = num % 10
    num //= 10
    milhar = num % 10
                
    # Saída de dados
    print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')    
        
if __name__ == '__main__':
    main()