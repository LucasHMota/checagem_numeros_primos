#LUCAS HENRIQUE MOTA

numero = int(input("Digite um número qualquer: "))
resposta = int(input("Escolha se você quer processo de força bruta (1), busca por ímpares (2) ou busca por ímpares até a metade do valor (3): "))
contador = 0
iteracoes = 0

#Teste por força bruta. Verifica todos os números até o valor digitado.
if resposta == 1:
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
        iteracoes += 1

    if contador == 2:
        print("\nResposta: O número {} é primo.".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))
    else:
        print("\nResposta: O número {} NÃO é primo!".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))

#Busca por ímpares. Aqui só será dividido pelos números ímpares e por 2.
#2 é primo e precisa ser incluído.
elif resposta == 2:
    for i in range(1, numero + 1):
        if i % 2 != 0 or i == 2:
            if numero % i == 0:
                contador += 1
            iteracoes += 1

    if contador == 2:
        print("\nResposta: O número {} é primo.".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))
    else:
        print("\nResposta: O número {} NÃO é primo!".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))

#Busca por ímpares até a metade do valor. Funciona como a anterior, mas é dividido o valor informado por 2 e a busca para quando chegar nele.
#Quando o programa se encerra, se o contador só tiver aumentado em 1 quer dizer que é primo.
elif resposta == 3:
    metade = int(numero / 2)
    for i in range(1, metade):
        if i % 2 != 0 or i == 2:
            if numero % i == 0:
                contador += 1
            iteracoes += 1

    if contador == 1:
        print("\nResposta: O número {} é primo.".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))
    else:
        print("\nResposta: O número {} NÃO é primo!".format(numero))
        print("A quantidade de iterações necessárias para verificar foram {}.".format(iteracoes))
