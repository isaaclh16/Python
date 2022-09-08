'''
Ejercicio 1

Realizar un programa que haga el proceso de formula general 
para la resolución de ecuaciones, sabiendo que la formula 
general es la que está en la imagen, el usuario debe ingresar 
los valores de “a”, “b” y “c”, y el programa debe hacer el 
proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''

nombre = input('Ingresa tu nombre:')
edad = float(input("Ingresa tu edad:"))

print(nombre)
print(edad)

a = float(input ('Ingrese el valor de a :'))
b = float(input('Ingrese el valor de b :'))
c = float(input('Ingrese el valor de c :'))
x1 = (-b + (((b**2) - (4*a*c))**0.5))/(2*a)
x2 = (-b - (((b**2) - (4*a*c))**0.5))/(2*a)

print (a,b,c)
print ('El valor de X1 es: ')
print (x1)
print ('El valor de X2 es: ')
print (x2)

'''Ejercicio 2 

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.
Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final
'''

P1 = float(input('Ingrese el valor de P1 :'))
P2 = float(input('Ingrese el valor de P2 :'))
P3 = float(input('Ingrese el valor de P3 :'))
EP = float(input('Ingrese el valor de EP :'))
EF = float(input('Ingrese el valor de EF :'))
PP = (P1+P2+P3)
PROM = ( PP + 2*EP + 3*EF ) / 6

print (P1,P2,P3,EP,EF)
print ('El valor de PROM es: ')
print (PROM)

