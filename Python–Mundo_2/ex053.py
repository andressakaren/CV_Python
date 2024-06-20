def main():
    frase = str(input('Digite uma frase que deseja verificar se é um Palíndromo: ')).strip()
    
    # Substituir o espaço por uma string vazia
    fraseSem_espaco = frase.replace(' ', '')
    
    indo = fraseSem_espaco[0:]
    voltando = fraseSem_espaco[::-1]
    
    if indo == voltando:
        print('É um políndromo.')
    else:
        print('Não é um políndromo.')  
    
if __name__ == '__main__':
    main()