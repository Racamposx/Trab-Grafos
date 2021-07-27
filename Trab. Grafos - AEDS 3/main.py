import time
import math

def menu(tipo,grafo,n_vertices,n_arestas):
    op = 0
    while op !=5:
        print("GRAFOS\n\nMENU\n1) Visualizar\n2) Conectividade\n3) Busca em profundidade\n4) Busca em largura\n5) Sair\n\n") 
        op = int(input("Entre com sua opção: "))
        if op==1:
            if tipo==1:
                visualizar_matriz(grafo,n_vertices,n_arestas)
            elif tipo==2:
                visualizar_lista(grafo,n_vertices,n_arestas)
        elif op==2:
            componentes_conexas(grafo,tipo)
        elif op==3:
            v = int(input("Entre com o vertice inicial: "))
            busca_por_profundidade(grafo, v)
        elif op==4:
            v = int(input("Entre com o vertice inicial: "))
            busca_largura(grafo,v)
        elif op==5:
            break
        else:
            print("Opção inválida!\n")    

def exibe(maior,menor,maior_indice,menor_indice,medio,array,vertices):
    print(f"Maior grau: v={maior} grau={maior_indice}\nMenor grau: v={menor} grau={menor_indice}\nGrau médio: {medio}\nFrequencia relativa: ")
    for i in range(menor, (maior + 1)):
        if array.count(i) != 0:
            print(f"Grau {i}: {array.count(i) / vertices}")

def visualizar_lista(grafo, vertices, arestas):
    maior_indice = grafo[0]
    menor_indice = grafo[0]

    maior = 0
    menor = math.inf
    array = []

    for i, element in enumerate(grafo):
        if element == []:
            continue
        else:
            tamanho = len(element)
            array.append(tamanho)
            if maior < tamanho:
                maior = tamanho
                maior_indice = i
            if menor > tamanho:
                menor = tamanho
                menor_indice = i

    medio = (arestas * 2) / float(vertices)
    exibe(maior,menor,maior_indice,menor_indice,medio,array,vertices)
    return

def visualizar_matriz(grafo, vertices, arestas):
    maior_indice = 0
    menor_indice= 0
    maior = 0
    menor = math.inf
    array = []
    for i in range(vertices):
        tamanho = 0
        for j in range(vertices):
            if grafo[i][j] != 0:
                tamanho += 1
        if maior < tamanho :
            maior_indice = i
            maior = tamanho
        if menor > tamanho:
            menor_indice = i
            menor = tamanho
        array.append(tamanho)
    medio = (arestas * 2) / vertices
    exibe(maior,menor,maior_indice,menor_indice,medio,array,vertices)
    return

global inicio
inicio = time.time()

def busca_largura(grafo, s):
    visitas = [0 for i in range(len(grafo))]
    caminho = [None] * len(grafo)
    fila = [s]
    pilha2 = [s]
    visitas[s] = 1
    caminho[s] = 0
    path = ''
    if tipo==1:
        path = 'buscaLarguraMatriz.txt'
        while len(fila) != 0:
            u = fila.pop(0)
            for v in range(len(grafo[u])):
                if grafo[u][v] != 0 and visitas[v] == 0:
                    fila.append(v)
                    pilha2.append(v)
                    visitas[v] = 1
                    caminho[v] = caminho[u] + 1
    elif tipo==2:
        path = 'buscaLarguraLista.txt' 
        while len(fila) != 0:
            u = fila.pop(0)
            for j in grafo[u]:
                aux = j[0]
                if visitas[aux] == 0:
                    fila.append(aux)
                    pilha2.append(aux)
                    visitas[aux] = 1
                    caminho[aux] = caminho[u] + 1

    print("Busca em largura: ")
    for j in range(len(grafo)):
        if caminho[j] is not None:
            print(f"{j}: {caminho[j]}") 

    file = open(path, 'w')

    file.write("vertice:caminho\n")
    for j in range(len(grafo)):
        if caminho[j] is not None:
            file.write(f"{j}: {caminho[j]}\n")
    
    caminho = list(filter(lambda a: a != None, caminho))
    maior = max(caminho)
    print(f'valor do maior nível: {maior}')
    print(">%s segundos decorrido<" % (time.time() - inicio))


