def eh_triangulo(l1, l2, l3):
    if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
        print(f'Os três segmentos de retas formam um triângulo!!')
        # Tipo de triângulo 
        if l1 == l2 and l2 == l3:
            print('O triângulo é EQUILÁTERO (Todos os lados iguais).')
        elif l1 != l2 and l1 != l3 and l3 != l3:
            print('O triângulo é ESCALENO (Todos os lados diferentes).')
        else:
            print('O triângulo é ISÓSCELES (Dois lados iguais e um diferente.)')   
    else:
        print(f'Os três segmentos de reta NÃO formam um triângulo!!')       

def main():
    # A soma de dois lados é sempre maior que o terceiro lado   
    l1 = int(input('Digite o valor do lado 1: '))    
    l2 = int(input('Digite o valor do lado 2: '))    
    l3 = int(input('Digite o valor do lado 3: '))   
    
    eh_triangulo(l1, l2, l3)

if __name__ == "__main__":
    main()