'''Clase 3 de Programación 1
Agenda:
1. Introducción
2. Operadores relacionales
3. Operadores lógicos
4. Condicional
5. Condicional añidado
'''
######################################################################
'''1. Introducción
Hasta aquí hemos visto expresiones que  contienen operadores aritméticos (), %, **, *, +,-.

Hemos ASIGNADO datos a nombres que representan lugares en la memoria de la máquina (las variables) donde se guardan esos valores asignados. Además, estudiamos que estos datos pueden ser de tipo: Enteros, Reales, Caracteres, Booleanos.

En programación vamos a encontrar expresiones más complejas, que utilizan operadores aritméticos pero también incluyen otros tipos de operadores.'''

'''1. Operadores relacionales
Sirven para comparar dos valores y el resultado de la comparación es un dato de tipo Booleano, True o False. El simbolo == es el primer operador relacional (aquí se entiende la razón porque decíamos en la primer clase que el = solo no indicaba una ecuación). Se necesitan dos == para comparar si dos entidades son iguales. Pero existen otros operadores
- Igual: ==
- Diferente: !=
- Mayor: >
- Menor: <
- Mayor igual: >=
- Menor igual: <=

Veamos algunos ejemplos:
'''
# En relación al orden de valores numéricos.
# Igualdad o desigualdad
print(3 == 3.0)
print(3 != 3.0)

# mayor, mayor igual , menor y menor igual
print(5 > 2)
print(5 >= 5.0)

a = 1
b = 2
c = 1

print('Hagamos unas evaluaciones')
print('a es igual a b?: ' + str(a == b))
print('a es igual a c?: ' + str(a == c))
print('a es diferente a b?: ' + str(a != b))
print('a es mayor a b?: ' + str(a > b))

# El uso con los caracteres
# También los podemos usar con el orden ortográfico.
print("a" > "b")
print("b" > "a")

# Pero cuidado!!!  Ese orden no se conserva con las mayúsculas y minúsculas
print("A" == "a")
print("a" > "A")

# También entre cadenas de más de un caracter.

son_iguales = "trapo" == "trapo"
print(son_iguales)

no_son_iguales = "pañuelo" == " pañuelo"
print(no_son_iguales)
######################################################################
'''2. Operadores lógicos
Nos permiten evaluar más de una condición:
- and / &
- or / |
- not / ~
- xor / ^

Estos operadores representan la intersección, la union, el ejemplo del prendido de la luz doble y lo opuesto.
'''

''' El operador "and" es la interseccion, y lo usamos cuando queremos que varias condiciones se cumplan al unisono.'''

dos_verdaderas_and = (5 >= 3) and ("A" < "B")
print(dos_verdaderas_and)  ## True and True --> True

dos_Falsas_and = 5 < 3 and "A" > "B"
print(dos_Falsas_and)  ## False and False   -- > False

una_verdad_una_falsa_and = 5 > 3 and "A" > "B"
print(una_verdad_una_falsa_and)  ## True and False  --> False

'''El operador "or" es la unidad, y lo usamos cuando queremos que por lo menos se cumplan una.'''

dos_verdaderas_or = 5 >= 3 or "A" < "B"
print(dos_verdaderas_or)  ## True and True --> True

dos_Falsas_or = 5 < 3 or "A" > "B"
print(dos_Falsas_or)  ## False and False   -- > False

una_verdad_una_falsa_or = 5 > 3 or "A" > "B"
print(una_verdad_una_falsa_or)  ## True and False  --> True

'''El operador not sirve para obtener el opuesto/negar la expresión analizada'''

como_dice = not True
print(como_dice)

##  OPERACIONES MAS COMPLEJAS

# EJEMPLOS

que_verdad = 2**4 < (23 * 1) and len("cuantasletrashay") > 10
print(que_verdad)

y_este = not (True) == (2 < 1) or 5**2 == 25
print(y_este)

a_que_este_no = not True != (144**(1 / 2) == 12)
print(a_que_este_no)

### pero veamos este

a_que_este_no_seguro = not True != 144**(1 / 2) == 12
print(a_que_este_no_seguro)
# que paso acá


''' Veamos un ejemplo un poco más aplicado:
realizar estudios sociodemográficos es común clasificar a las familias por tipos. Por ejemplo:
- Tipo 1: tamaño == 1, cuartil_ingreso <= 2,  sin hijos
- Tipo 2: tamaño == 1, cuartil_ingreso <= 2,  con hijos
- Tipo 3: tamaño == 1, cuartil_ingreso > 2,  sin hijos
- Tipo 4: tamaño == 1, cuartil_ingreso > 2,  con hijos
- Tipo 5: tamaño > 1, cuartil_ingreso <= 2,  sin hijos
- Tipo 6: tamaño > 1, cuartil_ingreso <= 2,  con hijos
- Tipo 7: tamaño > 1, cuartil_ingreso > 2,  sin hijos
- Tipo 8: tamaño > 1, cuartil_ingreso > 2,  con hijos
'''

