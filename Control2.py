import matplotlib.pyplot as plt
import numpy as np
import statistics as sta


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
                
def Curvatura(distancia,altura,observador,a):
    
    parteOculta=[]
    terrenoReal=[]
    radioTierra=6371000*(a)
    distanciaHorizonte=pow(((radioTierra+observador)**2)-(radioTierra**2),1/2)
    
    for i in range(0,len(altura)):
        parteOculta.append(-(pow(distanciaHorizonte**2-2*distanciaHorizonte*distancia[i]+distancia[i]**2+radioTierra**2,1/2)-radioTierra))
                    
            
    co=-(parteOculta[len(parteOculta)-1])
    ca=distancia[len(distancia)-1]
    angulo=np.arctan(co/ca)
    #print(ca," / ",co," / ",angulo)
    
    for i in range(0,len(parteOculta)):
        co=np.tan(angulo)*distancia[i]
        parteOculta[i]=parteOculta[i]+co
        #print(angulo,"   ",distancia[i],"   ",co)
        terrenoReal.append(altura[i]+parteOculta[i])
    """
    for i in range(0,len(parteOculta)):       
        print(parteOculta[i])
    """
    return parteOculta,terrenoReal

def FresnelElipsoide(antenaA,antenaB,frecuencia,altura,distancia):
    
    invacion=[[],[]]
    porcentaje=[[],[]]
    
    landa=(3*10**8)/(frecuencia*10**9)
    ca=antenaB[0]-antenaA[0]
    co=antenaB[1]-antenaA[1]
    x=np.arctan(co/ca)    
    
    señal=[[],[]]
    for i  in range(0,ca):
        co_1=i*np.sin(x)
        señal[0].append(i+antenaA[0])
        señal[1].append(co_1+antenaA[1])
    
    radioFresnel=[[],[],[],[],[],[]]
    for i in range(0,ca):
        d1=i
        d2=ca-i
        radio=np.sqrt(landa*((d1*d2)/(d1+d2)))
        co_1=i*np.sin(x)
        
        radioFresnel[0].append(i+antenaA[0])
        radioFresnel[1].append(radio)
        radioFresnel[2].append(-(radio))
        radioFresnel[3].append(radio+antenaA[1]+co_1)
        radioFresnel[4].append(-(radio)+antenaA[1]+co_1)     
        radioFresnel[5].append(radio*0.4)   
        
    for a in range(0,len(distancia)):
        for b in range(0,len(radioFresnel[0])):
            if distancia[a] == radioFresnel[0][b]:
                #(altura[a]<=radioFresnel[3][b])and
                if (altura[a]>=radioFresnel[4][b]):
                    invacion[0].append(distancia[a])
                    invacion[1].append(altura[a]-radioFresnel[4][b])
                    porcentaje[0].append(distancia[a])
                    porcentaje[1].append(((altura[a]-radioFresnel[4][b])*100)/(radioFresnel[1][b]))
                else:
                    invacion[0].append(distancia[a])
                    invacion[1].append(0)
                    porcentaje[0].append(distancia[a])
                    porcentaje[1].append(0)

        
    return señal,radioFresnel,invacion,porcentaje

def reflexionEspecular(antenaA,antenaB,altura,distancia):
    angulo=[[],[],[]]
    for a in range(0,len(distancia)):
        if (distancia[a]>antenaA[0])and(distancia[a]<antenaB[0]):
            angulo[0].append(distancia[a])
            
            co1=antenaA[1]-altura[a]
            ca1=distancia[a]-antenaA[0]
            angulo[1].append(np.arctan(co1/ca1))
            
            co2=antenaB[1]-altura[a]
            ca2=antenaB[0]-antenaA[0]-ca1
            angulo[2].append(np.arctan(co2/ca2))
            
    return angulo
        
def perdidadLluvia(k,Rmm,alfa,lluvia):
    res=k*(Rmm**alfa)
    print("coeficiente lluvia \n",res)
    res=lluvia*res
    print("perdidas totales por lluvia \n",res)
    
def tierralisa(altura,fresnel):
    prom=sta.pstdev(altura)
    band=False
    for i in fresnel:
        if(i*0.1>prom):
            band=True
    print("la tierra lisa = ",band)

def ruido(elementos,b,ta,tamb,te,l,f,Gamp):
    
    l=10**(l/10)

    k=1.380649*(10**-23)
    res=0
    for i in ( elementos):
        if(i=="antena"):
            res=k*b*ta
            print("despues de la antena pN= ",res)
        if(i=="cable"):
            ss=res
            res=(ss/l)+k*b*tamb*(1-(1/l))
            print("despues de la cable pN= ",res)
        if(i=="amplificador"):
            ss=res
            res=(ss+(k*b*te*(f-1)))*Gamp
            print("despues de la amplificador pN= ",res)
        
    
    
