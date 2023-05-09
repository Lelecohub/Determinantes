#FUNÇÕES
def menor (matriz, i, j):
    return [linha[:j] + linha[j+1:] for linha in (matriz[:i] + matriz[i+1:])]

def determinante(matriz):
    x = len(matriz)
    if x == 1:
        return matriz[0][0]
    else:
        det = 0
        for j in range(x):
            sinal = (-1) ** j
            men = menor (matriz, 0, j)
            det += sinal * matriz[0][j] * determinante(men)
        return det
    
#DEFINIÇÃO MATRIZ NxN    
n = int(input("Defina o tamanho da matriz (N): "))

if  n <= 0:
    print("Erro: Insira valor inteiro maior que 0.")
else:
#INSERÇÃO VALORES DA MATRIZ
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            matriz[i][j] = valor
#IMPRESSÃO MATRIZ
    print("\nMatriz A =") 
    for linha in matriz: 
        print(linha)
#IMPRESSÃO DETERMINANTE DA MATRIZ    
    A = matriz
    det_A = determinante(A)
    print("\ndeterminante(A) = ", det_A)
