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
En el código de arriba estamos usando el `for` para ir accediendo a cada una de las cadenas que están guardadas dentro de `palabras`.
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

'''
Ejercicio de clase para hacer entre todos en el pizarrón
Usando la lista de cadenas de abajo, generar una frase e imprimirla.
palabras = ['']
Pistas:
* entre las palabras debería haber un espacio
* la concatenación de cadenas se logra con el operador +
* definir una variable `frase` a la que adicionar las palaras
'''

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

'''Bibliografía:
(1) Downey, A. 2016. "Think Python, How to think like a computer scientist". Publicado por O'Reilly
Lutz'
'''
