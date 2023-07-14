# ## LISTA DE FRUTAS
# frutas=[]
# while len(frutas)<5:
#     nuevaFruta=input ("ingresa una fruta:")
#     for fruta in frutas:
#         if len (nuevaFruta) == len(fruta):
#             print("tiene la misma logitud gilazo, ingresa otro:")
#     if nuevaFruta in frutas:
#         print("esta fruta ya existe huavonaso, ingresa otro pendejazo")
#     else:
#         frutas.append(nuevaFruta)

# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index])>longitudTexto:
#             longitudText=len(array[index])
#             mostrarFruta=array[index]
#     return mostrarFruta
# print(f"""la fruta con mayor cantidad de letras es:{textoLargo(frutas)}""")


##efhkfgdhsu
# frutas=[]
# contador=0
# while contador<5:
#     nuevaFruta=input ("ingresa una fruta:")
#     for fruta in frutas:
#         if len (nuevaFruta) == len(fruta):
#             print("tiene la misma logitud gilazo, ingresa otro:")
#             continue
#     if nuevaFruta in frutas:
#         print("esta fruta ya existe huavonaso, ingresa otro pendejazo")
#     else:
#         frutas.append(nuevaFruta)
#         contador=contador + 1
# def textoLargo(array):
#     longitudTexto=0
#     mostrarFruta=""
#     for index in range(0,len(array)):
#         if len(array[index])>longitudTexto:
#             longitudText=len(array[index])
#             mostrarFruta=array[index]
#     return mostrarFruta
# print(f"""la fruta con mayor cantidad de letras es:{textoLargo(frutas)}""")

## Identificar el indice y el sffsrdf
frutas=[]
contador=0
indice=0 
Palabra=""
while contador<5:
    nuevaFruta=input ("ingresa una fruta:")
    for fruta in frutas:
        if len (nuevaFruta) == len(fruta):
            print("tiene la misma logitud gilazo, ingresa otro:")
            continue
    if nuevaFruta in frutas:
        print("esta fruta ya existe huavonaso, ingresa otro pendejazo")
    else:
        frutas.append(nuevaFruta)
        contador=contador + 1
def textoLargo(array):
    longitudTexto=0
    mostrarFruta=""
    for index in range(0,len(array)):
        if len(array[index])>longitudTexto:
            longitudText=len(array[index])
            mostrarFruta=array[index]
    return mostrarFruta
print(f"""la fruta con mayor cantidad de letras es:{textoLargo(frutas)}""") 