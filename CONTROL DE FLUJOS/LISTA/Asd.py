##Pedir a un usuario una lista de 5 elementos 
## Si en la lista contiene la palabra disco
## Mostrar la palabra y la ubicacion de su indice positivo
## crear en 3 capaz.
lista=[]
indice= 0
palabra=""
while len(lista)<5:
    dato = input("ingresa un dato:")
    lista. append(dato)
for texto in range(0,len(lista)):
    if lista [texto] == "disco":
        palabra=lista[texto]
        indice=texto
print(f"""el texto disco se encuentra en el indice {indice} y el texto es {palabra}""")