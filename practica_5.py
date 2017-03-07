# Jose Alfredo Perez Lopez
# Los datos iniciales

import math
import matplotlib.pyplot as plt
import numpy

print("Para finalizar el codigo inserte 'q' en cualquier dato de entrada.")

x1 = 0.1
x2 = 0.2
x3 = 0.3
x4 = 0.4
x5 = 0.5
x6 = 0.6
x7 = 0.7
x8 = 0.8
x9 = 0.9
x10 = 1
y1 = 0.7805
y2 = 1.099
y3 = 1.3265
y4 = 1.51775
y5 = 1.7185
y6 = 1.8835
y7 = 2.048
y8 = 2.18775
y9 = 2.32175
y10 = 2.44975

x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]

# Numero de datos
num_datos_x = len(x)
num_datos_y = len(y)
num_datos = (num_datos_x + num_datos_y)/2

# Imprime los datos obtenidos
print('\tLos datos obtenidos fueron los siguientes:')

print("Los numeros de datos en la lista 'x' = " + str(num_datos_x))
print("Los numeros de datos en la lista 'y' = " + str(num_datos_y))
print("Por lo tanto lso numeros de datos son = " + str(num_datos))

print('Los "x" insertadas;')
print(x)

print('Las "y" insertadas;')
print(y)

# Grafica
grafica = input('Quiere visualizar la grafica de los datos insertados?(y/n)')
if grafica == 'y':
    plt.plot(x,y)
    plt.xlabel('Distancia (m)')
    plt.ylabel('Tiempo (s)')
    plt.plot(x,y,'co')
    plt.title('Grafica')
    plt.show()
elif grafica == 'q':
    quit('Programa finalizado')

# Obtiene el logaritmo natural de las 2 listas
log_x = [math.log(i) for i in x]
log_y = [math.log(j) for j in y]

# Imprime los datos obtenidos sobre los logaritmos
print('\tLos logaritmos de los datos obtenidos son los siguientes:')

print('Los logaritmos naturales de "x" son;')
print(log_x)

print('Los logaritmos naturales de "y" son;')
print(log_y)

# Multiplica el logaritmo natural del tiempo por el logaritmo natural de la distancia
log_xy = []

for i in log_x:
    for j in log_y:
        log_xy.append(i * j)
del log_xy[1:11]
del log_xy[2:12]
del log_xy[3:13]
del log_xy[4:14]
del log_xy[5:15]
del log_xy[6:16]
del log_xy[7:17]
del log_xy[8:18]
del log_xy[9:19]


print('\tEl logaritmo natural de "x" por el logaritmo natural de "y" es igual a:')
print(log_xy)

# La suma de cada una de las listas

# Suma los logaritmos de x
suma_log_x = sum(log_x)
print('La suma de los logaritmos de "x" es:')
print(suma_log_x)

# Suma los logaritmos de y

suma_log_y = sum(log_y)
print('La suma de los logaritmos de "y" es:')
print(suma_log_y)

# Suma la multiplicacion de los logaritmos de "x" por los logaritmos de "y"

suma_log_xy = sum(log_xy)
print('La suma de la multiplicacion de los logaritmos del tiempo por los logaritmos de la distancia:')
print(suma_log_xy)

# El cuadrado de cada termino de la lista y su respectiva suma

x_o_y = input("\tQuiere usar x(inserte 'x' sin comillas) o y(inserte 'y' sin comillas); si inserta x en la ecuacion linealizada obtendra 'y' y viceversa.")

# Funcion que se usara despues para graficar la ecuacion resultante
def draw_l_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Distancia (m)')
    plt.ylabel('Tiempo (s)')
    plt.title('Grafica del fenomeno')
    plt.show()

