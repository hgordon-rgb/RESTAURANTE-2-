class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(
        self,
        nombre: str,
        precio: float,
        cantidad: int,
        disponible: bool
    ):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Cantidad: {self.cantidad}\n"
            f"Disponible: {self.disponible}"
        )