##Los programas se manejan de manera secuencial
##control de flujo
## 1.condicional: Realiza algo si se cumple ciertas condiciones 
##Bloques: 
## cuando nosotros utilizamos cualquier control de 
##flujo o funciones del codigo que se debe ejecutar despues debera estar definido por bloques o identaciones


# ##EJERCICIO:
# DNI=input("ingresa su numero de DNI: ")
# Cantidad_Caracteres=len(DNI)
# if Cantidad_Caracteres==8:
#     nombre=input("igrese su Nombre: ")
#     mensaje=f""" HOLA BIENVENIDO, {nombre}"""
#     print(mensaje)
# else:
#     print("el numero de DNI es", "INCORRECTO")

# ##HACER UN PROGRAMA QUE PIDA AL USUARIO INGRESAR SU PRIMER APELLIDO SI SU 
# # APELLIDO TIENE COMO ULTIMOS CARACTERES LAS LETRAS "EZ" MOSTRAR UN MENSAJE QUE DIGA ERES CASI ESPAÑOL, 
# # SI LOS CARACTERES FINALES SON "ES" QUE DIGA ERES CASI PERUANO.
# Apellido= input("INGRESA SU APELLIDO PATERNO: ")
# if Apellido[3:]=="ez":
#     print("eres casi español")
# if Apellido[3:]=="es":
#     print("esres casi peruano")

# ## EJERCICIO N°3
# ##HACER QUE EL PROGRAMA PIDA A UN USUARIO SU DNI COMPRUEBE QUE SEA DE 8 DIGITOS,
# #  SI ES CORRECTO QUE SUME EL PRIMER NUMERO Y EL ULTIMO NUMERO DE DNI, MOSTRAR 
# # PARA PANTALLA LA SUMA Y EL RESULTADO

# DNI=input("ingresa su numero de DNI: ")
# Cantidad_Caracteres=len(DNI)
# if Cantidad_Caracteres==8:
#     print("SU DNI ES CORRECTO")
#     suma=(DNI[0:-1])
#     print(DNI[0:-1])
    
# # Ejercicio N° 4

# # hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no

# #2023
 
# año=1980
# if año % 4 != 0: 
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 != 0: 
# 	print("Es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
# 	print("No es bisiesto")
# elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
# 	print("Es bisiesto")
        
# ##EJERCICIO N° 5
# ## TAREA DE PIEDRA, PAPEL O TIJERA.
# ##Otra Clase
# lista=[]
# print(lista)
# primerdato=input("ingresa una fruta: ")
# lista.append(primerdato)
# print(lista)
# segundodato=input("ingrese una segunda fruta: ")
# lista.append(segundodato)
# print(lista)

# ##crear un programa que me deje ingresar datos en una lista vacia
# # Creamos una lista vacía
# lista = []

# # Función para ingresar datos a la lista
# def ingresar_datos():
#     while True:
#         dato = input("Ingresa un dato (o 'salir' para terminar): ")
#         if dato.lower() == "salir":
#             break
#         lista.append(dato)

# # Llamamos a la función para ingresar datos
# ingresar_datos()

# # Mostramos la lista resultante
# print("La lista final es:", lista)

# ## Y su indice posito es 1
# lista=["a","e","i"]
# for indice,valor in enumerate(lista):
#     if valor == "i":
#         print(valor,indice)

## CREAR UNA LISTA QUE ALMACENE LOS NUMEROS DE UNO AL DIEZ
## CREAR UNA FUNCION QUE ME PERMITA RECIBIR COMO PARAMETRO UNA LISTA
## LA FUNCION TENDRA QUE RETORNAR UN NUEVO ARRAY CON LOS NUMEROS PARES QUE EXISTEN 
# Crear la lista que almacene los números del uno al diez
# lista=[1,2,3,4,5,6,7,8,9,10]
# def numeros_pares(array):
#     nueva_lista=[]
#     for _,num in enumerate(array):
#         if num%2==0:
#             nueva_lista.append(num)
#     return nueva_lista
# print("los numeros pares son: ")
# print(numeros_pares(lista))

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def numeros_pares(array):
#     return [num for num in array if num % 2 == 0]
# print("Los números pares son:")
# print(numeros_pares(lista))

## hacer un programa que pida al usuario un texto y evaluar con una funcion la cantidad de vocales a que tiene el texto:
def contar_vocales_a(texto):
    cantidad_a = 0
    for letra in texto:
        if letra.lower() == 'a':
            cantidad_a += 1
    return cantidad_a
def main():
    texto = input("Ingresa un texto: ")
    cantidad_vocales_a = contar_vocales_a(texto)
    print("La cantidad de letras 'a' en el texto es:", cantidad_vocales_a)
if __name__ == "__main__":
    main()

