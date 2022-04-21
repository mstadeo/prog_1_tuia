'''Clase 5
Agenda:
* `for` statement
* range()
* `while` statement
'''

'''
### Sentencia for
De la documentación de python
https://docs.python.org/es/3/tutorial/controlflow.html#for-statements
> La sentencia for de Python itera sobre los ítems de cualquier secuencia (una lista o una cadena de texto), en el orden que aparecen en la secuencia. Por ejemplo:
'''
palabras = ['gato', 'ventana', 'perro']
for palabra in palabras:
    print(palabra, len(palabra))

'''El objecto `palabras` es una lista, un objeto que aún no estudiamos. Por ahora pensemos en las listas como objetos que nos permiten guardar otros objetos dentro.
En el código de arriba estamos usando el `for` para ir accediendo a cada una de las cadenas que están guardadas dentro de la lista `palabras`.
Luego, cuando pudimos acceder a la `palabra`, la imprimimos y medimos su longitud con la función len() '''

'''
### Formato general
for `elemento` in `objeto`:
    acciones a realizar en cada iteración:
    acción 1
    acción 2
    ...
    acción n

Pero, que significa iterar?
En cada loop/vuelta python le va a asignar a la variable `elemento` uno a uno los objetos dentro de `objeto`.
Luego, realizará el conjunto/bloque de acciones (identadas) dentro del for con esa variable elemento
'''


'''
### Función range
De la documentación de python:
https://docs.python.org/es/3/tutorial/controlflow.html#the-range-function
Cuando se necesita iterar sobre una secuencia de números, es atinado usar la funcion integrada range.
La estructura de range es:
range(inicio, fin, step)
los parámetros inicio y step son opcionales.

'''
for i in range(5):
    print(5)

'''
Por qué solo imprime hasta el número 5?
'''

for i in range(5, 9):
    print(i)

for i in range(1, 10, 2):
    print(i)

"""
### Contadores
En el control de flujo que se logra a través de las iteraciones en un bucle, muchas veces es necesario el uso de "contadores".
Estos elementos son una variable a la que se le asigna un valor inicial (comúnmente  0 ) y se incrementa su valor con cada recorrido con el código interno del bucle

un ejemplo de uso de un contador puede ser
"""
cont = 0
for i in range(10):
     count = count + 1
# (esto incrementará el valor de la varaible "count" en 1 cada vuelta)

"""
#### Operadores de asignación
Es importante tener en cuenta que muchas veces encontraremos
count += 1

esta declaracion reducida es equivalente a:
count = count + 1

La misma notación puede aplicarse con otros operadores aritmético

EJEMPLOS DE USO
- count -= 1  restara 1 cada iteración
- count *= 2  duplicará el valor cada iteración
- count / 2  divirá por dos el valor cada iteración
- count ** 2  elevará al cuadrado el valor cada iteración

"""

'''
Ejercicio de clase para hacer entre todos en el pizarrón
Usando la lista de cadenas de abajo, generar una frase e imprimirla.
palabras = ['La', 'fceia', 'es', 'la', 'facultad', 'de', 'ciencias', 'exactas', 'ingeniería', 'y', 'agrimensura']
Pistas:
* entre las palabras debería haber un espacio
* la concatenación de cadenas se logra con el operador +
* definir una variable `frase` a la que adicionar las palaras
'''

"""
### Uso del primer objeto iterable (cadena)

En clases anteriores vimos que existian objetos que no eran unidimensionales. Mensionamos que el primero que veríamos es la CADENA.
Sobre estos objetos es posible "iterar" por cada uno de sus elementos. En el caso de la cadena sus elementos interiores son CARACTERES.
Así pordríamos generar un bucle que repita el mismo flujo de codigo sobre cada uno de los caracteres.

El ejemplo básico:

"Contar cuantas letras tiene una cadena" (esto lo hace como vimos la funciòn len())"
"""

palabra = "rio"
count = 0
for i in palabra:
  count += 1
print("la palabra tiene: ", count, " letras")


'''
### Sentencia while
De la documentación de python:
https://docs.python.org/es/3/reference/compound_stmts.html#the-while-statement

La sentencia while se usa para la ejecución repetida siempre que una expresión sea verdadera
'''
target = 3
ingreso = int(input('introduzca un número entre 0 y 10: '))
while ingreso != target:
    ingreso = int(input('introduzca un número entre 0 y 10: '))
print('Ganaste!!!')

'''
Analicemos lo que paso arriba:
1. Definimos una variable que se llama target. Target sería como el número que una persona piensa para que otra adivine
2. Le pedimos a la persona que ingrese un número, `ingreso`
3. Evaluamos si el número ingresado es diferente a `target`. Si esto es así, ejecuto las acciones dentro de `while`, que están identadas
4. Vuelvo a preguntar por un número y redefino la variable `ingreso`
5. Cuando `ingreso` es igual a `target` o `ingreso` != `target` --> False, me retiro del while
6. Imprimo `Ganaste`

Pensemos como usarlo con la función random
'''

# Otro ejemplo, cuenta atrás para año nuevo
n = 10
while n > 0:
    print(n)
    n -= 1
print('Feliz año nuevo!!!')
'''
### Formato general
while condición:
    acciones a realizar en cada iteración:
    acción 1
    acción 2
    ...
    acción n
resto del código 1
resto del código 2
...
fin del código

Secuencia de pasos según (1):
1. Determinar si la condición es True o False
2. Si es false, salir del  `while` y continuar con la ejecución del resto del código
3. Si la condición es verdadera, correr el cuerpo de código dentro del `while` y volver al paso 1.

'''

"""
------------------------------------------------------------------------------------
             Diferencias y similitudes de las sentencias for y while

                 "for"                                   "while"


-      Se sabe el n° de iteraciones                    No se sabe

-          Usa un contador                      puede usar un cotador pero
                                                debe ser iniciado antes del
                                                bucle y debe incrementar dentro

-     Puede reescribirse un for                   No se puede a la inversa
          usando un while

-     Se puede terminar con "break"                Se puede terminar con "break"

------------------------------------------------------------------------------------
"""


'''
Ejercicio de clase para escribir la lógica en el pizarrón juntes y el código en la compu solos.
Vamos a crear un juego para niñes que están aprendiendo a sumar.
En pantalla se mostrarán dos números y se le debe pedir a la persona que calcule la suma de ambos.
Si la suma es correcta felicitar a la persona. Sino, alentarla a que siga intentando hasta lograrlo

'''

'''
Ejercicios extras
1. Escribir un programa que permita ingresar un número llamado valor_objetivo.
Luego, se debe pedir al usuario que ingrese números por consola hasta que la suma de los números ingresados sea mayor o igual que valor_objetivo

2. Escribir un programa que le permita a una persona ingresar 10 números. Al finalizar, calcular la media, el máximo y el mínimo entre esos valores

3. Escribir un programa que le permita al usuario ingresar la lista del supermercado.
Para finalizar la lista, se deberá ingresar el símbolo *
Imprimir la lista del supermercado

4. Volvemos al ejercicio de la clase anterior donde segmentamos a la población por edades.
Escribir un programa dónde se ingresen 10 edades y devuelva la cantidad de personas en cada grupo etario

'''


'''Bibliografía:
(1) Downey, A. 2016. "Think Python, How to think like a computer scientist". Publicado por O'Reilly
Lutz'
'''
