'''
Ejercicio 1
Escribir una tupla con los meses del año, luego, pide al usuario 
un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''
#Codigo
tupla = ('enero','febrero','marzo','abril','mayo','junio','julio','agosto',
         'setiembre','octubre','noviembre','diciembre')
numero = int (input('Ingrese un numero del 0 al 11 : ' ))
if numero == 0 :
     print(tupla[0])
elif numero == 1 :
     print(tupla[1])
elif numero == 2 :
     print(tupla[2])
elif numero == 3 :
     print(tupla[3])     
elif numero == 4 :
     print(tupla[4])
elif numero == 5 :
     print(tupla[5])
elif numero == 6 :
     print(tupla[6])
elif numero == 7 :
     print(tupla[7])
elif numero == 8 :
     print(tupla[8])
elif numero == 9 :
     print(tupla[9])
elif numero == 10 :
     print(tupla[10])
elif numero == 11 :
     print(tupla[11])
else :
    print('No se ingreso el numero adecuado')
    
'''
Ejercicio 2
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir 
al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa '''

tupla = ('a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q',
         'r','s','t','u','v',
         'w','x','y','z')
numero = int (input('Ingrese un numero del 0 al 25 : ' ))
if numero == 0 :
     print(tupla[0])
elif numero == 1 :
     print(tupla[1])
elif numero == 2 :
     print(tupla[2])
elif numero == 3 :
     print(tupla[3])     
elif numero == 4 :
     print(tupla[4])
elif numero == 5 :
     print(tupla[5])
elif numero == 6 :
     print(tupla[6])
elif numero == 7 :
     print(tupla[7])
elif numero == 8 :
     print(tupla[8])
elif numero == 9 :
     print(tupla[9])
elif numero == 10 :
     print(tupla[10])
elif numero == 11 :
     print(tupla[11])
elif numero == 12 :
     print(tupla[12])
elif numero == 13 :
     print(tupla[13])
elif numero == 14 :
     print(tupla[14])     
elif numero == 15 :
     print(tupla[15])
elif numero == 16 :
     print(tupla[16])
elif numero == 17 :
     print(tupla[17])
elif numero == 18 :
     print(tupla[18])
elif numero == 19 :
     print(tupla[19])
elif numero == 20 :
     print(tupla[20])
elif numero == 21 :
     print(tupla[21])
elif numero == 22 :
     print(tupla[22])
elif numero == 23 :
     print(tupla[23])
elif numero == 24 :
     print(tupla[24])
elif numero == 25 :
     print(tupla[25])
else :
    print('No se ingreso el numero adecuado')
    
# Otra forma de resolverlo 
tupla = ('enero' , 'febrero' , 'marzo' , 'abril' , 'mayo' , 'junio' , 'julio' , 'agosto' , 'septiembre' , 'octubre' , 'noviembre' , 'diciembre')
OpcionMes = int(input("Ingresa el numero de tu mes: "))
print("El mes correspondiente es: ", tupla[OpcionMes-1])


   
  