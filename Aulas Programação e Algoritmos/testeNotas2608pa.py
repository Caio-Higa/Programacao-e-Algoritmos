notaMat1 = float(input("Digite o valor da P1 de matemática: "))
notaMat2 = float(input("Digite o valor da P2 de matemática: "))
notaMat3 = float(input("Digite o valor da P3 de matemática: "))

if (type(notaMat1 + notaMat2 + notaMat3) == float):
    print("Notas aceitas.")

maiorNota = max(notaMat1, notaMat2, notaMat3)
#função max(), pega o valor mais alto.

mediaNota = (notaMat1 + notaMat2 + notaMat3) / 3

print("Nota mais alta: ", maiorNota, " / Média em matemática: ", mediaNota)

if (mediaNota >= 7):
    print("Status: Aprovado")

elif (5 < mediaNota < 7):
    print("Status: Recuperação")

else:
    print("Status: Reprovado")
