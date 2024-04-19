dias = int(input('Quantidade de dias rodados: '))
km = float(input('Quilometragem rodada nesses dias: '))
total_dias = dias * 60
total_km = km * 0.15
total = total_dias + total_km
print(f'A quantidade a ser cobrada por usar {dias} dias e rodar {km} quilometros é R$ {total:.2f}.')
print(f'Em {dias} dias: R$ {total_dias:.2f}.')
print(f'Em {km}Km : R$ {total_km:.2f}.')
print(f'Total: R$ {total}.')
