#Ideia dessa versão: adicionar o sistema de perícias e adicionar a evolução de ficha, com habilidades, rituais, itens e patentes, criar uma versão automatizada disso tudo. 
#TENTAR usar dicionários.

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

#Lista de Origens
listaOrigens = ["Artista", "Atleta", "Cientista Forense", "Criminoso", "Desgarrado", "Dublê"];
origem = int;

#Lista de Classes
listaClasses = ["Combatente", "Especialista", "Ocultista"];
classe = int;

#Lista de Perícias
#Lista de Perícias
pericias = [
    {"codigo" : 1,"Nome" : "Acrobacia", "Valor" : 0},
    {"codigo" : 2,"Nome" : "Adestramento", "Valor" : 0}, 
    {"codigo" : 3,"Nome" : "Artes", "Valor" : 0}, 
    {"codigo" : 4,"Nome" : "Atletismo", "Valor" : 0}, 
    {"codigo" : 5,"Nome" : "Atualidades", "Valor" : 0}, 
    {"codigo" : 6,"Nome" : "Ciências", "Valor" : 0}, 
    {"codigo" : 7,"Nome" : "Crime", "Valor" : 0}, 
    {"codigo" : 8,"Nome" : "Diplomacia", "Valor" : 0}, 
    {"codigo" : 9,"Nome" : "Enganação", "Valor" : 0}, 
    {"codigo" : 10,"Nome" : "Fortitude", "Valor" : 0}, 
    {"codigo" : 11,"Nome" : "Furtividade", "Valor" : 0}, 
    {"codigo" : 12,"Nome" : "Iniciativa", "Valor" : 0},
    {"codigo" : 13,"Nome" : "Luta", "Valor" : 0}, 
    {"codigo" : 14,"Nome" : "Medicina", "Valor" : 0}, 
    {"codigo" : 15,"Nome" : "Ocultismo", "Valor" : 0}, 
    {"codigo" : 16,"Nome" : "Percepção", "Valor" : 0}, 
    {"codigo" : 17,"Nome" : "Pilotagem", "Valor" : 0}, 
    {"codigo" : 18,"Nome" : "Pontaria", "Valor" : 0}, 
    {"codigo" : 19,"Nome" : "Profissão", "Valor" : 0}, 
    {"codigo" : 20,"Nome" : "Reflexos", "Valor" : 0}, 
    {"codigo" : 21,"Nome" : "Religião", "Valor" : 0}, 
    {"codigo" : 22,"Nome" : "Sobrevivência", "Valor" : 0}, 
    {"codigo" : 23,"Nome" : "Tática", "Valor" : 0}, 
    {"codigo" : 24,"Nome" : "Tecnologia", "Valor" : 0}, 
    {"codigo" : 25,"Nome" : "Vontade", "Valor" : 0}
];
pontosPericias = str;

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
        nexPersonagem = nivelPersonagem * 5
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

#Sistema de perícias.
if classe == 1:
    pontosPericias = 1 + atributosTotais[2];

    print("Escolha uma perícia: [1] Luta ou [2] Pontaria")
    print("")
    escolha1 = int(input("Perícias escolhida: "))
    if escolha1 == 1:
        pericias[12]["Valor"] = 5;

    elif escolha1 == 2: 
        pericias[17]["Valor"] = 5;

    print("")
    print("Escolha uma perícias: [1] Fortitude ou [2] Reflexos")
    print("")
    escolha2 = int(input("Perícias escolhida: "))
    if escolha2 == 1:
        pericias[9]["Valor"] = 5;

    elif escolha2 == 2: 
        pericias[19]["Valor"] = 5;

if classe == 2:
    pontosPericias = 7 + atributosTotais[2];

if classe == 3:
    pontosPericias = 3 + atributosTotais[2]
    pericias[14]["Valor"] = 5
    pericias[24]["Valor"] = 5;

while pontosPericias > 0:
    print("")
    for i, pericia in enumerate(pericias, start=1):
        print(f"| {pericia["Nome"]:17} {pericia["Valor"]:>3} |");

    print("");
    print("Pontos disponíveis: ", pontosPericias);
    print("");
    print("Digite o NOME das perícias que deseja: ");

    busca = input("Busca: ").lower();
    achados = [i for i in pericias if busca in i["Nome"].lower()];

    if len(achados) == 0:
        print("Perícia não encontrada")
        print("");

    for pericia in achados:
        pontosPericias -= 1
        pericia["Valor"] += 5
        print(pericia["Nome"], pericia["Valor"]);