# Hogar N1
tam = 5
cuartil_ingreso = 3
hijos = 2

# Probemos si N1 es de tipo 1
print((tam == 1) and (cuartil_ingreso <= 2) and (hijos == 0))
print(tam == 1, cuartil_ingreso <= 2 , hijos == 0)

# Probemos si N1 es de tipo 5
print((tam > 1) and (cuartil_ingreso <= 2) and (hijos == 0))
print((tam > 1) , (cuartil_ingreso <= 2) , (hijos == 0))

# Probemos si N1 es de tipo 8
print((tam > 1) and (cuartil_ingreso > 2) and (hijos > 0))
print((tam > 1) , (cuartil_ingreso > 2) , (hijos > 0))

'''Pero por qué estamos viendo todos estos operadores?
Porque con su uso en interaccion con otros elemetos de la programación podremos tener el CONTROL DE FLUJO del programa.

Dentro de los elementos de control de flujo hoy veremos los CONDICIONALES

La palabra clave para evaluar si se cumple una condición, al igual que en nuestra lengua es el SI escrito en inglés, IF. Y su estructura es:
if condición:
  acción a tomar si la condición es verdadera '''

#evaluar si x es positiva
x = 3
if x > 0:
  print('x es positiva')

'''Otra forma de declaración es usando alternativas, "si..pasa esto ...entonces ....la respuesta será esto otro". Como en python los comando estan programados en inglés, esto deberá ser en inglés, o sea : "if"  en lugar del "si", "else" en lugar de si no.

En otros lenguajes la sentencia que se ejecuta al cumplirse la condicion debe estar entre llaves por ejemplo. Python es tan similar al idioma que utiliza los dos puntos:. La estructura de un condicional en Python es la siguiente:
if (condicion):
  acción a tomar si la condición es verdadera
else:
  acción a tomar si la condición es false
'''
# Un ejemplo clásico. Decidir si un número es par o impar.

num = int(inEjercicio de clase:put("Ingrese un numero: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("Es un número impar")

'''También podemos generar un flujo con más de 2 opciones posibles, lo que se conoce como condiciones encadenadas. Para esto se utiliza una nueva palabra clave "elif" que es una abreviatura de "else if" y quiere decir  "si no, si" y nos permite encadenar otras posibilidades del condicionamiento del flujo.'''

edad = int(input("Ingrese la edad del individuo: "))

if edad <= 12:
    print("Es un niña/o")
elif edad < 18:
    print("Es una persona joven, menor de edad")
elif edad <= 65:
    print("Es un adulto, posiblemente en actividad")
else:
    print("Es persona eque puede optar por el retiro.")

# Pero... elif que diferencia tiene de usar más if secuencialmente......
if edad <= 12:
    print("Es un niña/o")
if (edad > 12) and (edad < 18):
    print("Es una persona joven, menor de edad")
if edad >= 18 and edad <= 65:
    print("Es un adulto, posiblemente en actividad")
else:
    print("Es persona eque puede optar por el retiro.")

'''Los flujos condicionales pueden estar ANIDADOS
Retomemos el ejemplo de Arabia Saudí y Argentina.
Podemos usar condicional para hacer un poco más complejo el programa y más directa la salida.'''

intensidad = int(input(" 2 si es de Arabia y 30 si es de Argentina:   "))
equipo = input("Ingrese el equipo que hizo el gol, VAR si fue fuera de juego")
# ASIGNAMOS el gol.
gol = "G" + intensidad * "0" + "L!"

# ASIGNAMOS los complementos del relato según selección.
Arabia = " de la selección Saudí que sorprende a la escuadra Argentina"
Argentina = " de la Scaloneta que arranca con todo en Qatar 2022"

# Utilicemos, entonces  condicionales
if intensidad:
    gol = "G" + intensidad * "0" + "L!"
    if equipo == "Argentina":
        relato = (gol + Argentina)
        print(relato)
    elif equipo:
        relato = (gol + Arabia)
        print(relato)
    else:
        print(gol + "...NO, el arbitro lo anulo por el VAR")

'''Ejercicio de clase:
Escribir un programa que dados el tamaño, el cuartil de ingresos y la cantidad de hijos que tiene un hogar, devuelva el tipo de hogar según lo mostrado arriba.'''

'''Bibliografía:
- Downey, A. 2016. "Think Python, How to think like a computer scientist". Publicado por O'Reilly '''
