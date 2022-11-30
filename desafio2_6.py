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
tam = len(matriz[0])
while tam > 0:
    i = 0
    while i < tam - 1:
        if matriz[0][i] > matriz[0][i + 1]:
            print(f'C {i+1} {i+2}')
            for pos, valor in enumerate(matriz):
                var = matriz[pos][i]
                matriz[pos][i] = matriz[pos][i+1]
                matriz[pos][i+1] = var
        i+=1
    tam -= 1
tam = len(matriz)
while tam > 0:
    i = 0
    while i < tam - 1: 
        if matriz[i] > matriz[i + 1]:
            print(f'L {i+1} {i+2}')
            var = matriz[i]
            matriz[i] = matriz[i+1]
            matriz[i+1] = var
        i+=1
    tam -= 1
print(matriz)
