n=0
lista=[]
def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    global n , lista
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
            if i!=ini-1:
                n+=1
                lista.append(f"L {ini} {i+1} ")
    return ini - 1

def transp(x):
    global matriz
    for l in matriz:
        linha=[]
        for c in matriz:
            linha.append



tamanho = str(input('Digite a quantidade de linhas e colunas: ')).split()
linha = int(tamanho[0])
coluna = int(tamanho[1])

matriz = []

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
print(matriz)
quick_sort(matriz)
print(n)

quick_sort()
for i in lista:
    print(i)
print(quick_sort(matriz))
