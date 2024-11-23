from inventario import Inventario
from utils import guardar_productos, cargar_productos, leer_numero, guardar_cambios

def main():
    inventario = Inventario()
    try:
        cargar_productos("productos.json", inventario)
    except FileNotFoundError:
        print("Archivo 'productos.json' no encontrado, iniciando inventario vacío.")
    except Exception as e:
        print(f"Error al cargar productos: {e}")

    header = '''
    ------------------------------------------------------------
                        I N V E N T A R I O
    ------------------------------------------------------------
    1: CREAR ITEM   |  2: CONSULTAR ITEM  |  3: MODIFICAR ITEM
    4: BORRAR ITEM  |  5: VER INVENTARIO  |  6: SALIR
    '''

    @guardar_cambios
    def crear_item(inventario):
        referencia = input('Introduce referencia: ')
        descripcion = input('Introduce descripción: ')
        precio = float(input('Introduce precio: '))
        marca = input('Introduce marca (opcional): ')
        inventario.crear_producto(referencia, descripcion, precio, marca)

    def consultar_item(inventario):
        referencia = input('Introduce referencia a consultar: ')
        print(inventario.leer_producto(referencia) or "Producto no encontrado.")
    
    @guardar_cambios
    def modificar_item(inventario):
        referencia = input('Introduce referencia a modificar: ')
        producto = inventario.leer_producto(referencia)
        if not producto:
            print("Producto no encontrado.")
            return
        descripcion = input('Introduce nueva descripción: ')
        precio = float(input('Introduce precio: '))
        marca = input('Introduce nueva marca (opcional): ')
        inventario.actualizar_producto(referencia, descripcion, precio, marca)
    
    @guardar_cambios
    def borrar_item(inventario):
        referencia = input('Introduce referencia a borrar: ')
        inventario.borrar_producto(referencia)
    
    def listar_items(inventario):
        if inventario.productos:
            print('\nLISTADO DE PRODUCTOS:')
            for producto in inventario.productos:
                print(f'- {producto}')
        else:
            print("El inventario está vacío.")

    def get_action():
        action = leer_numero('Elige una opción: ', int)
        if 1 <= action <= 6:
            return action
        print('Opción no válida, elige un número entre 1 y 6.')
        return get_action()

    actions = {
        1: crear_item,
        2: consultar_item,
        3: modificar_item,
        4: borrar_item,
        5: listar_items
    }

    while True:
        print(header)
        my_action = get_action()
        if my_action == 6:
            break
        action = actions.get(my_action)
        if action:
            action(inventario)
        else:
            print('Opción no válida.')

    print("Gracias por usar el inventario. ¡Hasta luego!\n")


if __name__ == "__main__":
    main()