def voraz(tiempos):
    tiempoEsperaAcumulado=0
    acu=0
    while(len(tiempos)!=0):
        menorTiempo=tiempos[0]
        for i in range(len(tiempos)):
            if (tiempos[i]<menorTiempo):
                menorTiempo=tiempos[i]

        tiempos.remove(menorTiempo)
        acu=acu+menorTiempo
        tiempoEsperaAcumulado=tiempoEsperaAcumulado+acu
    return tiempoEsperaAcumulado

tiempos=[]

linea = input("")
trozos = linea.split(" ")
for trozo in trozos:
    tiempos.append(int(trozo))


tiempoEsperaAcumulado = voraz(tiempos)
print(tiempoEsperaAcumulado)