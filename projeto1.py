n = int(input('tamanho da matriz:' ))

numero = 0
linha = [0] * n
matriz_A = [linha] * n
matrizB = [linha] * n


for i in range(n):
    linha = []
    for j in range(n):
        numero = int(input(" informe os número da matriz A: {},{} : ".format(i, j)))
        linha.append(numero)

    matriz_A[i] = linha

print('informe os números da  Matriz B:')
for k in range(n):
    linha1 = []

    for l in range(n):
        numero = int(input("Matriz B {},{} : ".format(k, l)))
        linha1.append(numero)
    matrizB[k] = linha1

print('MATRIZ A')
for i in range(n):
    for j in range(n):
        print(f'[{matriz_A[i][j]:^5}]', end=' ')
    print()

print('-='*30)
print('MATRIZ B:') 
for k in range(n):
    for l in range(n):
        print(f'[{matrizB[k][l]:^5}]', end=' ')

    print()
print('-='*30)
print('MATRIZ BTS:')
bst = []
for i in range(n):
    BsTl = [0] * n
    bst.append(BsTl)
for x in range(0, n):
    for y in range(x, n):
        bst[x][y] = matrizB[x][y]


for x in range(0, n):
    for y in range(0, n):
        print(f'[{(bst[x][y]):^5}]', end=' ')
    print()
print('-='*30)
print('MATRIZ AT:')
at = []
for m in range(n):
    atc = [0] * n
    at.append(atc)
    for o in range(n):
        at[m][o] = (matriz_A[o][m])

c = 0
for i in range(n):
    for j in range(n):
        print(f'[{at[i][j]:^5}]', end=' ')

        c += 1
    print()
print('-='*30)
print('MATRIZ  SAIDA:')
saida = []
for m in range(n):
    sai = [0] * n
    saida.append(sai)
    for o in range(n):
        saida[m][o] = (at[o][m])
for x in range(0, n):
    for y in range(0, n):
        print(f'[{at[x][y] * bst[x][y]:^5}]', end=' ')
    print()

'''obs: faltou a matriz Bnx'''