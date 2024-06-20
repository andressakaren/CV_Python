def main():
    contMaior20 = 0
    nomeMaisvelho = ''
    maiorIdade = 0
    somaIdades = 0
    for n in range(1, 5):
        print(f'____________________{n}° PESSOA____________________')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [F] - Feminino OU [M] - Masculino: ')).strip().upper()
        somaIdades += idade
        if sexo == 'M':
            if n == 1:
                maiorIdade = idade
                nomeMaisvelho = nome
            else:
                if idade > maiorIdade:
                    maiorIdade = idade
                    nomeMaisvelho = nome      
        if sexo == 'F':
            if idade < 20:
                contMaior20 += 1
        
    print(f'A média das idades é: {somaIdades/4:.2f} anos')
    print(f'O homem mais velho é: {nomeMaisvelho} e tem {maiorIdade} anos')
    print(f'Temos {contMaior20} mulheres com menos de 20 anos.')
    
if __name__ == '__main__':
    main()