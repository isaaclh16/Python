'''
Ejercicio 1
Crear un programa que pida al usuario una letra, y si 
es vocal, muestre el mensaje "Es vocal". Sino, decirle 
al usuario que no es vocal
'''
palabra = input ('Ingrese una letra : ')

if palabra == 'a' or  palabra == 'e' or palabra == 'i' or palabra == 'o' or palabra == 'u' :
   print ('La letra es vocal')
else:
   print ('No es vocal')
   
'''
Ejercicio 2
Escribir un programa que, dado un número entero, muestre 
su valor absoluto. Nota: para los números positivos su valor 
absoluto es igual al número (el valor absoluto de 52 
es 52), mientras que, para los negativos, su valor absoluto 
es el número multiplicado por -1 (el valor absoluto de -52 es 52).
'''
# Primera Forma 
numero = int(input ('Ingrese un numero : '))
if numero > 0  :
   print ('El numero es ' , numero  )
elif numero < 0 :
     numero = numero*-1
     print ('El numero es ', numero )
else :
    print ('No es entero ')
    
#Segunda Forma pero solo se cambia el numero *-1 por el metodo abs que calcula el valor absoluto

numero = int(input ('Ingrese un numero : '))
if numero > 0  :
   print ('El numero es ' , numero  )
elif numero < 0 :
     numero = abs (numero)
     print ('El numero es ', numero )
else :
    print ('No es entero ')
    

'''
Ejercicio 3
Escribe un programa que pida dos palabras y diga si 
riman o no. Si coinciden las tres últimas letras tiene que 
decir que riman. Si coinciden sólo las dos últimas tiene 
que decir que riman un poco y si no, que no riman.
'''
palabra1 = input('Ingrese la primera palabra : ')
palabra2 = input('Ingrese la segunda palabra : ')

if palabra1 [ -3: ] == palabra2 [ -3:] :
    print ('Las palabras riman ')

elif palabra1 [ -2:] == palabra2 [ -2:] :
    print ('Las palabras riman un poco')

else :
    print ('las palabras no riman ')
 
'''
Ejercicio 4
Crear un programa que permita al usuario elegir un candidato 
por el cual votar. Las posibilidades son: candidato A por el 
partido rojo, candidato B por el partido verde, candidato C 
por el partido azul. Según el candidato elegido (A, B ó C) se 
le debe imprimir el mensaje “Usted ha votado por el partido [color 
que corresponda al candidato elegido]”. Si el usuario ingresa 
una opción que no corresponde a ninguno de los candidatos 
disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el 
programa debe convertirla en mayúscula
'''
candidato = input('Ingrese la letra A,B o C que represent a lo candidatos : ')

if candidato.upper() == 'A' :
    print("Usted ha votado por el partido rojo")
elif candidato.upper() == 'B' :
    print("Usted ha votado por el partido verde")
elif candidato.upper() == 'C' :
    print('Usted ha votado por el partido azul')
else:
    print("Usted no ha elegido bien a su candidato")

