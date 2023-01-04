from colorama import Fore
import time
#Um projeto de caixa eletronico!! ainda em testes... (:

repetir = "sim"
l_dinheiro = []
l_nome = []


while repetir == "sim":
    nome = input(Fore.LIGHTCYAN_EX + "Digite o seu nome: " + Fore.RESET).capitalize()

    if nome in l_nome:
        repetir = "sim"
    else:
        l_nome.append(nome)

    l_dinheiro.append(float(input(Fore.LIGHTCYAN_EX + "DIgite aqui a quantia do dinheiro: "  + Fore.RESET)))

    repetir = input("Deseja repetir a operação?: 'sim' ou 'não': ").lower()
("\n")

print("Agora a interação...")
time.sleep(2)
resul = "sim"

while resul == "sim":
    saque = float(input("Digite a quantia do saque: "))
    nomme = input("Digite o seu nome: ").capitalize()

    for i in l_nome:
        if nomme == i:
            x = i

    idice = l_nome.index(x)
    y = l_dinheiro[idice]

    if saque > y:
        break
    else:
        print(f"O total final da sua conta é: {y - saque}")

    resul = input("Deseja repetir: 'sim' ou 'não': ").lower()
