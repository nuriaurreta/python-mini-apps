# Manejar y modificar productos

from models import Producto, Subproducto
from utils import validar_datos_producto

class Inventario:
    """Clase para gestionar un inventario de productos."""
    def __init__(self):
        self.productos = {}

    def crear_producto(self, referencia, descripcion, precio, marca=None):
        validar_datos_producto(referencia, descripcion, precio, marca)
        if referencia.lower() in self.productos:
            print(f"El producto con referencia '{referencia}' ya existe en el inventario.")
            return False
        if marca:
            self.productos[referencia.lower()] = Subproducto(referencia, descripcion, precio, marca)
        else:
            self.productos[referencia.lower()] = Producto(referencia, descripcion, precio)
        return True


    def leer_producto(self, referencia):
        return self.productos.get(referencia.lower(), None)

    def actualizar_producto(self, referencia, descripcion=None, precio=None, marca=None):
        producto = self.leer_producto(referencia)
        if producto:
            producto.actualizar(descripcion, precio)
            if isinstance(producto, Subproducto) and marca:
                producto.actualizar(marca=marca)
        else:
            raise ValueError(f"Producto con referencia '{referencia}' no encontrado")

    def borrar_producto(self, referencia):
        if referencia.lower() in self.productos:
            del self.productos[referencia.lower()]
        else:
            raise ValueError(f"Producto con referencia '{referencia}' no encontrado")

    def listar_productos(self):
        return list(self.productos.values())

    def __str__(self):
        return "\n".join(str(producto) for producto in self.productos.values())
