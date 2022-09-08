
'''
FOR
Ejercicio 1
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al 
usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
for i in range(1,11) :
    print (i)
numero1 = int(input('Ingrese el primer numero : ' ))
numero2 = int(input('Ingrese el primer numero : ' ))

for j in range(numero1,numero2 = 1) :
    print (j)

'''
Ejercicio 2
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar 
el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''
numero1 = int(input('Ingrese el primer numero : ' ))
numero2 = int(input('Ingrese el primer numero : ' ))
for j in range(numero1,numero2) :
    if j %2 != 0 :
        print(j)
 
''' 
Ejercicio 3
Escribir un programa que pida un numero al usuario 
y muestre las tablas de multiplicar de ese numero
''' 
numero = int (input('Ingrese un numero : ')) 

i = 0 
while i <= 12 :
    i += 1
    print ("la tabla es {}".format(numero*i))
 
''' 
WHILE  
Ejercicio 4
Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
edad = int (input('Cual es su edad : '))
i = 1 
while i < 29 :
    print ("Has cumplido :  {}".format(i))
    i += 1
