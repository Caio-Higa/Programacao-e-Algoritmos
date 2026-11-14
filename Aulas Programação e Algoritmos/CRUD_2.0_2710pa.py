#Nome de Jogador e Personagem
nomeJogador = str(input("Digite o seu nome: "))
nomePersonagem = str(input("Digite o nome do seu personagem: "))

#Valores Atributos
atributosNomes = ["Agilidade", "Força", "Intelecto", "Presença", "Vigor"];
atributosTotais = [0, 0, 0, 0, 0];
pontosAtributosIniciais = 9;

#Valores Status
pontosVida = int;
pontosDeterminação = int;
nivelPersonagem = 0;
nexPersonagem = nivelPersonagem * 5;

#Lista de Origens
listaOrigens = ["Artista", "Atleta", "Cientista Forense", "Criminoso", "Desgarrado", "Dublê"];
origem = int;

#Lista de Classes
listaClasses = ["Combatente", "Especialista", "Ocultista"];
classe = int;

#Seleção de origem
print("");
for i, origens in enumerate (listaOrigens, start=1):
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

#Seleção de classes
print("");
for i, classes in enumerate (listaClasses, start=1):
    print(i, classes);

print("");
classe = int(input("Digite o número da classe desejada: "));

while True:
    if classe <= 3 and classe >= 1:
        print("")
        print("Classe selecionada: ", listaClasses[classe - 1])
        break;

    else:
        classe = int(input("Classe não encontrada, digite novamente: "));

#Distribuição de Atributos
while True:
    pontosAtributosIniciais = 9;
    print("");
    print("Pontos disponíveis: ", pontosAtributosIniciais);

    if pontosAtributosIniciais == 9:

        while True:
            print("")
            atributosTotais[0] = int(input("Digite o valor de Agilidade: "))
            if atributosTotais[0] > 3 or atributosTotais[0] < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.");

            else:
                print("")
                pontosAtributosIniciais = pontosAtributosIniciais - atributosTotais[0]
                print("Pontos Disponíveis: ", pontosAtributosIniciais)
                break;

        while True:
            print("")
            atributosTotais[1] = int(input("Digite o valor de Força: "))
            if atributosTotais[1] > 3 or atributosTotais[1] < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.");

            else:
                print("")
                pontosAtributosIniciais = pontosAtributosIniciais - atributosTotais[1]
                print("Pontos Disponíveis: ", pontosAtributosIniciais)
                break;

        while True:
            print("")
            atributosTotais[2] = int(input("Digite o valor de Intelecto: "))
            if atributosTotais[2] > 3 or atributosTotais[2] < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.");

            else:
                print("")
                pontosAtributosIniciais = pontosAtributosIniciais - atributosTotais[2]
                print("Pontos Disponíveis: ", pontosAtributosIniciais)
                break;

        while True:
            print("")
            atributosTotais[3] = int(input("Digite o valor de Presença: "))
            if atributosTotais[3] > 3 or atributosTotais[3] < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.");

            else:
                print("")
                pontosAtributosIniciais = pontosAtributosIniciais - atributosTotais[3]
                print("Pontos Disponíveis: ", pontosAtributosIniciais)
                break;

        while True:
            print("")
            atributosTotais[4] = int(input("Digite o valor de Vigor: "))
            if atributosTotais[4] > 3 or atributosTotais[4] < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.");

            else:
                print("")
                pontosAtributosIniciais = pontosAtributosIniciais - atributosTotais[4]
                print("Pontos Disponíveis: ", pontosAtributosIniciais)
                break;
        
        if pontosAtributosIniciais < 0 or pontosAtributosIniciais > 0:
            print("Pontos distribuidos de forma incorreta. Por favor, distribua-os novamente.");

        else:
            print("")
            print("Pontos distribuidos corretamente.")
            print("")
            break;

for i, atributo in enumerate(atributosNomes):
    print(atributo, atributosTotais[i]);

#Cálculo de Pontos de Vida e Pontos de Determinação
if classe == 1:
     pontosVida = 20 + atributosTotais[4]
     pontosDeterminação = 6 + atributosTotais[3];

if classe == 2:
     pontosVida = 16 + atributosTotais[4]
     pontosDeterminação = 8 + atributosTotais[3];

if classe == 3:
     pontosVida = 12 + atributosTotais[4]
     pontosDeterminação = 10 + atributosTotais[3];

print("");
print("Pontos de vida: ", pontosVida, "|", "Pontos de Determinação: ", pontosDeterminação);

#Determinação de nível (NEX) de personagem
print("");
print("NEX = Nível de Exposição Paranormal");
print("Nível de personagem Exemplo: Nível 0 = NEX 0%, Nível 1 = NEX 5%, Nível 2 = NEX 10%");
print("");

while True:
    nivelPersonagem = int(input("Digite o nível do seu personagem: "));

    if (type(nivelPersonagem) == int):
        print("Nível aceito.")
        print("")
        break;

    else:
        continue;

if classe == 1:
     pontosVida = pontosVida + ((4 + atributosTotais[4]) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((3 + atributosTotais[3]) * (nivelPersonagem - 1));

if classe == 2:
     pontosVida = pontosVida + ((3 + atributosTotais[4]) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((4 + atributosTotais[3]) * (nivelPersonagem - 1));

if classe == 3:
     pontosVida = pontosVida + ((2 + atributosTotais[4]) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((5 + atributosTotais[3]) * (nivelPersonagem - 1));