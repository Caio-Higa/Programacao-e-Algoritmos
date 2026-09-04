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
pontosVida = 0;
pontosDeterminação = 0;
nivelPersonagem = 0;

#Lista e seleção de origem
listaOrigens = ("[1] Artista" , "[2] Atleta" , "[3] Cientista Forence" , "[4] Criminoso" , "[5] Desgarrado" , "[6] Dublê");
print("")
print("Origens disponíveis: " , listaOrigens);
print("")

origemSelecionada = int(input("Digite o número da Origem desejada: "));
print("")
 
if (origemSelecionada > 6):
    print("Origem não encontrada")

while origemSelecionada > 6 or origemSelecionada < 1:
    origemSelecionada = int(input("Digite o número da Origem desejada: "))
    print ("Origem não encontrada")
    if origemSelecionada <= 6 and origemSelecionada > 0:
        print("Origem escolhida: ", origemSelecionada)
        break
        
if (origemSelecionada == 1):
    origemSelecionada = "Artista"
    print("Origem escolhida: Artista");

elif (origemSelecionada == 2):
    origemSelecionada = "Atleta"
    print("Origem escolhida: Atleta");

elif (origemSelecionada == 3):  
    origemSelecionada = "Cientista Forence"
    print("Origem escolhida: Cientista Forence");

elif (origemSelecionada == 4):
    origemSelecionada = "Criminoso"
    print("Origem escolhida: Criminoso");

elif (origemSelecionada == 5):
    origemSelecionada = "Desgarrado"
    print("Origem escolhida: Desgarrado");

elif (origemSelecionada == 6):
    origemSelecionada = "Dublê"
    print("Origem escolhida: Dublê");

else:
    print("Origem não encontrada.")

#Lista e seleção de Classe
listaClasses = ("[1] Combatente" , "[2] Especialista" , "[3] Ocultista")
print("")
print("Classes disponíveis: " , listaClasses)
print("")

classeSelecionada = int(input("Digite o número da Classe desejada: "));
print("")

if (classeSelecionada > 3):
    print("Classe não encontrada")

while classeSelecionada > 3 or classeSelecionada < 1:
    classeSelecionada = int(input("Digite o número da Classe desejada: "))
    print("Classe não encontrada")
    if classeSelecionada <= 4 and classeSelecionada > 0:
        print("Classe escolhida: ", classeSelecionada)
        break

if (classeSelecionada == 1):
    classeSelecionada = "Combatente"
    print("Classe escolhida: Combatente");

elif (classeSelecionada == 2):
    classeSelecionada = "Especialista"
    print("Classe escolhida: Especialista");

elif (classeSelecionada == 3):
    classeSelecionada = "Ocultista"
    print("Classe escolhida: Ocultista");

else:
    print("Classe não encontrada.");

#Distribuição de Atributos
print("")
print("Pontos Disponíveis: ", pontosAtributosIniciais);
print("")
atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
print("")

while atributoAgilidade > 3 or atributoAgilidade < 0:
        print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
        print("")
        atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
        print("")

        if atributoAgilidade <= 3 and atributoAgilidade >= 0:
            break

pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

print("Pontos disponíveis: ", pontosDisponíveis)
print("")
atributoForca = int(input("Digite o valor da sua Força: "));
print("")

while atributoForca > 3 or atributoForca < 0:
        print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
        print("")
        atributoForca = int(input("Digite o valor da sua Força: "));
        print("")

        if atributoForca <= 3 and atributoForca >= 0:
            break

pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

print("Pontos disponíveis: ", pontosDisponíveis)
print("")
atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
print("")

while atributoIntelecto > 3 or atributoIntelecto < 0:
        print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
        print("")
        atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
        print("")

        if atributoIntelecto <= 3 and atributoIntelecto >= 0:
            break

pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

print("Pontos disponíveis: ", pontosDisponíveis)
print("")
atributoPresenca = int(input("Digite o valor da sua Presença: "));
print("")

while atributoPresenca > 3 or atributoPresenca < 0:
        print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
        print("")
        atributoPresenca = int(input("Digite o valor da sua Presença: "));
        print("")

        if atributoPresenca <= 3 and atributoPresenca >= 0:
            break

pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

