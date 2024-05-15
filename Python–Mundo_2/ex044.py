def opcao_pagamento(preco_compra, forma_pagamento):
    if forma_pagamento == '1':
        a_vista_dinheiro = preco_compra - (0.1 * preco_compra)
        print(f'À vista no dinheiro/cheque tem 10% de desconto. O valor final é de R$ {a_vista_dinheiro:.2f}')
    elif forma_pagamento == '2':
        a_vista_cartao = preco_compra - (0.05 * preco_compra)  
        print(f'À vista no cartão tem 5% de desconto. O valor final é de R$ {a_vista_cartao:.2f}') 
    elif forma_pagamento == '3':
        duas_vezes = preco_compra/2
        print(f'Parcelando 2x no cartão o valor total é R$ {preco_compra} com duas parcelas de R$ {duas_vezes:.2f}')
    elif forma_pagamento == '4':
        qntd_vezes = input('Deseja parcelar em quantas vezes? ')
        tres_mais_vezes = preco_compra + (0.2 * preco_compra)
        parcela = tres_mais_vezes / int(qntd_vezes)
        print(f'Parcelando 3x ou mais no cartão, tem juros de 20%. O valor total é R$ {tres_mais_vezes:.2f} com {qntd_vezes} parcelas de R$ {parcela:.2f}')
    else:
        print('Opção inválida!!')
def main():
    preco_compra = float(input('Digite o preço do produto: R$ '))
    forma_pagamento = input('''Digite a opção de pagamento: 
[1] - à vista dinheiro/cheque
[2] - à vista cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
''')
    opcao_pagamento(preco_compra, forma_pagamento)
  
if __name__ == "__main__":
    main()