valorX = int(input("Digite o Valor de X: "))

if (type(valorX) == int):
    print("Valor aceito.")

valorY = int(input("Digite o Valor de Y: "))

if (type(valorY) == int):
    print("Valor aceito.")

if (valorX > 10 and valorY <= 4):
    print("Proposição verdadeira. (x > 10 and y <= 4).")

else:
    print("Proposição falsa. (x > 10 and y <= 4).")