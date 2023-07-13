import inicio
while len(inicio.lista)<5:
    dato = input("ingresa un dato:")
    inicio.lista.append(dato)
for texto in range(0,len(inicio.lista)):
    if inicio.lista [texto] == "disco":
        palabra=inicio.lista[texto]
        indice=texto