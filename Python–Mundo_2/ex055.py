def main():
    maior = 0
    menor = 0
    for n in range(1, 6):
        peso = float(input(f'Digite o {n}° peso, em Kg: '))
        if n == 1:
            maior = peso
            menor = peso
        else:           
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
        
    print(f'O maior peso foi {maior:.2f} Kg')
    print(f'O maior peso foi {menor:.2f} Kg')
    
if __name__ == '__main__':
    main()