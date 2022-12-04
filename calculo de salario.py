# Folha de Pagamento

# Precisamos saber quanto uma determinada empresa deve pagar para seus
# colaboradores, porém temos apenas a quantidade de horas trabalhadas e o valor
# hora. Escreva um programa que leia o número de um colaborador, seu número de
# horas trabalhadas, o valor que recebe por hora e calcula o salário desse
# colaborador. Em seguida, apresente o número e o salário do colaborador, com
# duas casas decimais.

# - Entrada

# Você receberá 2 números inteiros e 1 número com duas casas decimais,
# representando o número, quantidade de horas trabalhadas e o valor que o
# funcionário recebe por hora trabalhada.

# - Saída

# Exiba o número e o salário do colaborador, conforme exemplo abaixo, com um
# espaço em branco antes e depois da igualdade. No caso do salário, também deve
# haver um espaço em branco após o $.


repetir = "sim"
lista_num = []

while repetir =="sim":

    numero = int(input("Digite o número desse funcionário: "))
    while numero in lista_num:
        numero = int(input("Número de funcionário ja existe na lista... Tente novamente: "))

    lista_num.append(numero)
    val_hora = float(input("Digite aqui o valor da hora trabalhada: "))
    horas = float(input("Digite aqui o número de horas trabalhadas desse funcionário: "))
    print(f"O salário desse funcionário é: {round(val_hora*horas,2)} R$ e seu número: {numero}")
    repetir = input("Deseja repetir a operação: ").lower()

