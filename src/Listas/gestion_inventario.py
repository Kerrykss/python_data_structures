# Sistema de gestión de inventario

# 1. Inventario: lista de sublistas [nombre, cantidad, precio]
inventario = [
    ["Manzanas", 50, 1.20],
    ["Leche",    30, 0.90],
    ["Pan",      20, 2.50],
]

# 2. Actualizar el precio de un producto
def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"Precio de '{producto}' actualizado a ${nuevo_precio:.2f}")
            return
    print(f"Producto '{producto}' no encontrado.")

# 3. Registrar una venta (descuenta stock si hay suficiente)
def registrar_venta(producto, cantidad):
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta registrada: {cantidad} x '{producto}'")
            else:
                print(f"Stock insuficiente para '{producto}'. Disponible: {item[1]}")
            return
    print(f"Producto '{producto}' no encontrado.")

# 4. Añadir producto nuevo o sumar stock si ya existe
def anadir_producto(producto, cantidad, precio):
    for item in inventario:
        if item[0] == producto:
            item[1] += cantidad
            print(f"Stock de '{producto}' actualizado. Total: {item[1]}")
            return
    inventario.append([producto, cantidad, precio])
    print(f"Producto '{producto}' añadido al inventario.")

# 5. Mostrar el estado del inventario
def mostrar_inventario():
    print("\n--- INVENTARIO ACTUAL ---")
    print(f"{'Producto':<15} {'Cantidad':>10} {'Precio':>10}")
    print("-" * 38)
    for item in inventario:
        print(f"{item[0]:<15} {item[1]:>10} {item[2]:>9.2f}€")
    print("-" * 38)

# --- Llamadas ---
actualizar_precio("Leche", 1.10)        # 2.º producto
registrar_venta("Manzanas", 10)         # 1.er producto
anadir_producto("Huevos", 24, 3.00)     # producto nuevo
mostrar_inventario()