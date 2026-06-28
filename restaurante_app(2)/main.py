from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante_principal = Restaurante(
    "Restaurante Cayambe"
)

# Crear productos
producto_1 = Producto(
    "Hamburguesa Especial",
    6.50,
    15,
    True
)

producto_2 = Producto(
    "Pizza Familiar",
    12.75,
    10,
    True
)

# Crear clientes
cliente_1 = Cliente(
    "Carla Elizabeth",
    24,
    "0991112233",
    True
)

cliente_2 = Cliente(
    "Andrade Guerrero",
    30,
    "0984445566",
    True
)

# Agregar productos al restaurante
restaurante_principal.agregar_producto(producto_1)
restaurante_principal.agregar_producto(producto_2)

# Agregar clientes al restaurante
restaurante_principal.agregar_cliente(cliente_1)
restaurante_principal.agregar_cliente(cliente_2)

# Mostrar información
print(f"\n{restaurante_principal.nombre_restaurante}")

restaurante_principal.mostrar_productos()
restaurante_principal.mostrar_clientes()