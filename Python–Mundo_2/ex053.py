def main():
    frase = str(input('Digite uma frase que deseja verificar se é um Palíndromo: ')).strip().upper()
    
    # Substituir o espaço por uma string vazia
    fraseSem_espaco = frase.replace(' ', '')   
    fraseInversa = fraseSem_espaco[::-1]
    
    if fraseSem_espaco == fraseInversa:
        print(f'{fraseSem_espaco} e {fraseInversa} são iguais. É um políndromo.')
    else:
        print(f'{fraseSem_espaco} e {fraseInversa} NÃO são iguais. Não é um políndromo.')  
    
if __name__ == '__main__':
    main()