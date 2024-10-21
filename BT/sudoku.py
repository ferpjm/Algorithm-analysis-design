import math
def lee_sudoku(nombre_fichero):
    fichero = open(nombre_fichero ,'r')
    S=[[None]*9]*9
    i=0
    for line in fichero.readlines():
        S[i] = [int(x) for x in line.split(' ')]
        i=i+1
    fichero.close()
    return S

def imprime_sudoku(S):
    for s in S:
        print(*s)

 # Funci´on auxiliar para expandir la soluci´on parcial fila a fila
def avanza(fila,col):
 if col==8:
    return (fila+1,0)
 else:
    return (fila,col+1)

def resuelve_sudoku(i,j,S):
    if i==9: # Comprueba si la soluci´on parcial est´a completa
        return True # Soluci´on encontrada
    else:
# Comprueba si S[i][j] contiene un n´umero inicial fijo
        if S[i][j]!=0:
            (i_nueva ,j_nueva) = avanza(i,j)
            return resuelve_sudoku(i_nueva ,j_nueva ,S)
        else:
            sol_encontrada = False
            k=1
         # Genera candidatos
            while k<10 and not sol_encontrada:
         # Comprueba validez del candidato
                if es_candidato_valido(i,j,k,S): # ¡¡INEFICIENTE!!
                    # Incluye d´ıgito en celda (i,j)
                     S[i][j] = k

                     (i_nueva ,j_nueva) = avanza(i,j)
                     sol_encontrada = resuelve_sudoku(i_nueva ,j_nueva ,S)

                k=k+1

             # Si no hay soluci´on se marca la celda (i,j) como vac´ıa
            if not sol_encontrada:
                S[i][j] = 0

             # Devolver si se ha encontrado una soluci´on
            return sol_encontrada

# Comprueba si el d´ıgito en la celda (fila,col) is v´alido
def es_candidato_valido(fila,col,digito,S):
     # Comprueba conflicto en fila
    for k in range(0,9):
        if k!=col and digito==S[fila][k]:
            return False
    # Comprueba conflicto en columna
    for k in range(0,9):
        if k!=fila and digito==S[k][col]:
            return False

    # Comprueba conflicto en caja
    caja_fila= math.floor(fila/3)
    caja_col = math.floor(col/3)
    for k in range(0,3):
        for m in range(0,3):
            if fila!=3*caja_fila+k and col!=3*caja_col+m:
                if digito==S[3*caja_fila+k][3*caja_col+m]:
                    return False

    return True


S = lee_sudoku('sudoku01_input.txt')
if(resuelve_sudoku(0,0,S)):
    imprime_sudoku(S)

