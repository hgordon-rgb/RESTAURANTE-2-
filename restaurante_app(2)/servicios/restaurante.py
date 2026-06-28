class Restaurante:
    """Gestiona los productos y clientes del restaurante."""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n=== PRODUCTOS REGISTRADOS ===\n")

        for producto in self.productos:
            print(producto)
            print()

    def mostrar_clientes(self):
        print("\n=== CLIENTES REGISTRADOS ===\n")

        for cliente in self.clientes:
            print(cliente)
            print()