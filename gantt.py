import matplotlib.pyplot as plt
import numpy as np
import random as ran
x1=[1,1,3,5,5,10,16,16,17,19,24,29,31,32,36,37,39,40,40,44,45,46,47,50,51,52,54,57,59,59,64,66,71,74,78,79,81,82,87,88,88,89,92,93,94,95,96,99,101,102,107,109,114,120,122,122,123,124,128,129,130,131,136,137,138,138,141,142,142,142.3,142.6,143,143,143.3,143.6,144,144,159,206,325,439,449,479,575,585,585,590,595]

b=['1. Analisis legal de normas ', '1.1. Nacionales', '1.2. Internacionales', '2. Diseño y Gestion de espacios', '2.1. Diseño de pistas de Aterrizaje ', '2.2. Diseño torre de control', '2.3. Diseño de edificio Vuelos nacionales', '2.3.1. Bahia de parqueo aviones', '2.3.2. Check in aerolineas', '2.3.3. Zona de llegada', '2.3.4. Zona de salida', '2.3.5. Zona comercial', '2.3.6. Zona Espera', '2.3.7. Asesores y escaleras ', '2.3.8. Entradas y Salidas (Incluyendo emergencias)', '2.3.9. Cuarto Telecomunicaciones', '2.3.10.  Zona medica', '2.3.11.  Seguridad', '2.3.11.1. Policia', '2.3.11.2. Aduana', '2.3.11.3. Camaras', '2.3.11.4. Sistema de Incendio', '2.3.12. Almacen', '2.3.13. Baños', '2.3.14. Sala de empleados', '2.3.15. Diseño de puntos de conexion (toma corriente)', '2.3.16. Sonido ambiental', '2.3.17. Sistema climatizacion', '2.4. Diseño de edificio Vuelos Internacionales', '2.4.1. Bahia de parqueo aviones', '2.4.2. Check in aerolineas', '2.4.3. Zona de llegada', '2.4.4. Zona de salida', '2.4.5. Zona comercial', '2.4.6. Zona Espera', '2.4.7. Asesores y escaleras ', '2.4.8. Entradas y Salidas (Incluyendo emergencias)', '2.4.9. Cuarto Telecomunicaciones', '2.4.10.  Zona medica', '2.4.11.  Seguridad', '2.4.11.1. Policia', '2.4.11.2. Aduana', '2.4.11.3. Camaras', '2.4.11.4. Sistema de Incendio', '2.4.12. Almacen', '2.4.13. Baños', '2.4.14. Sala de empleados', '2.4.15. Diseño de puntos de conexion (toma corriente)', '2.4.16. Sonido ambiental', '2.4.17. Sistema climatizacion', '2.5. Diseño sistema de carga ', '2.6. Diseño Parqueadero', '2.7. Diseño metro', '2.8. Diseño de hangares de aerolineas', '3. Analisis de aplicativos TI', '3.1. Diseño Cableado estructurado', '3.2. Cobertura Wifi', '3.3. Parqueadero Inteligente', '3.4. Energias renovables', '3.5. Nœmero de counter para las aerolineas', '3.6. Almacenamiento CCTV', '3.7. Torre de control', '3.8. Iluminaci—n en pista', '3.9. Diseño App Aeropuerto', '4. Cotizacion ', '4.1. Contrataci—n de RRHH', '4.2. Administraci—n de proveedores', '4.3. Tiempo', '4.3.1. Proyeccion de tiempos de diseño', '4.3.2. Proyeccion de tiempos de Implementaci—n', '4.3.3. Proyeccion de mano de obra', '4.4. Costos Totales', '4.4.1. Costos de materiales', '4.4.2. Costos mano de obra', '4.4.3. Costo de seguros', '5. Ejecucion del diseño Junto a sus aplicativos TI', '5.1. Ejecucion del diseño de pistas de Aterrizaje ', '5.2. Ejecucion del diseño torre de control', '5.3. Ejecucion del diseño de edificio Vuelos nacionales', '5.4. Ejecucion del diseño de edificio Vuelos Internacionales', '5.5. Ejecucion del diseño sistema de carga ', '5.6. Ejecucion del diseño Parqueadero', '5.7. Ejecucion del diseño metro', '5.8. Ejecucion del diseño de hangares de aerolineas', '6. Cierre', '6.1. Pruebas generales', '6.2. Validacion con el cliente', '6.3. Mejora continua']

print(len(b))
print(len(x1))
x2=[4,2,4,121,9,15,58,16,18,23,26,30,31,33,36,38,39,43,40,44,45,46,47,50,51,53,54,58,103,59,65,68,73,75,78,80,81,86,87,103,88,89,92,93,94,95,96,100,101,103,108,110,117,121,137,122,123,124,128,129,130,135,136,137,143,138,141,142,141.3,141.6,142,143,142.3,142.6,143,584,158,205,324,438,448,478,574,584,599,589,594,599]

print(type(b))
print(type(b[0]))
for i in range(0,len(b)):
    x=np.arange(x1[i],x2[i],0.1)
    y=np.full_like(x,-i)
    r=ran.randint(0,255)
    g=ran.randint(0,255)
    b=ran.randint(0,255)
    plt.plot(x,y)
plt.title('Reflexion especular')
plt.xlabel('Distancia')
plt.ylabel('trabajo')    
plt.grid()
#plt.legend()
plt.show()