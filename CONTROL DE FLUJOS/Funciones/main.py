## lo que se va retornar
def mensajes(resultado):
    nuevoMensaje=f"""
    =======================
    Hola Chamo, como estas?
    Alamos
    {resultado}
    =======================
    """
    return nuevoMensaje
def suma(numeroUno,numeroDos):
    operacion=numeroUno+numeroDos
    return mensajes.mensajes(operacion)
primerDato=int(input("ingrese el primer numero: "))
segundoDato=int(input("ingrese el segundo numero: "))
print(suma(primerDato,segundoDato))