print("Pontos disponíveis: ", pontosDisponíveis)
print("")
atributoVigor = int(input("Digite o valor do seu Vigor: "));
print("")

while atributoVigor > 3 or atributoVigor < 0:
        print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
        print("")
        atributoVigor = int(input("Digite o valor do seu Vigor: "));
        print("")

        if atributoVigor <= 3 and atributoVigor >= 0:
            break

pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

print("Pontos disponíveis: ", pontosDisponíveis)
print("")
print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
print("")

while (pontosDisponíveis < 0):
        print("Pontos utilizados ultrapassaram o limite disponível.")
        print("")
        print("Pontos Disponíveis: ", pontosAtributosIniciais);
        print("")
        atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
        print("")

        while atributoAgilidade > 3 or atributoAgilidade < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
                print("")

                if atributoAgilidade <= 3 and atributoAgilidade >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoForca = int(input("Digite o valor da sua Força: "));
        print("")

        while atributoForca > 3 or atributoForca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoForca = int(input("Digite o valor da sua Força: "));
                print("")

                if atributoForca <= 3 and atributoForca >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
        print("")

        while atributoIntelecto > 3 or atributoIntelecto < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
                print("")

                if atributoIntelecto <= 3 and atributoIntelecto >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoPresenca = int(input("Digite o valor da sua Presença: "));
        print("")

        while atributoPresenca > 3 or atributoPresenca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoPresenca = int(input("Digite o valor da sua Presença: "));
                print("")

                if atributoPresenca <= 3 and atributoPresenca >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoVigor = int(input("Digite o valor do seu Vigor: "));
        print("")

        while atributoVigor > 3 or atributoVigor < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoVigor = int(input("Digite o valor do seu Vigor: "));
                print("")

                if atributoVigor <= 3 and atributoVigor >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
        print("")


while (pontosDisponíveis > 0):
        print("Pontos de atributos ainda disponíveis, por favor, distribua-os.")
        print("")
        print("Pontos Disponíveis: ", pontosAtributosIniciais);
        print("")
        atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));

        while atributoAgilidade > 3 or atributoAgilidade < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
                print("")

                if atributoAgilidade <= 3 and atributoAgilidade >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoForca = int(input("Digite o valor da sua Força: "));
        print("")

        while atributoForca > 3 or atributoForca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoForca = int(input("Digite o valor da sua Força: "));
                print("")

                if atributoForca <= 3 and atributoForca >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
        print("")

        while atributoIntelecto > 3 or atributoIntelecto < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
                print("")

                if atributoIntelecto <= 3 and atributoIntelecto >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoPresenca = int(input("Digite o valor da sua Presença: "));
        print("")

        while atributoPresenca > 3 or atributoPresenca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoPresenca = int(input("Digite o valor da sua Presença: "));
                print("")

                if atributoPresenca <= 3 and atributoPresenca >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoVigor = int(input("Digite o valor do seu Vigor: "));
        print("")

        while atributoVigor > 3 or atributoVigor < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoVigor = int(input("Digite o valor do seu Vigor: "));
                print("")

                if atributoVigor <= 3 and atributoVigor >= 0:
                    break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
        print("")

if (pontosDisponíveis == 0): 
        print("Atributos distribuidos corretamente.")
        print("")

#Calculo de Pontos de Vida e Pontos de Determinação
if (classeSelecionada == "Combatente"):
     pontosVida = 20 + atributoVigor
     pontosDeterminação = 6 + atributoPresenca

if (classeSelecionada == "Especialista"):
     pontosVida = 16 + atributoVigor
     pontosDeterminação = 8 + atributoPresenca

if (classeSelecionada == "Ocultista"):
     pontosVida = 12 + atributoVigor
     pontosDeterminação = 10 + atributoPresenca

print("|Pontos de Vida: ", pontosVida, "|", "Pontos de Determinação: ", pontosDeterminação, "|");

print("")
print("NEX = Nível de Exposição Paranormal")
print("Nível de personagem Exemplo: Nível 0 = NEX 0%, Nível 1 = NEX 5%, Nível 2 = NEX 10%")
print("")
nivelPersonagem = int(input("Digite o nível do seu personagem: "))

if (type(nivelPersonagem) == int):
     print("Nível aceito.")
     print("")

