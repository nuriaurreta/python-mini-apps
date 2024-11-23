# Definir estructuras de datos de producto y subproducto

class Producto:
    """Clase base para un producto general."""
    def __init__(self, referencia, descripcion, precio):
        self.referencia = referencia
        self.descripcion = descripcion
        self.precio = precio

    def actualizar(self, descripcion=None, precio=None):
        if descripcion:
            self.descripcion = descripcion
        if precio:
            self.precio = precio

    def __str__(self):
        return (f"\nPRODUCTO:\nReferencia: {self.referencia}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio: {self.precio:.2f} €\n")


class Subproducto(Producto):
    """Clase para un producto con una marca específica."""
    def __init__(self, referencia, descripcion, precio, marca):
        super().__init__(referencia, descripcion, precio)
        self.marca = marca

    def actualizar(self, descripcion=None, precio=None, marca=None):
        super().actualizar(descripcion, precio)
        if marca:
            self.marca = marca

    def __str__(self):
        return (f"\nPRODUCTO:\nReferencia: {self.referencia}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio: {self.precio:.2f} €\n"
                f"Marca: {self.marca if self.marca else 'Sin marca'}")
