import copy

def verificaVitoria(tab): 
    a = True
    if tab[0][0]!=1:
        a = False
    if tab[0][1]!=2:
        a = False
    if tab[0][2]!=3:
        a = False
    if tab[1][0]!=8:
        a = False
    if tab[1][1]!=0:
        a = False
    if tab[1][2]!=4:
        a = False
    if tab[2][0]!=7:
        a = False
    if tab[2][1]!=6:
        a = False
    if tab[2][2]!=5:
        a = False
    return a


def mostraTabuleiro(tab): 
    print('Profundidade do nó atual:', tab[3][0])
    print('-----------')
    print(tab[0])
    print(tab[1])
    print(tab[2])
    print('-----------')

def expandir(tab):
    jogadas = []
    if tab[1][1]==0: 
        # move pra baixo
        a = copy.deepcopy(tab)
        a[1][1] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[1][1] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[1][1] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)
        a[1][1] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #2 se vazio esta no canto esquerdo superior
    elif tab[0][0]==0:
        # move pra cima
        a = copy.deepcopy(tab)
        a[0][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[0][0] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #3 se vazio esta no canto direito superior
    elif tab[0][2]==0:
        # move pra cima
        a = copy.deepcopy(tab)
        a[0][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[0][2] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #4 se vazio esta no canto inferior esquerdo
    elif tab[2][0]==0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[2][0] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #5 se vazio esta no canto inferior direito
    elif tab[2][2]==0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[2][2] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #6 se vazio esta no meio da linha de cima
    elif tab[0][1]==0:
        # move pra cima
        a = copy.deepcopy(tab)
        a[0][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[0][1] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[0][1] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #7 se vazio esta no meio da linha de baixo
    elif tab[2][1]==0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[2][1] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[2][1] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #8 se vazio esta no meio da coluna da esquerda
    elif tab[1][0]==0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[1][0] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)
        a[1][0] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[1][0] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #9 se vazio esta no meio da coluna da direita
    elif tab[1][2]==0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[1][2] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)
        a[1][2] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[1][2] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    return jogadas

def mostraJogadas(tab):
    print("\nAs jogadas foram:")
    pilha = []
    while(tab[3][1] != None): #vai até o nó raiz
        pilha.append(tab)
        tab = tab[3][1]
    pilha.append(tab)
    while(len(pilha)>0):
        temp = pilha.pop()
        mostraTabuleiro(temp)