# def perdidaGases
"""
## Guardamos los datos en un archivo csv
exel=open("Datos de exel.csv","w")
exel.write(altitud)   
"""
     
      
            
#distancia=input("Distancia total entre los puntos  ")
#nombreDocumento=input("Ingrese nombre del kmz  ")

nombreDocumento="exel2 kmz.txt"

## ---------------- Grafica -------------

# Graficas Basicas



# ancho de banda
b=14000

# temperatura antena
ta=100

# temperatura ambiente
tamb=300

# temperatura equipo activo
te=290

# Perdidas del cable
l=3.06

# elemento activo
f=3

Gamp=20

orden=["antena","cable","amplificador"]
ruido(orden,b,ta,tamb,te,l,f,Gamp)

distancia=80
res=Terreno(nombreDocumento,distancia)

distancia=res[0]
altura=res[1]
nivelMar=res[2]

frecuencia=7

# R(mm/h)
Rmm=70
k=0.001425
alfa=1.4745
celdaLluvia=20


perdidadLluvia(k,Rmm,alfa,celdaLluvia)

distancia=[0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000,65000,70000,75000,80000]

altura=[2600,2361,2356,2300,2200,2100,2020,1356,1129,1152,768,1143,1340,766,713,1299,1300]

altura=[1680,1550,1400,1200,1000,800,1000,1200,1400,1800,2100,2150,2150,2290,2100,2150,2500]

plt.plot(distancia,altura,label='terreno',color='green')

curvaTerrestre,terrenoReal=Curvatura(distancia,altura,0,1)
print("1  ",terrenoReal)
plt.plot(distancia,curvaTerrestre,label='curvatura 1',color='red')
plt.plot(distancia,terrenoReal,label='elevacion real 1',color='red')

curvaTerrestre,terrenoReal=Curvatura(distancia,altura,0,(4/3))
print("(4/3)  ",terrenoReal)
plt.plot(distancia,curvaTerrestre,label='curvatura 4/3',color='brown')
plt.plot(distancia,terrenoReal,label='elevacion real 4/3',color='brown')


print(sta.mean(terrenoReal))

antena1=[0,(terrenoReal[distancia.index(0)]+6)]
antena2=[80000,(terrenoReal[distancia.index(80000)]+17)]
antena3=[80000,(terrenoReal[distancia.index(80000)]+16)]

# Graficas de antenas
plt.plot(antena1[0],antena1[1],"x",label='Antena 1',color='cyan')
plt.plot(antena2[0],antena2[1],"x",label='Antena 2',color='purple')
plt.plot(antena2[0],antena2[1],"x",label='Antena 3',color='black')

# Grafica del radio de las antenas
señal,radioFresnel,invacion,porcentaje=FresnelElipsoide(antena1,antena2,frecuencia,terrenoReal,distancia)
plt.plot(señal[0],señal[1],label='señal 1',color='violet')
plt.plot(radioFresnel[0],radioFresnel[3],color='violet')
plt.plot(radioFresnel[0],radioFresnel[4],color='violet')
plt.title('Plano General')
plt.xlabel('Distancia')
plt.ylabel('Elevacion')
plt.grid()
plt.legend()

tierralisa(terrenoReal,radioFresnel[3])

plt.figure()
plt.plot(radioFresnel[0],radioFresnel[1],color='blue',label='Radio de Fresnel')
plt.plot(radioFresnel[0],radioFresnel[5],color='black',label='limite')
#plt.plot(radioFresnel[0],radioFresnel[2],color='blue')
plt.plot(invacion[0],invacion[1],color='red',label='Invacion')
plt.plot(porcentaje[0],porcentaje[1],color='green',label='Porcentaje de Invacion')
plt.title('FresnelElipsoide')
plt.xlabel('Distancia')
#plt.ylabel('Elevacion')
plt.grid()
plt.legend()


plt.figure()
angulos=reflexionEspecular(antena1,antena2,terrenoReal,distancia)
plt.plot(angulos[0],angulos[1],color='red',label='Angulo antena1')
plt.plot(angulos[0],angulos[2],color='green',label='Angulo antena2')
plt.title('Reflexion especular')
plt.xlabel('Distancia')
plt.ylabel('Grados')
plt.grid()
plt.legend()

plt.show()    