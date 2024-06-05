# INCOMPLETA

def pa(a1, r, qtd_termos):
    an = a1 + (qtd_termos - 1) * r
    return an

def main():
    a1 = int(input('Digite o primeiro termo da P.A.: '))
    r = int(input('Digite a razão da P.A.: '))
    an = pa(a1, r, qtd_termos=10)
    print(an)
    
    for i in range(a1, an+1):
        print(i, end=' ')
if __name__ == "__main__":
    main()