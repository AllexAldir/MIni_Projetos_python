import matplotlib.pyplot as plt

meses = ["janeiro","fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
vendas = []
repetir = "sim"

while repetir == "sim":
    mes = input("Digite aqui o mês da venda: ").lower()

    while mes not in meses:
        mes = input("Mês imcompatível... Tente novamente: ").lower()

    print(f"Mês de: {mes}")
    vendas.append(float(input("Digite aqui o valor de vendas feitas nesse mês: ")))
    repetir = input("Deseja repetir essa operação? 'sim' ou 'não': ").lower()

#gráfico

plt.plot(meses,vendas)
plt.xlabel("meses")
plt.ylabel("vendas")
plt.title("Estatisticas de Vendas")
plt.show()
