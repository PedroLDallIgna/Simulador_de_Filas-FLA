##Solução implementada por Pedro Lucas Dall' Igna, estudante do IFC - Concórdia
##Implementação de um simulador de filas de banco para a disciplina de Fundamentos do professor Hewerton 

idosos = []
gestantes = []
populares = []
nPessoas = 0

print("+-------------------------------------------------------------------------------+")
print("|                                                                               |")
print("|                              #################                                |")
print("|                              #   PYTHONBANK  #                                |")
print("|                              #################                                |")
print("|                                                                               |")
print("+-------------------------------------------------------------------------------+")
print("Olá! Este é o Python Bank. Está solução é para automação das filas do nosso banco.\n"
	"Existem três filas, determinadas pela prioridade de atendimento:\n"
	"-> IDOSOS - Pessoas acima dos 60 anos;\n"
	"-> GESTANTES - Mulheres grávidas;\n"
	"-> POPULARES - Pessoas comuns.")
print()
dia = input("Tecle ENTER para começar o dia de trabalho")
print()
while dia == '':
    acrescentar = input("Desejas acrescentar alguém às filas? - [SIM/NAO]: ").upper()
    print()
    while acrescentar != 'SIM' and acrescentar != 'NAO':
        acrescentar = input("DADO INVÁLIDO! Quer acrescentar alguém? - [SIM/NAO]: ").upper()
        print()
    if acrescentar == 'SIM':
        print()
        nome = str(input("Nome -> ")).upper()
        if nome == '':
            nome = "ANÔNIMO"
        nPessoas += 1
        tipoFila = str(input("Escolha a fila - IDOSOS, GESTANTES e POPULARES: ")).upper()
        print()
        while tipoFila != "IDOSOS" and tipoFila != "GESTANTES" and tipoFila != "POPULARES":
            tipoFila = input("DADO INVÁLIDO! Escolha a fila - IDOSOS, GESTANTES e POPULARES: ").upper()
            print()
        if tipoFila == "IDOSOS":
            idosos.append(nome)
        elif tipoFila == "GESTANTES":
            gestantes.append(nome)
        elif tipoFila == "POPULARES":
            populares.append(nome)
        print()
        print(" * Fila idosos:", idosos)
        print()
        print(" * Fila gestantes:", gestantes)
        print()
        print(" * Fila populares:", populares)
        print()
    else:
        if len(idosos) == 0 and len(gestantes) == 0 and len(populares) == 0:
            print("NÃO HÁ NINGUÉM NAS FILAS!")
            desejo = input("Quer esperar?  - [SIM/NAO]: ").upper()
            print()
            while desejo != 'SIM' and desejo != 'NAO':
                desejo = input("DADO INVÁLIDO. Quer esperar? - [SIM/NAO]: ").upper()
                print()
            if desejo == 'SIM':
                dia = ''
            elif desejo == 'NAO':
            	dia = 'a'
        else:
            retirar = input("Deseja retirar alguém da fila (conforme a prioridade das filas) - [SIM/NAO]: ").upper()
            print()
            while retirar != 'SIM' and retirar != 'NAO':
                retirar = input("DADO INVÁLIDO! Deseja retira alguém alguém das filas - [SIM/NAO]: ").upper()
                print()
            if retirar == 'NAO':
                dia = ''
            elif retirar == 'SIM':
                if len(idosos) != 0:
                    print()
                    print("%s já foi atendido" % idosos[0])
                    del(idosos[0])
                elif len(idosos) == 0:
                    if len(gestantes) != 0:
                        print()
                        print("%s já foi atendido" % gestantes[0])
                        del(gestantes[0])
                    elif len(gestantes) == 0:
                        if len(populares) != 0:
                            print()
                            print("%s já foi atendido" % populares[0])
                            del(populares[0])
                        elif len(populares) == 0:
                            break
            print()
            print(" * Fila idosos:", idosos)
            print()
            print(" * Fila gestantes:", gestantes)
            print()
            print(" * Fila populares:", populares)
            print()
else:
    print()
    if nPessoas > 1:
        print("O expediente terminou! Foram atendidas %d pessoas." % nPessoas)
    else:
        print("O expediente terminou! Foi atendida %d pessoa." % nPessoas)