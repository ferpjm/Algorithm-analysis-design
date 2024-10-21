
def BTTodas(a,r,n,sol,aparicionesGastadas,contadorSoluciones,etapa):
    intento=len(a)-1
    while(intento>=0):
        if aparicionesGastadas[intento]<r[intento]:
            sol[etapa]= a[intento]
            aparicionesGastadas[intento]=aparicionesGastadas[intento]+1
            if(etapa==n-1):
                print(sol)
                contadorSoluciones[0]=contadorSoluciones[0]+1
            else:
                BTTodas(a,r,n,sol,aparicionesGastadas,contadorSoluciones,etapa+1)

            sol[etapa] = '-'
            aparicionesGastadas[intento] = aparicionesGastadas[intento] - 1
        intento=intento-1

a = ['a','b','c']
r = [1,2,1]

n = 0
for i in range(len(r)):
    n = n+r[i]

sol=['-']*n
aparicionesGastadas = [0]*len(r)
contadorSoluciones=[0]

BTTodas(a,r,n,sol,aparicionesGastadas,contadorSoluciones,0)
print(contadorSoluciones[0])