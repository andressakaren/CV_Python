def main():
    a1 = int(input('Digite o primeiro termo da P.A.: '))
    r = int(input('Digite a razão da P.A.: '))
    an = a1 + (10 - 1) * r
    for num in range(a1, an + r, r):
        print(num)
    
if __name__ == "__main__":
    main()