nexPersonagem = nivelPersonagem * 5;

if classeSelecionada == "Combatente":
     pontosVida = pontosVida + ((4 + atributoVigor) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((3 + atributoPresenca) * (nivelPersonagem - 1))

if classeSelecionada == "Especialista":
     pontosVida = pontosVida + ((3 + atributoVigor) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((4 + atributoPresenca) * (nivelPersonagem - 1))

if classeSelecionada == "Ocultista":
     pontosVida = pontosVida + ((2 + atributoVigor) * (nivelPersonagem - 1))
     pontosDeterminação = pontosDeterminação + ((5 + atributoPresenca) * (nivelPersonagem - 1))

while True:

    print("---------------------------------------------------------------------------")
    print("|Nome de Jogador: ", nomeJogador, "|", "|Nome da Personagem: ", nomePersonagem, "|")
    print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
    print("")
    print("|Origem: ", origemSelecionada, "|")
    print("|Classe: ", classeSelecionada, "|")
    print("|NEX: ", nexPersonagem, "% |")
    print("")
    print("|Pontos de Vida: ", pontosVida, "|", "|Pontos de Determinação: ", pontosDeterminação, "|")
    print("---------------------------------------------------------------------------")
    print("")
    print("Deseja mudar algo na sua ficha?")
    print("[1] Nome do Jogador")
    print("[2] Nome do Personagem")
    print("[3] Origem do Personagem")
    print("[4] Classe do Personagem")
    print("[5] Nível do Personagem")
    print("[6] Atributos do Personagem")
    print("[7] Não desejo alterar nada")
    print("")

    mudançaFicha = int(input("Digite o número relacionado a opção que deseja: "))

    #Mudança Nome Jogador
    if mudançaFicha == 1:
        nomeJogador = str(input("Digite o seu nome: "))

    #Mudança Nome Personagem
    elif (mudançaFicha == 2):
        nomePersonagem = str(input("Digite o nome do seu Personagem: "))

    #Mudança Origem
    elif (mudançaFicha == 3):
        listaOrigens = ("[1] Artista" , "[2] Atleta" , "[3] Cientista Forence" , "[4] Criminoso" , "[5] Desgarrado" , "[6] Dublê");
        print("")
        print("Origens disponíveis: " , listaOrigens);
        print("")

        origemSelecionada = int(input("Digite o número da Origem desejada: "));
        print("")
 
        if (origemSelecionada > 6):
            print("Origem não encontrada")

        while origemSelecionada > 6 or origemSelecionada < 1:
            origemSelecionada = int(input("Digite o número da Origem desejada: "))
            print ("Origem não encontrada")
            if origemSelecionada <= 6 and origemSelecionada > 0:
                print("Origem escolhida: ", origemSelecionada)
                break
        
        if (origemSelecionada == 1):
            origemSelecionada = "Artista"
            print("Origem escolhida: Artista");

        elif (origemSelecionada == 2):
            origemSelecionada = "Atleta"
            print("Origem escolhida: Atleta");

        elif (origemSelecionada == 3):  
            origemSelecionada = "Cientista Forence"
            print("Origem escolhida: Cientista Forence");

        elif (origemSelecionada == 4):
            origemSelecionada = "Criminoso"
            print("Origem escolhida: Criminoso");

        elif (origemSelecionada == 5):
            origemSelecionada = "Desgarrado"
            print("Origem escolhida: Desgarrado");

        elif (origemSelecionada == 6):
            origemSelecionada = "Dublê"
            print("Origem escolhida: Dublê");

        else:
            print("Origem não encontrada.")

    #Mudança Classe
    elif (mudançaFicha == 4):
        listaClasses = ("[1] Combatente" , "[2] Especialista" , "[3] Ocultista")
        print("")
        print("Classes disponíveis: " , listaClasses)
        print("")

        classeSelecionada = int(input("Digite o número da Classe desejada: "));
        print("")

        if (classeSelecionada > 3):
            print("Classe não encontrada")

        while classeSelecionada > 3 or classeSelecionada < 1:
            classeSelecionada = int(input("Digite o número da Classe desejada: "))
            print("Classe não encontrada")
            if classeSelecionada <= 4 and classeSelecionada > 0:
                print("Classe escolhida: ", classeSelecionada)
                break

        if (classeSelecionada == 1):
            classeSelecionada = "Combatente"
            print("Classe escolhida: Combatente");

        elif (classeSelecionada == 2):
            classeSelecionada = "Especialista"
            print("Classe escolhida: Especialista");

        elif (classeSelecionada == 3):
            classeSelecionada = "Ocultista"
            print("Classe escolhida: Ocultista");

        else:
            print("Classe não encontrada.");

        #Calculo de Pontos de Vida e Pontos de Determinação
        if (classeSelecionada == "Combatente"):
            pontosVida = 20 + atributoVigor
            pontosDeterminação = 6 + atributoPresenca

        if (classeSelecionada == "Especialista"):
            pontosVida = 16 + atributoVigor
            pontosDeterminação = 8 + atributoPresenca

        if (classeSelecionada == "Ocultista"):
            pontosVida = 12 + atributoVigor
            pontosDeterminação = 10 + atributoPresenca

        print("|Pontos de Vida: ", pontosVida, "|", "Pontos de Determinação: ", pontosDeterminação, "|");

        #Calculo de Vida e Determinação por nível
        if classeSelecionada == "Combatente":
            pontosVida = pontosVida + ((4 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((3 + atributoPresenca) * (nivelPersonagem - 1))

        if classeSelecionada == "Especialista":
            pontosVida = pontosVida + ((3 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((4 + atributoPresenca) * (nivelPersonagem - 1))

        if classeSelecionada == "Ocultista":
            pontosVida = pontosVida + ((2 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((5 + atributoPresenca) * (nivelPersonagem - 1))

    #Mudança Nível
    elif (mudançaFicha == 5):
        nivelPersonagem = int(input("Digite o nível do seu personagem: "))
        if (type(nivelPersonagem) == int):
            print("Nível aceito.")
            print("")
    
        nexPersonagem = nivelPersonagem * 5;

    #Mudança Atributos
    elif (mudançaFicha == 6):
        print("")
        print("Pontos Disponíveis: ", pontosAtributosIniciais);
        print("")
        atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
        print("")

        while atributoAgilidade > 3 or atributoAgilidade < 0:
            print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
            print("")
            atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
            print("")

            if atributoAgilidade <= 3 and atributoAgilidade >= 0:
                break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoForca = int(input("Digite o valor da sua Força: "));
        print("")

        while atributoForca > 3 or atributoForca < 0:
            print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
            print("")
            atributoForca = int(input("Digite o valor da sua Força: "));
            print("")

            if atributoForca <= 3 and atributoForca >= 0:
                break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
        print("")

        while atributoIntelecto > 3 or atributoIntelecto < 0:
            print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
            print("")
            atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
            print("")

            if atributoIntelecto <= 3 and atributoIntelecto >= 0:
                break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoPresenca = int(input("Digite o valor da sua Presença: "));
        print("")

        while atributoPresenca > 3 or atributoPresenca < 0:
            print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
            print("")
            atributoPresenca = int(input("Digite o valor da sua Presença: "));
            print("")

            if atributoPresenca <= 3 and atributoPresenca >= 0:
                break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        atributoVigor = int(input("Digite o valor do seu Vigor: "));
        print("")

        while atributoVigor > 3 or atributoVigor < 0:
            print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
            print("")
            atributoVigor = int(input("Digite o valor do seu Vigor: "));
            print("")

            if atributoVigor <= 3 and atributoVigor >= 0:
                break

        pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

        print("Pontos disponíveis: ", pontosDisponíveis)
        print("")
        print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
        print("")

        while (pontosDisponíveis < 0):
            print("Pontos utilizados ultrapassaram o limite disponível.")
            print("")
            print("Pontos Disponíveis: ", pontosAtributosIniciais);
            print("")
            atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
            print("")

            while atributoAgilidade > 3 or atributoAgilidade < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
                print("")

                if atributoAgilidade <= 3 and atributoAgilidade >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoForca = int(input("Digite o valor da sua Força: "));
            print("")

            while atributoForca > 3 or atributoForca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoForca = int(input("Digite o valor da sua Força: "));
                print("")

                if atributoForca <= 3 and atributoForca >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
            print("")

            while atributoIntelecto > 3 or atributoIntelecto < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
                print("")

                if atributoIntelecto <= 3 and atributoIntelecto >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoPresenca = int(input("Digite o valor da sua Presença: "));
            print("")

            while atributoPresenca > 3 or atributoPresenca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoPresenca = int(input("Digite o valor da sua Presença: "));
                print("")

                if atributoPresenca <= 3 and atributoPresenca >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoVigor = int(input("Digite o valor do seu Vigor: "));
            print("")

            while atributoVigor > 3 or atributoVigor < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoVigor = int(input("Digite o valor do seu Vigor: "));
                print("")

                if atributoVigor <= 3 and atributoVigor >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
            print("")


        while (pontosDisponíveis > 0):
            print("Pontos de atributos ainda disponíveis, por favor, distribua-os.")
            print("")
            print("Pontos Disponíveis: ", pontosAtributosIniciais);
            print("")
            atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));

            while atributoAgilidade > 3 or atributoAgilidade < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoAgilidade = int(input("Digite o valor da sua Agilidade: "));
                print("")

                if atributoAgilidade <= 3 and atributoAgilidade >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoForca = int(input("Digite o valor da sua Força: "));
            print("")

            while atributoForca > 3 or atributoForca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoForca = int(input("Digite o valor da sua Força: "));
                print("")

                if atributoForca <= 3 and atributoForca >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
            print("")

            while atributoIntelecto > 3 or atributoIntelecto < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoIntelecto = int(input("Digite o valor do seu Intelecto: "));
                print("")

                if atributoIntelecto <= 3 and atributoIntelecto >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoPresenca = int(input("Digite o valor da sua Presença: "));
            print("")

            while atributoPresenca > 3 or atributoPresenca < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoPresenca = int(input("Digite o valor da sua Presença: "));
                print("")

                if atributoPresenca <= 3 and atributoPresenca >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            atributoVigor = int(input("Digite o valor do seu Vigor: "));
            print("")

            while atributoVigor > 3 or atributoVigor < 0:
                print("Valor não aceito. O valor de atributo inicial só pode ser abaixo de 3.")
                print("")
                atributoVigor = int(input("Digite o valor do seu Vigor: "));
                print("")

                if atributoVigor <= 3 and atributoVigor >= 0:
                    break

            pontosDisponíveis = pontosAtributosIniciais - (atributoAgilidade + atributoForca + atributoIntelecto + atributoPresenca + atributoVigor)

            print("Pontos disponíveis: ", pontosDisponíveis)
            print("")
            print("|Agilidade: ", atributoAgilidade, "|", "|Força: ", atributoForca, "|", "|Intelecto: ", atributoIntelecto, "|", "|Presença: ", atributoPresenca, "|", "|Vigor: ", atributoVigor, "|")
            print("")

        if (pontosDisponíveis == 0): 
            print("Atributos distribuidos corretamente.")
            print("")

        #Calculo de Pontos de Vida e Pontos de Determinação
        if (classeSelecionada == "Combatente"):
            pontosVida = 20 + atributoVigor
            pontosDeterminação = 6 + atributoPresenca

        if (classeSelecionada == "Especialista"):
            pontosVida = 16 + atributoVigor
            pontosDeterminação = 8 + atributoPresenca

        if (classeSelecionada == "Ocultista"):
            pontosVida = 12 + atributoVigor
            pontosDeterminação = 10 + atributoPresenca

        print("|Pontos de Vida: ", pontosVida, "|", "Pontos de Determinação: ", pontosDeterminação, "|");

        #Calculo de Vida e Determinação por nível
        if classeSelecionada == "Combatente":
            pontosVida = pontosVida + ((4 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((3 + atributoPresenca) * (nivelPersonagem - 1))

        if classeSelecionada == "Especialista":
            pontosVida = pontosVida + ((3 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((4 + atributoPresenca) * (nivelPersonagem - 1))

        if classeSelecionada == "Ocultista":
            pontosVida = pontosVida + ((2 + atributoVigor) * (nivelPersonagem - 1))
            pontosDeterminação = pontosDeterminação + ((5 + atributoPresenca) * (nivelPersonagem - 1))
     

    if (mudançaFicha == 7):
        print ("Ficha completa, aproveite.")
        break

