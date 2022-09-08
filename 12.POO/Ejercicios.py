'''
Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que 
tenga como atributos el nombre y la nota del alumno. Definir los métodos 
para inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
resultado de la nota y si ha aprobado o no.
'''
class Estudiante ():
    def __init__(self,nombre ,nota):
        self.nombre = nombre 
        self.nota = nota 
    def imprimir (self):
        print('Nombre: :{} \nNota :{}'.format(self.nombre, self.nota))
    def resultados (self):
        if self.nota > 7 :
            print ('APROBADO')
        else :
            print ('DESAPROBADO')

estudiante1 = Estudiante('Isaac', 10)
estudiante1.imprimir()
estudiante1.resultados()

'''
Ejercicio 2
Realizar un programa en el cual se declaren dos valores enteros 
por teclado utilizando el método __init__. Calcular después 
la suma, resta, multiplicación y división. Utilizar un método 
para cada una e imprimir los resultados obtenidos. Llamar a la 
clase Calculadora.
'''
class Calculadora ():
    def __init__ (self ):
        self.num1 = int (input ('Ingrese el primer numero '))
        self.num2 = int (input('Ingrese el segundo numero '))
    def suma(self ):
        self.suma = self.num1 + self.num2
        return 'La suma da como resultado:', self.suma 
    def resta(self):
        self.resta = self.num1 - self.num2
        return 'La resta da como resultado:', self.resta 
    def division(self):
        self.division = self.num1 / self.num2
        return 'La division da como resultado:', self.division
calcular = Calculadora()
print(calcular.suma())
print(calcular.resta())
print(calcular.division())

'''
Ejercicio 3
Crear una clase Fabrica que tenga los atributos de Llantas, Color 
y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales 
son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color 
y precio de ambos transportes. Por ultimo, crear objetos para cada 
clase y mostrar por pantalla los atributos de cada uno. 
'''
class Fabrica ():
    def __init__(self,Llantas,Color,Precio):
        self.Llantas = Llantas
        self.Color = Color
        self.Precio = Precio
class Moto (Fabrica):
    def datos(self):
        print('La cantidad de llantas es de :', self.Llantas)
        print('El color es  :', self.Color)
        print('El precio  es de :', self.Precio)
    
class Carro(Fabrica):
    def datos(self):
        print('La cantidad de llantas de la moto es de :', self.Llantas)
        print('El color de la moto es  :', self.Color)
        print('El precio de la moto es de :', self.Precio)
        
moto = Moto(3,'Rojo',3000)
moto.datos()

carro = Carro(4,'Verde',4000)
carro.datos()

''' 
Ejercicio 4
Crear una clase llamada Marino(), con un metodo que 
sea hablar, en donde muestre un mensaje que diga "Hola...". 
Luego, crear una clase Pulpo() que herede Marino, pero modificar 
el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una 
clase Foca(), heredada de Marino, pero que tenga un atributo nuevo 
llamado mensaje y que muestre ese mesjae como parametro
'''
class Marino():
    def hablar(self):
        print("Hola...")

class Pulpo(Marino):
    def hablar(self):
        print("Soy un pulpo")

class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca")

'''
Ejercicio 5
Crear un programa con tres clases Universidad, con 
atributos nombre (Donde se almacena el nombre de la 
Universidad). Otra llamada Carerra, con los atributos 
especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre 
y edad. El programa debe imprimir la especialidad, edad, nombre y universidad 
de dicho estudiante con un objeto llamado persona.
'''

class Universidad ():
    def __init__(self,Nombre):
      self.Nombre = Nombre
class Carrera ():
    def carrera(self,especialidad ):                                                                                                          
      self.especialidad = especialidad
    
class Estudiante (Universidad,Carrera):
    def datos(self,nombre,edad):
      self.nombre = nombre
      self.edad = edad
      print('Mi nombre es {},tengo{} años , mi especialidad es {},Estudio en la Universidad {}'.format(self.nombre,self.edad,self.especialidad,self.Nombre))

persona = Estudiante('SanMarcos')
persona.carrera('Sistemas')
persona.datos('Isaac',20)    
