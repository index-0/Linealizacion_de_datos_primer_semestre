# Jose Alfredo Perez Lopez
# Los datos iniciales
tiempos = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4]
distancias = [0,0.4333,1.2666,2.35,4.05,6.3333,9.0133,11.85,14.6,18.6166,23.06666,27.9666,33.3666,39.25,45.4333,53.29,
              60.4,66.3,73.85,81.6333,89.5333]
num_datos_tiempos = len(tiempos)
num_datos_distancias = len(distancias)
num_datos = (num_datos_distancias + num_datos_tiempos)/2

# Imprime los datos obtenidos
print('\tLos datos obtenidos fueron los siguientes:')

print("Los numeros de datos en la lista del tiempo son = " + str(num_datos_tiempos))
print("Los numeros de datos en la lista de la distancia son = " + str(num_datos_distancias))
print("Por lo tanto lso numeros de datos son = " + str(num_datos))

print('Los tiempos obtenidos fueron;')
print(tiempos)

print('Las distancias obtenidas fueron;')
print(distancias)
# Remueve el numero 0 porque si no el logaritmo natural de la lista muestra un error
x = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4]
y = [0.4333,1.2666,2.35,4.05,6.3333,9.0133,11.85,14.6,18.6166,23.06666,27.9666,33.3666,39.25,45.4333,53.29,
              60.4,66.3,73.85,81.6333,89.5333]

import math

# Obtiene el logaritmo natural de las 2 listas
log_tiempos = [math.log(i) for i in x]
log_distancias = [math.log(j) for j in y]

# Agrega el 0 al inicio de la lista
log_tiempos.insert(0,0)
log_distancias.insert(0,0)
# Imprime los datos obtenidos sobre los logaritmos
print('\tLos logaritmos de los datos obtenidos son los siguientes:')

print('Los logaritmos naturales del tiempo son;')
print(log_tiempos)
print('Los logaritmos naturales de la distancia son;')
print(log_distancias)

# Multiplica el logaritmo natural del tiempo por el logaritmo natural de la distancia
xy = []

for i in log_tiempos:
    for j in log_distancias:
        xy.append(i * j)
del xy[1:22]
del xy[2:23]
del xy[3:24]
del xy[4:25]
del xy[5:26]
del xy[6:27]
del xy[7:28]
del xy[8:29]
del xy[9:30]
del xy[10:31]
del xy[11:32]
del xy[12:33]
del xy[13:34]
del xy[14:35]
del xy[15:36]
del xy[16:37]
del xy[17:38]
del xy[18:39]
del xy[19:40]
del xy[20:41]

print('\tEl logaritmo natural de los tiempos multiplicado por el logaritmo natural de las distancias:')
print(xy)

x_entre_y = []
for j in x:
    for i in y:
        x_entre_y.append(i / j)

del x_entre_y[1:21]
del x_entre_y[2:22]
del x_entre_y[3:23]
del x_entre_y[4:24]
del x_entre_y[5:25]
del x_entre_y[6:26]
del x_entre_y[7:27]
del x_entre_y[8:28]
del x_entre_y[9:29]
del x_entre_y[10:30]
del x_entre_y[11:31]
del x_entre_y[12:32]
del x_entre_y[13:33]
del x_entre_y[14:34]
del x_entre_y[15:35]
del x_entre_y[16:36]
del x_entre_y[17:37]
del x_entre_y[18:38]
del x_entre_y[19:39]
del x_entre_y[20:40]
del x_entre_y[21:41]


x_entre_y.insert(0, 0)
print("La velocidad es igual a: ")
print(x_entre_y)

# El cuadrado de cada termino de la lista
log_tiempo_cuadrado = [n**2 for n in log_tiempos]

print('El cuadrado del los logaritmos del tiempo:')
print(log_tiempo_cuadrado)

# La suma de cada una de las listas

suma_log_tiempo = sum(log_tiempos)
print('La suma de los logaritmos de los tiempos es:')
print(suma_log_tiempo)

suma_log_distancia = sum(log_distancias)
print('La suma de los logaritmos de las distancias es:')
print(suma_log_distancia)

suma_log_tiempo_cuadrado = sum(log_tiempo_cuadrado)
print('La suma de los logaritmos de los tiempos al cuadrado es:')
print(suma_log_tiempo_cuadrado)

suma_log_tiempo_por_distancia = sum(xy)
print('La suma de la multiplicacion de los logaritmos del tiempo por los logaritmos de la distancia:')
print(suma_log_tiempo_por_distancia)

# las formulas de las funciones lineales

m = (num_datos * suma_log_tiempo_por_distancia - suma_log_tiempo * suma_log_distancia)/(num_datos * suma_log_tiempo_cuadrado - suma_log_tiempo**2)
print('La pendiente es igual a:')
print('m = ' + str(m))

b = (suma_log_tiempo_cuadrado * suma_log_distancia - suma_log_tiempo * suma_log_tiempo_por_distancia)/(num_datos * suma_log_tiempo_cuadrado - suma_log_tiempo**2)
print('La intercepcion con el eje y es:')
print('b = ' + str(b))

n = m
a = math.exp(b)
print('El exponente de la ecuacion es: ' + str(n))
print('a = ' + str(a))
t = eval(input('Cual es el tiempo?'))
distancia = a*t**n
print('La distancia obtenida es: ' + str(distancia))
