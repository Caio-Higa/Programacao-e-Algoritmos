valorTemp = float(input("Digite a temperatura do quarto: "))

if (type(valorTemp) == float):
    print("Temperatura Aceita.")

if (valorTemp >= 30):
    print("A temperatura do quarto está quente, bem vindo ao nordeste.")

else:
    print("A temperatura do quarto está baixa.")