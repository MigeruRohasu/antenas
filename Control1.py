from cProfile import label
from cmath import sqrt
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks 
from scipy.signal import unique_roots

##------------------- Libreria de exel ---------------------
## cargamos el documento exel que queremos 
#excel_document = openpyxl.load_workbook('Datos.xlsx')

## Abrimos la hoja de exel 
#sheet = excel_document.get_sheet_by_name('Sheet1')

## Comandos de celdas
#celda = sheet.cell(row = 2, column = 2)
#celda = 45




## -----------------------  Archivo TXT ----------------------

## Separamos la informacion importante y la que no se descarta
def Terreno(nombreArchivo,km):
    
    ## Abrimos el archivo
    txt=open(nombreArchivo)

    ## Leemos 6000 caracteres y lo separamos en un lista llamada datos
    datos=txt.read().split('\t')
    
    
    
    ## Calculamos la separacion en metros de la distancia total
    count = 0
    n=8
    for i in range(0,len(datos)):
        if i==n:
            n=n+5
            count=count+1
            
    puntos=(float(km)/count)
    
    ## Iniciamos variables
    distancia=0
    n=8
    count = 0
    
    salida=[[],[],[]]
    for i in range(0,len(datos)):
        if i==n:
            n=n+5    
            salida[0].append(distancia)
            salida[1].append(float(datos[i]))
            salida[2].append(0)
            count=count+1
            distancia=puntos*count

    """
    for i in range(0,len(salida[0])):
        print(salida[0][i],"\t",salida[1][i])
        """
    return salida
            
            
            
def Curvatura(distancia,altura,observador):
    
    parteOculta=[]
    terrenoReal=[]
    for i in range(0,len(altura)):
        radioTierra=6371000
        distanciaHorizonte=pow(((radioTierra+observador)**2)-(radioTierra**2),1/2)

        parteOculta.append(-(pow(distanciaHorizonte**2-2*distanciaHorizonte*distancia[i]+distancia[i]**2+radioTierra**2,1/2)-radioTierra))
        terrenoReal.append(altura[i]+parteOculta[i])
            
    """
    for i in range(0,len(parteOculta)):       
        print(parteOculta[i])
    """
    return parteOculta,terrenoReal


def FresnelElipsoide(antenaA,antenaB,frecuencia):
    landa=(3*10**8)/(frecuencia*10**9)
    ca=antenaB[0]-antenaA[0]
    co=antenaB[1]-antenaA[1]
    x=np.arctan(co/ca)    
    
    señal=[[],[]]
    for i  in range(0,ca):
        co_1=i*np.sin(x)
        señal[0].append(i+antenaA[0])
        señal[1].append(co_1+antenaA[1])
    
    radioFresnel=[[],[],[]]
    for i in range(0,ca):
        d1=i
        d2=ca-i
        radio=np.sqrt(landa*((d1*d2)/(d1+d2)))
        co_1=i*np.sin(x)
        
        radioFresnel[0].append(i+antenaA[0])
        radioFresnel[1].append(radio+antenaA[1]+co_1)
        radioFresnel[2].append(-(radio)+antenaA[1]+co_1)
          
    return señal,radioFresnel
"""
## Guardamos los datos en un archivo csv
exel=open("Datos de exel.csv","w")
exel.write(altitud)   
"""
     
      
            
#distancia=input("Distancia total entre los puntos  ")
#nombreDocumento=input("Ingrese nombre del kmz  ")

nombreDocumento="exel2 kmz.txt"

## ---------------- Grafica -------------

"""
x=input("Distancia en la que quiere poner el marcador  ") 
xx=[[],[]]
for i in range(0,3600):
    xx[0].append(x)
    xx[1].append(i)
plt.plot(xx[0],xx[1]) 
   """
    
# Graficas Basicas
distancia=74675
res=Terreno(nombreDocumento,distancia)
distancia=res[0]
altura=res[1]
nivelMar=res[2]
plt.plot(distancia,altura,label='terreno',color='green')
plt.plot(distancia,nivelMar,label='nivel del mar',color='blue')

curvaTerrestre,terrenoReal=Curvatura(distancia,altura,3)
plt.plot(distancia,curvaTerrestre,label='curvatura',color='red')
plt.plot(distancia,terrenoReal,label='elevacion real',color='brown')

# Graficas de antenas
frecuencia=8.5   
antena1=[0,(3525+20)]
antena2=[41486,(2524+20)]
antena3=[74280,(2+20)]

plt.plot(antena1[0],antena1[1],"x",label='Antena 1',color='cyan')
plt.plot(antena2[0],antena2[1],"x",label='Antena 2',color='purple')
plt.plot(antena3[0],antena3[1],"x",label='Antena 3',color='violet')

# Grafica del radio de las antenas
señal,radioFresnel=FresnelElipsoide(antena1,antena2,frecuencia)
plt.plot(señal[0],señal[1],label='señal 1',color='violet')
plt.plot(radioFresnel[0],radioFresnel[1],color='violet')
plt.plot(radioFresnel[0],radioFresnel[2],color='violet')

señal,radioFresnel=FresnelElipsoide(antena2,antena3,frecuencia)
plt.plot(señal[0],señal[1],label='señal 2',color='sienna')
plt.plot(radioFresnel[0],radioFresnel[1],color='sienna')
plt.plot(radioFresnel[0],radioFresnel[2],color='sienna')

plt.title('Grafica de distancia')
plt.xlabel('Distancia')
plt.ylabel('Elevacion')
plt.grid()
plt.legend()

plt.show()
    

 
    