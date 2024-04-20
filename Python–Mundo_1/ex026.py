def main():
    # Entrada de dados:
    frase = str(input('Digite uma frase: ')).lower().strip()
    
    # Processamento:
    letra_a = frase.count('a')
    primeira_a = frase.find('a')
    ultimo_a = frase.rfind('a')
           
    # Saída de dados:
    print(f'A letra \'A\' aparece: {letra_a} vezes.')
    print(f'A posição da primeira letra \'A\' é: {primeira_a + 1}°')
    print(f'A posição da última letra \'A\' é: {ultimo_a + 1}°')

if __name__ == '__main__':
    main()