import os
os.system("cls")

frutas = ['Siriguela']
def menu():
    print("-----------------------------------------")
    print("-------------Menu Principal--------------")
    print("-----------------------------------------")
    print("| Digite 1 para inserir uma nova fruta   |")
    print("| Digite 2 para mostrar as frutas        |")
    print("| Digite 3 para excluir uma fruta        |")
    print("| Digite 4 para sair do sistema          |")
    print("-----------------------------------------")
    opcao = input("Digite uma opção do menu:\n")
    if (opcao == "1"):

        inserirFruta()
    elif (opcao =="2"):
        mostrarFrutas()

    elif (opcao=="3"):
        excluirFrutas()

    elif(opcao=="2"):
        sair()
    else:
        mostrarOpcoes()

def inserirFruta():
    fruta = input("Dgitie o nome de uma fruta:\n")
    frutas.append(fruta)
    mostrarOpcoes()


def excluirFrutas():
    fruta = input("Digite o nome da fruta para exluir:\n")
    frutas.remove(fruta)
    mostrarOpcoes()


def mostrarFrutas():
    i =1
    for fruta in frutas:
        print("Fruta {0}: {1}".format(i, fruta))
        i +=1
    mostrarOpcoes()

    
def sair():
    print("thcau!")

def mostrarOpcoes():
    tecla = input("Se deseja voltar ao menu, digite 1, sair digite 2")
    if (tecla =="1"):
        menu()
    else:
        sair()

menu()