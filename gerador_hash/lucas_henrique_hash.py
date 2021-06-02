from time import sleep

def valor(x):
    alf = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        if x == alf[i]:
            return i
    return 0

def hash(text):
    tot = 0
    for i in range(len(text)):
        tot += valor(text[i])
    return str(tot % 1000).zfill(3)

if __name__ == '__main__':
    text = str(input("Digite um texto qualquer (no máximo 100 caracteres): "))
    print("\nGerando hash...")
    sleep(2)
    print("O hash para esse texto é: ", hash(text))