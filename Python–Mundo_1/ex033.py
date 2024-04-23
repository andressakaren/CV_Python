def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    
    # Para n1 menor número:
    if n1 < n2 and n1 < n3:
        print(f'{n1} é o menor número.')
        if n2 < n3:
            print(f'{n3} é o maior número.')
        else:
            print(f'{n2} é o maior número.')
    
    # Para n2 menor número:
    if n2 < n1 and n2 < n3:
        print(f'{n2} é o menor número.')
        if n1 < n3:
            print(f'{n3} é o maior número.')
        else:
            print(f'{n1} é o maior número.')
    
    # Para n3 menor número:
    if n3 < n1 and n3 < n2:
        print(f'{n3} é o menor número.')
        if n1 < n2:
            print(f'{n2} é o maior número.')
        else:
            print(f'{n1} é o maior número.')
                       
if __name__ == "__main__":
    main()
    
    # Usando o método sort()
    
    # n1 = int(input('Digite um número: '))
    # n2 = int(input('Digite outro número: '))
    # n3 = int(input('Digite um último número: '))
    # l = [n1, n2, n3]
    # l.sort()
    # print(f'O maior número é {l[2]} e o menor é {l[0]}')
       