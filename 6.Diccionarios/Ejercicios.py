'''
Ejercicio 1

En el siguiente diccionario se encuentran capitales 
de los paises en el mundo, debes realizar un programa 
que pida un pais al usuario, y muestre la capital de 
ese pais, en dado caso el pais no este en el 
diccionario, se debe mostrar un mensaje diciendo 
que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San 
Salvador", "Honduras": "Honduras","Nicaragua": "Managua", 
"Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''
 #Codigo
diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", 
"Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input('Debe ingresar un pais : ')

if  diccionario.get(pais): 
    print(diccionario.get(pais))

else :
    print('Este pais no se encuentra')

'''
Ejercicio 2

Con el siguiente diccionario, debes crear un programa que pregunte 
al usuario por un número; el programa debe imprimir el jugador 
al que hace referencia ese número
{
    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}
'''

diccionario = {
    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"

}
numero = int(input ('Ingresar un numero : '))
diccionario.get(numero) 
print(diccionario.get(numero))