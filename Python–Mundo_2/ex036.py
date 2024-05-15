def prestacao_mensal(valor_por_ano, salario_comprador):
    verificacao_salario = 0.3 * salario_comprador
    
    if valor_por_ano > verificacao_salario:
        print(f'Emprestimo Negado. A prestação será de R$ {valor_por_ano:.2f}')
    else:
        print(f'Emprestimo Concedido!! Valor da parcela por ano: R$ {valor_por_ano:.2f}')

def main():
    valor_casa = float(input('Digite o valor da casa: R$ '))
    salario_comprador = float(input('Digite o valor médio do salário: R$ '))
    qntd_anos_pagar = int(input('Digite em quantos anos pretende pagar a casa: '))

    valor_por_ano = valor_casa / (qntd_anos_pagar * 12)
    
    prestacao_mensal(valor_por_ano, salario_comprador)

if __name__ == "__main__":
    main()
