def tengasActividadesSeleccionables(seleccionables):
    for e in seleccionables:
        if (e==True):
            return True
    return False
def voraz(horasIni,horasFin,resultado,numActividades):
    seleccionables=[True]*numActividades

    while tengasActividadesSeleccionables(seleccionables):
        #Tenemos que buscar la actividad seleccionable, que termine antes
        idMejor=-1
        for i in range(len(horasIni)):
            if(seleccionables[i]) and idMejor==-1:
                idMejor = i
            elif (seleccionables[i] and horasFin[i]<horasFin[idMejor]):
                idMejor= i
        #Apagamos la actividad para que no sea más seleccionable
        seleccionables[idMejor]=False
        #Mirar si esa actividad es compatible con las que ya tenemos seleccionadas
        #miramos que la hora de inicio de mi actividad sea compatibel con las horas de finalizacion de las que ya estan seleccionadas
        ok=True
        for i in range(len(horasFin)):
            if(resultado[i]):
                if(horasIni[idMejor]<horasFin[i]):
                    ok=False
        if ok:
            resultado[idMejor]=True



numActividades = int(input())
horasIni=[]
horasFin=[]

linea= input("")
trozos = linea.split(" ")
for trozo in trozos:
    horasIni.append(int(trozo))

linea= input("")
trozos = linea.split(" ")
for trozo in trozos:
    horasFin.append(int(trozo))


resultado=[False]*numActividades

voraz(horasIni,horasFin,resultado,numActividades)

print(resultado)


