number_times=0
lista=[]
transposta=[]
matriz= []
def organizar_matriz(matriz):
    global number_times 
    number_times=0
    for j in matriz:
        quicksort(j)
        number_times+=1

def quicksort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quicksort(a, ini, pp)
        quicksort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    global mode , lista, number_times
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
            if i!=ini-1 and number_times==0:
                lista.append(f"{mode} {ini} {i+1} ")
    return ini - 1
    
def transpor(mtx1,mtx2):
    for i in range(len(mtx1[0])):
        coluna=[]
        for j in range(len(mtx1)):
            coluna.append(mtx1[j][i])
        mtx2.append(coluna)

tamanho = str(input('Digite a quantidade de linhas e colunas: ')).split()
linha = int(tamanho[0])
coluna = int(tamanho[1])

if 1 <= linha <= 200 and 1 <= coluna <= 200 and len(tamanho)==2:
    for l in range(linha):
        matriz.append([])
        valor = str(input(f'Como estão organizadas as fileiras da linha {l+1}º: ')).split()
        for c in valor:
            c = int(c)
            matriz[l].append(c)
else:
    print('Valor inválido. Encerrando...')
    exit()

mode="C"
organizar_matriz(matriz)
transpor(matriz,transposta)

mode="L"
organizar_matriz(transposta)

matriz=[]
transpor(transposta,matriz)

print(len(lista))

for i in lista:
    print(i)

for l in matriz:
    print(l)
input()
