tamanho = str(input('Digite a quantidade de linhas e colunas: ')).split()
linha = int(tamanho[0])
coluna = int(tamanho[1])
matriz = []
if 1 <= linha <= 200 and 1 <= coluna <= 200:    
    for l in range(linha):
        matriz.append([])
        valor = str(input(f'Como estão organizadas as fileiras da linha {l+1}º: ')).split()
        for c in valor:
            c = int(c)
            matriz[l].append(c)
constante = 0
trocas = []
tam = len(matriz)
while tam > 0:
    i = 0
    while i < tam - 1:
        if matriz[i] > matriz[i + 1]:
            constante += 1
            trocas.append(f'C {i+1} {i+2}')
            var = matriz[i]
            matriz[i] = matriz[i+1]
            matriz[i+1] = var
        i+=1
    tam -= 1
organizada = []
for pos, valor in enumerate(matriz):
    organizada.append([])
    for pos_1, valor_1 in enumerate(valor):
        ponto = ((pos)*len(valor))+pos_1
        organizada[pos].append(ponto+1)
for c, i in zip(matriz, organizada):
    pos_1 = 0
    for j, k in zip(c, i):
        if j!= k:
            for pos_2, valor in enumerate(c):
                if valor == k:
                    constante += 1
                    trocas.append(f'L {pos_1 + 1} {pos_2 + 1}')
                    for g in range(len(matriz)):
                        matriz[g][pos_1] = k
                        matriz[g][pos_2] = j
        pos_1 += 1
print(constante)
for i in trocas: print(i)
