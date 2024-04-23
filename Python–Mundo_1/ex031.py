def main():
    dist = float(input('Digite a distância da viagem, em Km: '))
    
    if dist <= 200:
        print(f'O preço da passagem custará: R$ {dist * 0.50:.2f}')
    else:
        print(f'O preço da passagem custará: R$ {dist * 0.45:.2f}')
        
if __name__ == '__main__':
    main()