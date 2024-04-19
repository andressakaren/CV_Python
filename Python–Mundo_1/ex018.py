import math

angulo = float(input('Digite um valor de ângulo qualquer: '))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Para o angulo {angulo}, o cosseno é {cosseno:.2f}, o seno é {seno:.2f} e a tangente é {tangente:.2f}.')