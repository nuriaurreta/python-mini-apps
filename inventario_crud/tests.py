import unittest
from models import Producto, Subproducto
from inventario import Inventario
from utils import validar_datos_producto

class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        producto = Producto("Camisa", "Camisa de algodón", 20.0)
        self.assertEqual(producto.referencia, "Camisa")
        self.assertEqual(producto.descripcion, "Camisa de algodón")
        self.assertEqual(producto.precio, 20.0)

    def test_actualizar_producto(self):
        producto = Producto("Camisa", "Camisa de algodón", 20.0)
        producto.actualizar(descripcion="Camisa de lino", precio=25.0)
        self.assertEqual(producto.descripcion, "Camisa de lino")
        self.assertEqual(producto.precio, 25.0)

class TestSubproducto(unittest.TestCase):
    def test_creacion_subproducto(self):
        subproducto = Subproducto("Zapatillas", "Zapatillas deportivas", 50.0, "Nike")
        self.assertEqual(subproducto.referencia, "Zapatillas")
        self.assertEqual(subproducto.descripcion, "Zapatillas deportivas")
        self.assertEqual(subproducto.precio, 50.0)
        self.assertEqual(subproducto.marca, "Nike")

    def test_actualizar_subproducto(self):
        subproducto = Subproducto("Zapatillas", "Zapatillas deportivas", 50.0, "Nike")
        subproducto.actualizar(descripcion="Zapatillas de running", precio=55.0, marca="Adidas")
        self.assertEqual(subproducto.descripcion, "Zapatillas de running")
        self.assertEqual(subproducto.precio, 55.0)
        self.assertEqual(subproducto.marca, "Adidas")

class TestUtils(unittest.TestCase):
    def test_validar_datos_producto(self):
        # Caso válido
        validar_datos_producto("Camisa", "Camisa de algodón", 20.0)
        # Casos inválidos
        with self.assertRaises(ValueError):
            validar_datos_producto("", "Camisa de algodón", 20.0)  # Referencia vacío
        with self.assertRaises(ValueError):
            validar_datos_producto("Camisa", "", 20.0)  # Descripción vacía
        with self.assertRaises(ValueError):
            validar_datos_producto("Camisa", "Camisa de algodón", -5.0)  # Precio negativo

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()
        self.inventario.crear_producto("Camisa", "Camisa de algodón", 20.0)
        self.inventario.crear_producto("Pantalón", "Pantalón de mezclilla", 30.0)
        self.inventario.crear_producto("Zapatillas", "Zapatillas deportivas", 50.0, "Nike")

    def test_crear_producto(self):
        self.inventario.crear_producto("Sombrero", "Sombrero de verano", 15.0)
        producto = self.inventario.leer_producto("Sombrero")
        self.assertIsNotNone(producto)
        self.assertEqual(producto.referencia, "Sombrero")

    def test_crear_producto_existente(self):
        resultado = self.inventario.crear_producto("Camisa", "Otra descripción", 25.0)
        self.assertFalse(resultado)  # No debería permitir duplicados

    def test_leer_producto(self):
        producto = self.inventario.leer_producto("Camisa")
        self.assertIsNotNone(producto)
        self.assertEqual(producto.referencia, "Camisa")
        self.assertEqual(producto.descripcion, "Camisa de algodón")
        self.assertEqual(producto.precio, 20.0)

    def test_actualizar_producto(self):
        self.inventario.actualizar_producto("Camisa", descripcion="Camisa de lino", precio=25.0)
        producto = self.inventario.leer_producto("Camisa")
        self.assertEqual(producto.descripcion, "Camisa de lino")
        self.assertEqual(producto.precio, 25.0)

    def test_actualizar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            self.inventario.actualizar_producto("NoExiste", descripcion="Descripción nueva")

    def test_borrar_producto(self):
        self.inventario.borrar_producto("Camisa")
        producto = self.inventario.leer_producto("Camisa")
        self.assertIsNone(producto)

    def test_borrar_producto_inexistente(self):
        with self.assertRaises(ValueError):
            self.inventario.borrar_producto("NoExiste")

    def test_listar_productos(self):
        productos = self.inventario.listar_productos()
        self.assertEqual(len(productos), 3)  # Hay 3 productos en el inventario inicial

if __name__ == "__main__":
    unittest.main()
