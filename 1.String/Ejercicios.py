
'''Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''

cadena = 'Te quiero solo como amigo'

print (cadena[ 0:2])
print (cadena[ -3:])
print (cadena[::2]) # : Dice saque una copia y imprimes cada 2 los caracteres 
print (cadena [::-1])# : Dice saque una copia y imprime cada 1 desde atras 
print (cadena , cadena [::-1])



'''Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y 
un carácter de coma (,); e inserte el carácter entre cada letra de la 
cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r 
'''

palabra = 'eparado'
print (palabra)
reemplazar = palabra.replace('',',')
print ('S',reemplazar)