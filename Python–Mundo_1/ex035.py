def main():
    # A soma de dois lados é sempre menor que o terceiro lado
    
    l1 = int(input('Digite o valor do lado 1: '))    
    l2 = int(input('Digite o valor do lado 2: '))    
    l3 = int(input('Digite o valor do lado 3: '))   
           
    if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
        print(f'Os três segmentos de retas formam um triângulo!!')
    else:
        print(f'Os três segmentos de reta NÃO formam um triângulo!!')
            
if __name__ == "__main__":
    main()