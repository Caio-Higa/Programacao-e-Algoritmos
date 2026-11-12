#Nome de Jogador e Personagem
nomeJogador = str(input("Digite o seu nome: "))
nomePersonagem = str(input("Digite o nome do seu personagem: "))

#Valores Atributos
atributoAgilidade = 0;
atributoForca = 0;
atributoIntelecto = 0;
atributoPresenca = 0;
atributoVigor = 0;
pontosAtributosIniciais = 9;

#Valores Status
pontosVida = int;
pontosDeterminação = int;
nivelPersonagem = int;

#Lista de Origens
listaOrigens = ["Artista", "Atleta", "Cientista Forense", "Criminoso", "Desgarrado", "Dublê"];

#Lista de Classes
listaClasses = ["Combatente", "Especialista", "Ocultista"];

#Seleção de origem
print("");
for i,origens in enumerate(listaOrigens, start=1):
    print(i, origens);

print("");
origem = int(input("Digite o número da origem desejada: "));

while True:
    if origem <= 6 and origem >= 1:
        print("")
        print("Origem selecionada: ", listaOrigens[origem - 1])
        break;

    else:
        origem = int(input("Origem não encontrada, digite novamente: "));












