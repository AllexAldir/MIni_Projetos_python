# from colorama import Fore
import time


def cau(operacao):
    if operacao == "x":
        x = num1 * num2
        return x

    if operacao == "/":
        x = num1 / num2
        return x

    if operacao == "+":
        x = num1 + num2
        return x

    if operacao == "-":
        x = num1 - num2
        return x


l_sinais = ["-", "+", "/", "x"]
repetir = 'sim'

while repetir == 'sim':
    operacao = input("Qual operação você deseja fazer? +,-,/,x: ").lower()

    while operacao not in l_sinais:
        operacao = input("Tente novamente não foi possivel identificar esses sinais: ").lower()

    time.sleep(2)

    num1 = float(input("Digite um número: "))

    p = input("Deseja adicionar mais um número a operação? 'sim' ou 'não': ").lower()

    if p == "sim":
        num2 = float(input("Digite o segundo número aqui: "))

    result = cau(operacao)

    print(f"Resultado da operação é: {result}")

    repetir = input("Deseja realizar uma outra operação ? 'sim' ou 'não': ").lower()