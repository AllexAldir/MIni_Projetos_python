# O usuário insere o limite inferior e o limite superior do intervalo.
# O compilador gera um inteiro aleatório entre o intervalo e o armazena em uma variável para referências futuras.
# Para adivinhação repetitiva, um loop while será inicializado.
# Se o usuário adivinhou um número maior do que um número selecionado aleatoriamente, o usuário obtém uma saída “ Tente novamente! Você adivinhou muito alto “
# Caso contrário, se o usuário adivinhou um número menor do que um número selecionado aleatoriamente, o usuário obtém uma saída “ Tente novamente! Você adivinhou muito pequeno ”
# E se o usuário adivinhou um número mínimo de adivinhações, o usuário recebe um “ Parabéns! " Resultado.
# Do contrário, se o usuário não adivinhou o número inteiro no número mínimo de adivinhações, ele receberá “ Melhor sorte na próxima vez! " resultado.
import random
from colorama import Fore
import time

input(Fore.CYAN + """
    Jogo da adivinhação irá começar!
    regras:
    -números de tentativas: 10
    -você escolherá dois números... o primeiro será o inicio e o segundo
    o ponto final. Exemplo: (numero1: 4, numero2: 15) no intervalo de tempo
    entre 4 a 15 o sistema irá escolher um número o qual você terá que adivinhar
    qual o número o sistema escolheu!
    preparado? Aperte ENTER para começar: 
""")
print("Aguarde...")
time.sleep(2)
x = 0


def ctz(number_user):
    global x
    if number_user == escolha:
        y = "Parabéns você acertou!"
        return y

    if number_user > escolha:
        y = "Você adivinhou muito alto"
        return y

    if number_user < escolha:
        y = "Você adivinhou muito baixo"
        return y


num1 = int(input("Digite um número: "))

while True:
    num2 = int(input("Digite um segundo número: "))
    if num2 <= num1:
        print("Número menor que o número 2 não pode... tente novamente!")
    else:
        break

numeros = list(range(num1, num2))

escolha = random.choice(numeros)
# print(escolha)

input("O sistema ja escolheu um número... Preparado para adivinhar? aperte ENTER para começar: ")
print("Aguarde...")
time.sleep(2)


while x < 10:
    number_user = int(input("Digite um número o qual você acha que é: "))
    c = ctz(number_user)
    if c == "Parabéns você acertou!":
        print(c)
        break
    else:
        print(c)
        x += 1
        print(f"você tem: {10 - x} tentativas")
