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
def Creartxt(nombreArchivo,km):
    
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

                
    
    
    for i in range(0,len(salida[0])):
        print(salida[0][i],"\t",salida[1][i])
        
    return salida
            
            
            
def Curvatura(distancia,altura,observador):
    for i in range(0,len(altura)):
        radioTierra=6371000
        distanciaHorizonte=pow(((radioTierra+observador)**2)-(radioTierra**2),1/2)
        try:
            parteOculta.append(pow(distanciaHorizonte**2-2*distanciaHorizonte*distancia[i]+distancia[i]**2+radioTierra**2,1/2)-radioTierra)
            terrenoReal.append(parteOculta[i]+altura[i])
        except:
            parteOculta=[pow(distanciaHorizonte**2-2*distanciaHorizonte*distancia[i]+radioTierra**2,1/2)-radioTierra]
            terrenoReal=[parteOculta[i]+altura[i]]
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
    
    for i  in range(0,ca):
        co_1=i*np.sin(x)
        try:
            señal[0].append(i+antenaA[0])
            señal[1].append(co_1+antenaA[1])
        except:
            señal=[[i+antenaA[0]],[co_1+antenaA[1]]]
            
            
    for i in range(0,ca):
        d1=i
        d2=ca-i
        #radio=np.sqrt(landa*((d1*d2)/(d1*d2)))
        """
        try:
            radioFresnel[0].append()
            radioFresnel[1].append()
            radioFresnel[2].append()
        except:
            radioFresnel=[[],[],[]]
            """
    return señal
"""
## Guardamos los datos en un archivo csv
exel=open("Datos de exel.csv","w")
exel.write(altitud)   
"""
     
      
            
#distancia=input("Distancia total entre los puntos  ")
#nombreDocumento=input("Ingrese nombre del kmz  ")
distancia=74675
nombreDocumento="exel2 kmz.txt"
res=Creartxt(nombreDocumento,distancia)
distancia=res[0]
altura=res[1]
res1,res2=Curvatura(distancia,altura,3)


## ---------------- Grafica -------------
#plt.plot(res[0],res[2],label='nivel del mar')
plt.plot(res[0],res[1],label='terreno',color='green')
plt.plot(res[0],res[2],label='nivel del mar',color='blue')
plt.plot(res[0],res1,label='curvatura',color='red')
plt.plot(res[0],res2,label='elevacion real',color='brown')

plt.plot(0,3525+20,"x",label='Antena 1',color='cyan')
plt.plot(41091,2717+20,"x",label='Antena 2',color='purple')
plt.plot(73885,725+20,"x",label='Antena 3',color='violet')

res4=FresnelElipsoide([0,3525+20],[41091,2717+20],10)
plt.plot(res4[0],res4[1],label='señal 1',color='violet')

res5=FresnelElipsoide([41091,2717+20],[73885,725+20],10)
plt.plot(res5[0],res5[1],label='señal 2',color='sienna')

plt.title('Grafica de distancia')
plt.xlabel('Distancia')
plt.ylabel('Elevacion')
plt.grid()
plt.legend()
plt.show()

