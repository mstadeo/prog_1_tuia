'''Clase 2 de Programación 1
Agenda:
1. Operadores aritméticos
2. Tipos de datos
3. Asignación
4. Expresiones
'''


print("")   #### salto de linea para vizualizar mejor en consola
######################################################################
'''1. Operadores aritméticos

- suma: +
- resta: -
- multiplicación: *
- división: /
- exponencial: **
- floor division: //
- módulo: %

La jerarquia de los operadores aritméticos es la misma que conocemos de matemáticas.

Las jerarquía de menor a mayor, siendo la menor la dominante.

Valor Jerárquico    Operador                Nombres

      0                ()                 paréntesis
      1              % , **            Módulo, potencia
      2            * , /, //     producto, división, floor division
      3               + , -                suma, resta

'''

print('####### Operadores aritméticos #######')
print("")   #### salto de linea para vizualizar mejor en consola
a = 2
b = 6

print('Prueba de suma: ', a + b)
#print('Prueba de resta: ', a - b)
#print('Prueba de multiplacación: ', a * b)
#print('Prueba de división: ', a / b)
#print('Prueba de exponencial: ', a ** b)
#print('Prueba de floor división: ', b // a)
#print('Prueba de módulo: ', b % 2)

## Resolver


print("")   #### salto de linea para vizualizar mejor en consola
print("")   #### salto de linea para vizualizar mejor en consola
######################################################################
'''2. Tipos de datos
A continuación definimos una lista con sus nombres en español/inglés/ y el nombre asignado dentro de Python (tipo).

Todos los programas trabajan con objetos de datos. Dentro de este conjunto diferenciamos 2
subconjuntos

Escalar (Un dato atómico y unidimensional.)
- Enteros/Integers: int
- Flotantes/Floats: float
- Booleano: bool
- NoneType: None    Solo mencionar por ahora.

No Escalar (tiene una estructura interna a la que se puede acceder)
- Cadena/String: str
-
-
'''


print('####### Tipos de datos #######')
print("")   #### salto de linea para vizualizar mejor en consola
entero = 3      # números enteros
flotante = 3.0  # números reales
cadena = '3'


#Cuando los imprimimos se ven bastante parecidos
print(entero, '/', flotante, '/', cadena)

#Y python nos ayuda a ver el tipo de dato
print(type(entero), type(flotante), type(cadena))

#Pero no siempre podemos operar con ellos
print(entero + flotante)

# print(entero + cadena) #descomentar para ver error
print(entero * cadena)

# print(flotante * cadena) #descomentar para ver error
print(True)
print(False)

print("")   #### salto de linea para vizualizar mejor en consola
#Tambien podemos pasar de un tipo a otro:
print(type(entero))

print(type(str(entero))) #pasar el entero a cadena

print(entero + int(cadena)) #pasar la cadena a entero

flotante2 = 3.7
print(flotante2)
print(int(flotante2))  # corta la parte decimal.


# INT y FLOAT  y los
queTipo1 = entero * flotante
queTipo2 = entero / flotante
queTipo3 = entero // flotante
queTipo4 = entero // entero

##type(queTipo1)
