"""
La Encuesta Permanente de Hogares (EPH) es una encuesta de propósitos múltiples que
releva información sobre hogares y personas. Entre las temáticas se encuesta sobre la situación laboral de las personas. (NOTA : Esto es una simplificación)
Para que una persona pertenezca a la fuerza laboral (Población Económicamente Activa) de nuestro país debe presentar algunas características de lo contrario no se lo considera activo:


# ACTIVOS
  -  Edad >= 10

      * ocupados:
          Realizar alguna actividad remunerada o no en la actualidad
          plenamente ocupado >= 35 hs semanales
          subocupado < 35 hs semanales

      * desocupados:
          0 hs semanales pero se encuentré en búsqueda efectiva de empleo.


# NO ACTIVOS



**Ejercicio 1**

Realizar un programa utilizando control de flujo condicional que:
Partiendo de la edad del individuo (ingresada por el usuario) determine si la persona pertenece a PEA (ACTIVO) o no.



**Ejercicio 2**  (No se considera el caso de que la persona no busque empleo)

Realizar un programa utilizando control de flujo condicional que:
Partiendo de la edad del individuo (ingresada por el usuario) determine si la persona pertenece a PEA o no.
Y de pertenecer, a partir de las horas trabajadas (entero ingresado por el usuario en consola), indique si es:
    - ocupado >= 35 hs
    - 0 hs < subocupado < 35 hs
    - desocupado  == 0

imprima las caracteristicas en pantalla.


**Ejercicio 3**

Modifique el código para que el programa distinga entre la persona que busca empleo activamente y la que no.
(Esta última sera incluida como no activa/o en la salida del programa.)

"""

"""
**Ejercicio 4**

El gobierno nacional implementa un plan de vivienda subsidiado.
Las condiciones para acceder a este tipo de financiacón son las siguientes:

    - tener nacionalidad argentina
    - ser mayor de edad
    - no poseer vivienda propia
    - ser empleado en relacion de dependencia
           * tener ingresos netos no mayores a $2.646.009,01 de pesos anuales.
    - ser monotributista
           * no superar la categoria G ($2.646.009,01 de facturación anual)

generar un programa que por medio del control de flujo por declaraciones coneicionales if-elif-else pueda evaluar si la persona califica o no para el crédito e imprima por pantalla si califica o no para el mismo.
Nota: Las personas pueden sere monotributistas y trabajar en relacion de dependencia. En este caso, el ingreso es la suma de los ingresos en ambas actividades
"""
