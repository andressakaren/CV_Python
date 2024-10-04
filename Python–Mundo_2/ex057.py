def main():
    c = ''
    while c != 'F' and c != 'M': 
        c = str(input('Digite qual o seu sexo [F - Feminino] ou [M - Masculino]: ')).upper()
        if c != 'F' and c != 'M':
            c = str(input('Dados inválidos. Digite apenas umas das opções [F - Feminino] ou [M - Masculino]: ')).upper()
    
    
    if c == 'M':    
        print(f'O seu sexo escolhido foi Masculino. Registrado com sucesso!!!')
    else:
        print(f'O sexo escolhido foi Feminino! Registrado com sucesso!!!')

if __name__ == '__main__':
    main()