def busca_por_profundidade(grafo, s):
    visitas = [0 for i in range(len(grafo))]
    caminho = [None] * len(grafo)
    pilha1 = [s]
    pilha2 = [s]
    visitas[s] = 1
    caminho[s] = 0
    path = ''
    if tipo==1:
        path = 'buscaProfundidadeMatriz.txt'
        while len(pilha1) != 0:
            u = pilha1[-1]
            flag = True
            for i in range(len(grafo[u])):
                if grafo[u][i] != 0 and visitas[i] == 0:
                    flag = False
                    pilha1.append(i)
                    pilha2.append(i)
                    visitas[i] = 1
                    caminho[i] = caminho[u] + 1
                    break
            if flag:
                pilha1.pop()
    elif tipo==2:
        path = 'buscaProfundidadeLista.txt'
        while len(pilha1) != 0:
            u = pilha1[-1]
            flag = True
            for i in grafo[u]:
                aux = i[0]
                if visitas[aux] == 0:
                    flag = False
                    pilha1.append(aux)
                    pilha2.append(aux)
                    visitas[aux] = 1
                    caminho[aux] = caminho[u] + 1
                    break
            if flag:
                pilha1.pop() 
    print("Busca com profundidade:")
    for i in range(len(grafo)):
        if caminho[i] is not None:
            print(f"{i}: {caminho[i]}")
    file = open(path, 'w')
    file.write("vertice:caminho\n")
    for i in range(len(grafo)):
        if caminho[i] is not None:
            file.write(f"{i}: {caminho[i]}\n")

def comp_conexa_aux(grafo, s, visitado,tipo):
    comp[s] = visitado
    visitas = [0 for i in range(len(grafo))]
    pilha1 = [s]
    pilha2 = [s]
    visitas[s] = 1

    if tipo ==1:
        while len(pilha1) != 0:
            u = pilha1[-1]
            flag = True
            for i in range(len(grafo[u])):
                if grafo[u][i] != 0 and visitas[i] == 0:
                    flag = False
                    pilha1.append(i)
                    pilha2.append(i)
                    visitas[i] = 1
                    break
            comp[u] = visitado
            if flag:
                pilha1.pop()

    elif tipo == 2:
        while len(pilha1) != 0:
            u = pilha1[-1]
            flag = True
            for i in grafo[u]:
                aux = i[0]
                if visitas[aux] == 0:
                    flag = False
                    pilha1.append(aux)
                    pilha2.append(aux)
                    visitas[aux] = 1
                    break
            comp[u] = visitado
            if flag:
                pilha1.pop()


def componentes_conexas(grafo,tipo):
    global comp
    comp = [0 for i in range(len(grafo))]
    visitado = 0
    k = 0
    for l in range(len(grafo)):
        if comp[l] == 0:
            visitado += 1
            comp_conexa_aux(grafo, l, visitado,tipo)
    k = max(comp)
    print(f"Comp. Conexas : {visitado}")
    for o in range(1, (k + 1)):
        print(f"{o}: {comp.count(o)} vertices") 

def monta_grafo(tipo):
    file = open(input("Entre com o nome do arquivo: "), 'r')
    line = file.readline().split(' ')

    vertices = int(line[0])
    arestas = int(line[1])
    print(arestas,vertices)
    tuplas = []
    for i in range(arestas):
        line = file.readline().strip().split(' ')
        v1 = int(line[0])
        v2 = int(line[1])
        w  = int(line[2])
        tuplas.append((v1,v2,w))
    file.close()
    if tipo == 1:
        matriz = [[0 for i in range(vertices)] for i in range(vertices)]   
        for element in tuplas:
            matriz[element[0]][element[1]] = element[2]
            matriz[element[1]][element[0]] = element[2]
        return matriz, vertices, arestas

    elif tipo == 2:
        lista = [[] for i in range(vertices)]
        for element in tuplas:
            lista[element[0]].append((element[1], element[2]))
            lista[element[1]].append((element[0], element[2]))
        return lista, vertices, arestas
    else:
        print("Erro na montagem do grafo!\n")
        exit()


print("Selecione a representação do seu grafo\n1-Matriz de adjacência\n2- Lista de Adjacência\n\n")
tipo = int(input())
while tipo < 1 or tipo > 2:
    tipo = int(input("Opção inválida! Tente novamente: "))

grafo,n_vertices,n_arestas = monta_grafo(tipo)
menu(tipo,grafo,n_vertices,n_arestas)
