nome = str(input('Qual seu nome? '))
m = float(input('Digite uma distância em metro: '))

km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'Olá, {nome}!')
print(f'O valor {m} em metros equivale a: {km} km  | {hm} hm | {dam:.1f} dam | {m} m | {dm} dm | {cm} cm | {mm} mm |')
