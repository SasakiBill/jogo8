import copy
import buscas
import expansaoJogo
import time

print("-----------------------------")
print("--------JOGO DOS 8 ----------")
print("-----------------------------")
#time.sleep(1)
continuar = 1
print("Esse jogo pode ser resolvido através de buscas de Inteligência Artificial")
while(continuar == 1):
    
    #time.sleep(2)
    print("Antes de tudo, qual tabuleiro inicial deseja utilizar?")

    print("Opção 1:")
    print("[2, 8, 1]")
    print("[0, 4, 3]")
    print("[7, 6, 5]")
    #time.sleep(1)

    print("Opção 2:")
    print("[1, 3, 4]")
    print("[8, 6, 2]")
    print("[7, 0, 5]")
    #time.sleep(1)

    print("Opção 3:")
    print("[2, 8, 3]")
    print("[1, 6, 4]")
    print("[7, 0, 5]")
    
    esc = int(input("\nInforme a sua escolha"))

    if(esc == 1):
        configInicial = [[2,8,1],[0,4,3],[7,6,5],[0,None],[0, 0]]
    elif(esc == 2):
        configInicial = [[1,3,4],[8,6,2],[7,0,5],[0,None],[0, 0]]
    elif(esc == 3):
        configInicial = [[2,8,3],[1,6,4],[7,0,5],[0,None],[0, 0]]
    else:
        print("Opção Inválida")
        break

    print("O tabuleiro ficou configurado da seguinte forma:")
    expansaoJogo.mostraTabuleiro(configInicial)
    
    #time.sleep(1)
    print("As buscas disponíveis para resolução são: Busca Cega em Largura ou Busca Heurística com A-Estrela")
    print("Para continuar, informe qual algoritmo deseja para a busca")
    print("1: Busca em Largura")
    print("2: Busca Utilizando A-Estrela com Heurística de Peças fora do Lugar?")
    print("3: Busca utilizando A-Estrela com Heurística de Distância de Manhattan?")

    op = int(input('Informe uma opção:'))

    if(op==1):
        buscas.buscaLargura(configInicial)
    elif(op==2):
        buscas.buscaAestrelaPecas(configInicial)
    elif(op==3):
        buscas.buscaAestrelaManhattan(configInicial)
    else:
        print("Opção Inválida")
        break

    print("--------------")

    esc2 = int(input("\nDeseja verificar a resolução com outra configuração? (1 p/ sim, 0 p/ não)"))
    if(esc2 == 1):
        continuar = 1
    elif(esc2 == 0):
        continuar = 0
        print("\n Até mais o/")
        break
