##crear un programa que me deje ingresar datos en una lista vacia:
lista =[]
def ingresar_datos():
    while True:
        dato = input("Ingresa un dato (o 'si' para terminar): ")
        if dato.lower() == "si":
            break
        lista.append(dato)
ingresar_datos()
print("La lista completa es:", lista)