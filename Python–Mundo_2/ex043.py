def imc(p, a):
    formula_imc = p / ( a * a)
    if formula_imc < 18.5:
        print(f'Seu IMC é {formula_imc:.1f}. STATUS: Abaixo do Peso.')
    elif 18.5 <= formula_imc <= 25:
        print(f'Seu IMC é {formula_imc:.1f}. STATUS: Peso ideal.')
    elif 25 <= formula_imc < 30:
        print(f'Seu IMC é {formula_imc:.1f}. STATUS: Sobrepeso.')
    elif 30 <= formula_imc < 40:
        print(f'Seu IMC é {formula_imc:.1f}. STATUS: Obesidade.')
    elif formula_imc >= 40:
        print(f'Seu IMC é {formula_imc:.1f}. STATUS: Obesidade mórbida.')

def main():
    peso = float(input('Qual seu peso: '))
    altura = float(input('Qual sua altura: '))
    imc(peso, altura)
    
if __name__ == "__main__":
    main()