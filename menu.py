inicio = """
#######################################################
# Bienvenido a la documentacion del proyecto Aurelion #
#                     Grupo 8                         #
#######################################################
"""
opciones = """
Seleccione alguna opcion:
1. Integrantes
2. Tema, problema y solución
3. Dataset
4. Pseudocodigo
5. Salir
"""
integrantes = """
Andres Guzman
"""

tema = """
TEMA:
PROBLLEMA:
SOLUCIÓN:
"""

datos = """
TABLA PRODUCTOS
TABLA DETALLE_VENTAS
TABLA VENTAS
TABLA CLIENTES
"""

pseudocodigo = """
Inicio
MIENTRAS menu != 5
    EVALUAR menu
        CASO 1:
        CASO 2:
        CASO 3:
        CASO 4:
        CASO 5:
        CASO _:
            Imprimir(Selecione una opción valida)
"""
menu = None
while menu != 5:
    print(inicio)
    menu = int(input(opciones))
    print(f'Opcion Selecccionada: {menu}')
    match menu:
        case 1:
            print(integrantes)
        case 2:
            print(tema)
        case 3:
            print(datos)
        case 4:
            print(pseudocodigo)
        case 5:
            print('Gracias!')
        case _:
            print('Seleccione una opción valida')
