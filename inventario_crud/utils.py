# Funciones para guardar y cargar datos del inventario

import json
from models import Producto, Subproducto

def guardar_productos(ruta, inventario):
    """Guarda el inventario en un archivo JSON."""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump([vars(p) for p in inventario.listar_productos()], archivo)

def cargar_productos(ruta, inventario):
    """Carga el inventario desde un archivo JSON."""
    try:
        with open(ruta, 'r') as archivo:
            datos = json.load(archivo)
        for dato in datos:
            if 'marca' in dato:
                inventario.crear_producto(
                    dato['referencia'], dato['descripcion'], dato['precio'], dato['marca']
                )
            else:
                inventario.crear_producto(
                    dato['referencia'], dato['descripcion'], dato['precio']
                )
    except FileNotFoundError:
        print(f"El archivo {ruta} no existe. Se iniciará un inventario vacío.")

# decorator para guardar los cambios
def guardar_cambios(func):
    def wrapper(inventario, *args, **kwargs):
        resultado = func(inventario, *args, **kwargs)
        guardar_productos("productos.json", inventario)
        return resultado
    return wrapper

# función para validar datos de producto

def validar_datos_producto(referencia, descripcion, precio, marca=None):
    """Valida los datos de un producto para asegurar consistencia."""
    if not isinstance(referencia, str) or not referencia.strip():
        raise ValueError("La referencia debe ser una cadena no vacía")
    if not isinstance(descripcion, str) or not descripcion.strip():
        raise ValueError("La descripción debe ser una cadena no vacía")
    if not isinstance(precio, (int, float)) or precio <= 0:
        raise ValueError("El precio debe ser un número mayor a cero")
    if marca and (not isinstance(marca, str) or not marca.strip()):
        raise ValueError("La marca debe ser una cadena no vacía")
    
# validación de entrada numérica

def leer_numero(prompt, tipo=int):
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print(f"Entrada no válida. Por favor introduce un {tipo.__name__}.")
