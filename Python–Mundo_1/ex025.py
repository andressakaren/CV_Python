def main():
   
    nome = str(input('Digite seu nome: ')).strip()
    
    print(f'Tem \'Silva\' no {nome}?\nResposta: {'silva' in nome.lower()}!!')

if __name__ == '__main__':
    main()