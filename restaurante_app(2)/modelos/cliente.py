class Cliente:
    """Representa un cliente registrado."""

    def __init__(
        self,
        nombre: str,
        edad: int,
        telefono: str,
        activo: bool
    ):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.activo = activo

    def __str__(self):
        return (
            f"Cliente: {self.nombre} \n"
            f"Edad: {self.edad}\n"
            
            f"Teléfono: {self.telefono} \n"
            f"Activo: {self.activo}"
        )