if x_o_y == "x":
    log_x_cuadrado = [n ** 2 for n in log_x]
    print("El cuadrado de los logaritmos de 'x' es:")
    print(log_x_cuadrado)

    # Es la suma de los logaritmos de "x" al cuadrado

    suma_log_x_cuadrado = sum(log_x_cuadrado)
    print('La suma de los logaritmos de "x" al cuadrado es:')
    print(suma_log_x_cuadrado)

    # Pendiente
    m = (num_datos * suma_log_xy - suma_log_x * suma_log_y) / (
         num_datos * suma_log_x_cuadrado - suma_log_x ** 2)
    print('La pendiente es igual a:')
    print('m = ' + str(m))

    # Interseccion con eje y
    b = (suma_log_x_cuadrado * suma_log_y - suma_log_x * suma_log_xy) / (
         num_datos * suma_log_x_cuadrado - suma_log_x ** 2)
    print('La interseccion con el eje y es:')
    print('b = ' + str(b))

    n = m
    a = math.exp(b)
    print('El exponente de la ecuacion es (n): ' + str(n))
    print('a = ' + str(a))

    grafica = input('Quiere graficar la ecuacion obtenida? (y/n)')
    if grafica == 'y':
        val_p = input('Desea insertar valores personalizados?(y/n)')
        if val_p == 'y':
            rango_xi = eval(input('Inserte el valor inicial de "x"'))
            rango_xf = eval(input('Inserte el valor final de "x"'))
            delta_x = eval(input('Inserte la diferencia de distancia entre puntos para el eje "x"'))
            x = numpy.arange(rango_xi, rango_xf, delta_x)
            y = []
        elif grafica == 'q':
            quit('Programa finalizado')
        else:
            x = numpy.arange(0, x10, 0.001)
            y = []
        for d in x:
            tiempo = a * d ** n
            y.append(tiempo)
        draw_l_graph(x, y)
    elif grafica == 'q':
            quit('Programa finalizado')

    loop = True
    while loop == True:

        xx = eval(input('\nInserte algun valor de "x".'))
        yy = a * xx ** n
        print("\n" + str(a) + "*" + str(xx) + "**" + str(n))
        print('La "y" obtenida es: ' + str(yy))

elif x_o_y == "y":
    log_y_cuadrado = [n ** 2 for n in log_y]
    print("El cuadrado de los logaritmos de 'y' es:")
    print(log_y_cuadrado)

    # Es la suma de los logaritmos de "y" al cuadrado

    suma_log_y_cuadrado = sum(log_y_cuadrado)
    print('La suma de los logaritmos de "y" al cuadrado es:')
    print(suma_log_y_cuadrado)

    # Pendiente
    m = (num_datos * suma_log_xy - suma_log_y * suma_log_x) / (
    num_datos * suma_log_y_cuadrado - suma_log_y ** 2)
    print('La pendiente es igual a:')
    print('m = ' + str(m))

    # Interseccion con eje y
    b = (suma_log_y_cuadrado * suma_log_x - suma_log_y * suma_log_xy) / (
    num_datos * suma_log_y_cuadrado - suma_log_y ** 2)
    print('La interseccion con el eje y es:')
    print('b = ' + str(b))

    n = m
    a = math.exp(b)
    print('El exponente de la ecuacion es (n): ' + str(n))
    print('a = ' + str(a))

    grafica = input('Quiere graficar la ecuacion obtenida? (y/n)')
    if grafica == 'y':
        val_p = input('Desea insertar valores personalizados?(y/n)')
        if val_p == 'y':
            rango_yi = eval(input('Inserte el valor inicial de "y"'))
            rango_yf = eval(input('Inserte el valor final de "y"'))
            delta_y = eval(input('Inserte la diferencia de distancia entre puntos para el eje "y"'))
            y = numpy.arange(rango_yi, rango_yf, delta_y)
            x = []
        elif val_p == 'q':
            quit('Programa finalizado')
        else:
            y = numpy.arange(0, y10, 0.001)
            x = []
        for t in y:
            distancia = a * t ** n
            x.append(distancia)
        draw_l_graph(x, y)
    elif grafica == 'q':
        quit('Programa finalizado')
    loop = True
    while loop == True:

        yy = eval(input('\nInserte algun valor de "y".'))
        xx = a * yy ** n
        print(str(a) + "*" + str(yy) + "**" + str(n))
        print('La "x" obtenida es: ' + str(xx))

elif x_o_y == 'q':
    quit('Programa finalizado')

else:
    quit('Intente de nuevo e inserte un valor valido que sea "x" o "y".')
