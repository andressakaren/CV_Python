def main():
    
    vel = float(input('Digite a velocidade atual do seu carro, em Km/h: '))
     
    if vel > 80.00: 
        multa = (vel - 80) * 7
        print(f'Você foi multado. E deve pagar R$ {multa:.2f}.')

    print(f'Tenha um ótimo dia, dirija com cuidado!!')
    
if __name__ == '__main__':
    main()