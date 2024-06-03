import time
   
def main():
    for count in range(10,-1,-1):
        time.sleep(1)
        print(count)
    time.sleep(1)
    print("FELIZ ANO NOVO!!! 🎆🎇")

if __name__ == "__main__":
    main()