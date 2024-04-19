from math import hypot

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)


print(f'A hipotenusa do triangulo vai medir: {hipotenusa:.2f}')
