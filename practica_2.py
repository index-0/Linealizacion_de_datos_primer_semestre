# Jose Alfredo Perez Lopez
# Los datos iniciales

import math

x1 = 10
x2 = 30
x3 = 50
x4 = 70
x5 = 100
x6 = 120
x7 = 140
y1 = 0.0000000268
y2 = 0.00000000296
y3 = 0.00000000106
y4 = 0.000000000544
y5 = 0.000000000266
y6 = 0.000000000185
y7 = 0.000000000136

x = [x1, x2, x3, x4, x5, x6, x7]
y = [y1, y2, y3, y4, y5, y6, y7]

# Numero de datos
num_datos_x = len(x)
num_datos_y = len(y)
num_datos = (num_datos_x + num_datos_y)/2

# Imprime los datos obtenidos
print('\tLos datos obtenidos fueron los siguientes:')

print("Los numeros de datos en la lista 'x' = " + str(num_datos_x))
print("Los numeros de datos en la lista 'y' = " + str(num_datos_y))
print("Por lo tanto lso numeros de datos son = " + str(num_datos))

print('Los "x" obtenidas;')
print(x)

print('Las "y" obtenidas;')
print(y)

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
del log_xy[1:8]
del log_xy[2:9]
del log_xy[3:10]
del log_xy[4:11]
del log_xy[5:12]
del log_xy[6:13]

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
    loop = True

    while loop == True:

        xx = eval(input('Inserte algun valor de "x".'))
        yy = a * xx ** n
        print(str(a) + "*" + str(xx) + "**" + str(n))
        print('La "y" obtenida es: ' + str(yy))

        loop = input("Para finalizar escriba exit:")
        if xx == "exit":
            loop = False
        else:
            loop = True
    quit("Programa finalizado con exito.")

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
    loop = True

    while loop == True:

        yy = eval(input('Inserte algun valor de "y".'))
        xx = a * yy ** n
        print(str(a) + "*" + str(yy) + "**" + str(n))
        print('La "x" obtenida es: ' + str(xx))

        loop = input("Para finalizar escriba exit:")
        if xx == "exit":
            loop = False
        else:
            loop = True
    quit("Programa finalizado con exito.")

else:
    quit('Intente de nuevo e inserte un valor valido que sea "x" o "y".')
