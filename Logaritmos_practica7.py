# Jose Alfredo Perez Lopez
# Los datos iniciales
distancias = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
tiempos = [0.4533, 0.43, 0.4025, 0.38, 0.35, 0.32, 0.28, 0.25, 0.2, 0.136]
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
y = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
x = [0.4533, 0.43, 0.4025, 0.38, 0.35, 0.32, 0.28, 0.25, 0.2, 0.136]

import math

# Obtiene el logaritmo natural de las 2 listas
log_tiempos = [math.log(i) for i in x]
log_distancias = [math.log(j) for j in y]

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
del xy[1:11]
del xy[2:12]
del xy[3:13]
del xy[4:14]
del xy[5:15]
del xy[6:16]
del xy[7:17]
del xy[8:18]
del xy[9:19]
del xy[10:20]

print('\tEl logaritmo natural de los tiempos multiplicado por el logaritmo natural de las distancias:')
print(xy)

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
print('m = ' + str(m))
n = m
a = math.exp(b)
print('a = ' + str(a))
print('n = ' + str(n))


t = eval(input('Cual es el tiempo?'))
distancia = a*t**n
print('La altura obtenida es: ' + str(distancia))