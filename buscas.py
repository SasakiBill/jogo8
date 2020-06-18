import copy
import expansaoJogo
import datetime
import math

def buscaLargura(configInicial):
    primeiroInstante = datetime.datetime.now()
    fila = []
    fila.append(configInicial)
    nosExp = 0
    endgame = False
    jogadaExistente = False
    listaJogadas = []
    while (endgame == False):
        listaExpandir = copy.deepcopy(fila[0])
        listaJogadas.append(fila.pop(0))
        nosExp = nosExp+1
        print('\nNó expandido:', nosExp)
        expansaoJogo.mostraTabuleiro(listaExpandir)
        if expansaoJogo.verificaVitoria(listaExpandir) == True:
            print("----------------------------------")
            print("\n Solução Encontrada com sucesso!")
            print("----------------------------------")
            endgame = True
        else:
            jogadasExpandidas = expansaoJogo.expandir(listaExpandir)
            for n in jogadasExpandidas:
                for m in listaJogadas:
                    if(n[0][0]==m[0][0] and n[0][1]==m[0][1] and n[0][2]==m[0][2] and n[1][0]==m[1][0] and n[1][1]==m[1][1] and n[1][2]==m[1][2] and n[2][0]==m[2][0] and n[2][1]==m[2][1] and n[2][2]==m[2][2]):
                        jogadaExistente = True
                if(jogadaExistente == False):
                    fila.append(n)
                else:
                    jogadaExistente = False  
                listaExpandir.clear()
    ultimoInstante = datetime.datetime.now()
    print('Tempo Total de Execução da Busca Cega:', ultimoInstante-primeiroInstante)

def buscaAestrela(configInicial):
    primeiroInstante = datetime.datetime.now()
    fila = []
    fila.append(configInicial)
    nosExp = 0
    endgame = False
    jogadaExistente = False
    listaJogadas = []
    while (endgame == False):
        #Aqui foram feitas as alteração em relação à ordenação
        for n in fila:
            if (n[4][1] > maiorManhattan):
                maiorManhattan = n[4][1]
        sorted(fila, key = lambda x: maiorManhattan, reverse= False)

        listaExpandir = copy.deepcopy(fila[0])
        listaJogadas.append(fila.pop(0))
        
        nosExp = nosExp+1
        maiorManhattan = 0
        
       
        print('\nNó expandido:', nosExp)
        expansaoJogo.mostraTabuleiro(listaExpandir)
         
        if expansaoJogo.verificaVitoria(listaExpandir) == True:
            print("----------------------------------")
            print("\n Solução Encontrada com sucesso!")
            print("----------------------------------")
            endgame = True
        else:
            jogadasExpandidas = expansaoJogo.expandir(listaExpandir)
            for n in jogadasExpandidas:
                n[4][0] = pecasFora(n)
                n[4][1] = Manhattan(n)
                for m in listaJogadas:
                    if(n[0][0]==m[0][0] and n[0][1]==m[0][1] and n[0][2]==m[0][2] and n[1][0]==m[1][0] and n[1][1]==m[1][1] and n[1][2]==m[1][2] and n[2][0]==m[2][0] and n[2][1]==m[2][1] and n[2][2]==m[2][2]):
                        jogadaExistente = True
                if(jogadaExistente == False):
                    fila.append(n)
                else:
                    jogadaExistente = False  
                listaExpandir.clear()
    ultimoInstante = datetime.datetime.now()
    print('Tempo Total de Execução da Busca por A-Estrela:', ultimoInstante-primeiroInstante)

def pecasFora(tab): 
    a = 0
    if tab[0][0]!=1:
        a = a+1
    if tab[0][1]!=2:
        a = a+1
    if tab[0][2]!=3:
         a = a+1
    if tab[1][0]!=8:
        a = a+1
    if tab[1][1]!=0:
        a = a+1
    if tab[1][2]!=4:
        a = a+1
    if tab[2][0]!=7:
        a = a+1
    if tab[2][1]!=6:
        a = a+1
    if tab[2][2]!=5:
        a = a+1
    return a
  
def Manhattan(tab): 
    h = 0
    for i in range(3):
        for j in range(3):
            if(tab[i][j]==0):
                h = h + abs(0-i) + abs(0-j)
            if(tab[i][j]==1):
                h = h + abs(0-i) + abs(1-j)
            if(tab[i][j]==2):
                h = h + abs(0-i) + abs(2-j)
            if(tab[i][j]==3):
                h = h + abs(1-i) + abs(0-j)
            if(tab[i][j]==4):
                h = h + abs(1-i) + abs(1-j)
            if(tab[i][j]==5):
                h = h + abs(1-i) + abs(2-j)
            if(tab[i][j]==6):
                h = h + abs(2-i) + abs(0-j)
            if(tab[i][j]==7):
                h = h + abs(2-i) + abs(1-j)
            if(tab[i][j]==8):
                h = h + abs(2-i) + abs(2-j)
        return h

        

