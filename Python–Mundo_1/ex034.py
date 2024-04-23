def main():
    salario = float(input('Digite o valor atual do seu salário: '))
    
    if salario > 1250:
        salario = salario + salario*0.1
        print(f'Você recebeu um aumento de 10% e o novo salário será: R$ {salario:.2f}!!')
    else:
        salario = salario + salario*0.15
        print(f'Você recebeu um aumento de 15% e o novo salário será: R$ {salario:.2f}!!')
        
if __name__ == "__main__":
    main()