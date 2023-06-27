## Se separa con comas y entre corchetes []
#vocales = ["a","e","i","o","u"]
#for vocal in vocal:
#print(vocal)
colores = ["amarillo","rojo","azul","marron","anaranjado"]
clr = input("ingrese su color favorito:")
for color in colores:
    if color == clr:
        print (color)
        print(f"se encontro el color:{color}")
        break 
    print(color)