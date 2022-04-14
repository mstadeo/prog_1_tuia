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
"""
edad = int(input("Ingrese la edad de la persona: ")) # La función input me devuelve un tipo de dato String, por eso lo casteo a Int

if edad < 10:
    print("Esta persona no pertenece a la PEA")
else:
    print("Esta persona pertence a la población económicamente activa")


"""
**Ejercicio 2**  (No se considera el caso de que la persona no busque empleo)

Realizar un programa utilizando control de flujo condicional que:
Partiendo de la edad del individuo (ingresada por el usuario) determine si la persona pertenece a PEA o no.
Y de pertenecer, a partir de las horas trabajadas (entero ingresado por el usuario en consola), indique si es:
    - ocupado >= 35 hs
    - 0 hs < subocupado < 35 hs
    - desocupado  == 0

imprima las caracteristicas en pantalla.
"""



edad = int(input("Ingrese la edad de la persona: "))

if edad < 10:
    print("Esta persona no pertenece a la PEA")
else:
    horas = int(input("Ingrese las horas trabajadas semanales(0 hs -- desocupado): ")) #asumimos que siempre ingresan números positivos
    if horas == 0:
        print("Esta persona pertenece a la PEA y está buscando activamente trabajo")
    elif horas < 35:
        print("Esta persona pertenece a la PEA y está subocupada")
    else:
        print("Esta persona pertenece a la PEA y está ocupada")





"""
**Ejercicio 3**

Modifique el código para que el programa distinga entre la persona que busca empleo activamente y la que no.
(Esta última sera incluida como no activa/o en la salida del programa.)


"""

edad = int(input("Ingrese la edad de la persona: "))

if edad < 10:
    print("Esta persona no pertenece a la PEA")
else:
    horas = int(input("Ingrese las horas trabajadas semanales(0 hs -- desocupado): "))

    if horas == 0:
        busca = input("Esta buscando trabajo de forma activa (ingrese si o no):")
        if busca == "si":
            print("Esta persona pertenece a la PEA y está buscando activamente trabajo")
        else:
            print("Esta persona no pertenece a la PEA")

    elif  horas < 35: #asumimos que siempre ingresan números positivos
        print("Esta persona pertenece a la PEA y está subocupada")
    else:
        print("Esta persona pertenece a la PEA y está ocupada")

"""

** Ejercicio 4 **

El gobierno nacional implementa un plan de vivienda subsidiado.
Las condiciones para acceder a este tipo de financiacón son las siguientes:

    - tener nacionalidad argentina
    - ser mayor de edad
    - no poseer vivienda propia
    - ser empleado en relacion de dependencia
           * tener ingresos netos no mayores a $2.646.009,01 de pesos anuales.
    - ser monotributista
           * no superar la categoria G ($2.646.009,01 de facturación anual, la categoria H supera los 3000000)


Generar un programa que por medio del control de flujo por declaraciones condicionales if-elif-else pueda evaluar
si la persona califica o no para el crédito e imprima por pantalla si califica o no para el mismo.
Nota: Las personas pueden sere monotributistas y trabajar en relacion de dependencia. En este caso, el ingreso es la suma de los ingresos en ambas actividades
"""

nacionalidad = input(" Ingrese su nacionalidad: ")
if nacionalidad != "argentina" :
    print(" Esta persona no califica para el prestamo subsidiado")
else:
    edad = int(input(" Ingrese su edad "))
    if edad < 18:
        print(" Esta persona no califica para el prestamo subsidiado")
    else:
        vivienda =  input(" Posee vivienda propia (si, no)")
        if vivienda == "si":
            print(" Esta persona no califica para el prestamo subsidiado")
        else:
            empleado = input(" Es empleado en relación de dependencia (si ,no) ")
            monotributista = input(" Es monotributista (si ,no) ")
            if empleado == "si" or monotributista == "si":
                salario = int(input(" Cual es su ingreso anual bruto en pesos. Si respondió si a ambos sume ambos ingresos"))
                if salario > 2646009.01:
                    print(" Esta persona no califica para el prestamo subsidiado")
                else:
                    print(" Esta persona CALIFCA para el prestamo!!!!")
            else:
                print(" Esta persona no califica para el prestamo subsidiado")
