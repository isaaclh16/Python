'''
FUNCIONES
Ejercicio 1
Crear un programa que tenga una lista, luego 
crear una funcion con la cual se van a pedir numeros 
al usuario para agregar a la lista. Debes crear una 
segunda funcion en donde se ordenen los numeros pares e 
impares dentro de dos listas nuevas
'''
lista = []
num = 0
def pedir():
    i = 0
    while i <=5 :
        num = float(input('Ingresa un numero :' ))
        lista.append(num)
        i+=1
        
def ordenar ():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i %2 == 0:
           pares.append(i) 
        else:
           impares.append(i)
    print(pares)
    print(impares)

pedir()
ordenar()

''' 
Ejercicio 2
Escribir una función que reciba un número entero 
positivo y devuelva su factorial.
'''
def factorial() :
    num = int(input('Ingresar un numero : '))
    if num > 0:
        factorial = 1 
        for i in range(1,num +1) :
            factorial = factorial*i
        print(factorial)
factorial()

'''
FUNCIONES MATEMATICAS
Ejercicio 1
Crear una funcion que pida dos numeros. Si el primero 
es mayor al segundo, el programa debe retornar el 
valor 1; si el segundo es mayor al primero, debe 
retornar -1; si ambos son iguales, debe retornar 0  
'''  
def pida():
    numero1 = int(input('Ingrese el pimer numero : '))
    numero2 = int(input('Ingrese el segundo numero :'))
    if numero1>numero2 :
        return 1
    elif numero2>numero1:
        return -1
    elif numero1 ==numero2:
        return 0
print (pida())


'''
Ejercicio 2
Escribir una función que calcule el total de una 
factura tras aplicarle el IVA. La función debe recibir 
la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función 
sin pasarle el porcentaje de IVA, deberá aplicar un 21% 
'''
def calcule():
    cantidad = float(input('Ingresar la cantidad sin IVA: '))
    porcentaje = int(input('Ingresar el porcentaje: '))
    total = cantidad + (cantidad*(porcentaje/100))
    
    return total

print(calcule())

'''
VARIABLES Y ARGUMENTOS
Ejercicio 1
Crear un programa que tenga dos funciones, una que 
contenga el area de un cuadrado con argumentos de base 
y altura; y la otra el area de un circulo con argumento de radio
'''
def cuadrado(base,altura):
    area = base*altura
    return area
print (cuadrado(10 , 5))

def circulo(radio):
    area = 3.14*(radio**2)
    return area
print (circulo(4))

'''
Ejercicio 2
Escribir una función que reciba una muestra de números 
en una lista y devuelva su medida.
'''
def numeros(*tupla):
    print (len(tupla))
    for i in tupla:
        print(i)
    return len(tupla)
print (numeros(10,2,3,4,5))
    

    
                        