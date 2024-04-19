larg = float(input('Qual a largura da parede, em metros? '))
alt = float(input('Qual a altura da parede, em metros? '))
area = larg * alt
litro = (area * 1)/2
print(f'A área da parede é {area}.')
print(f'Cada litro de tinta pinta uma área de 2m², logo para pintar {area:.2f}, será necessário {litro:.2f} litros.')
