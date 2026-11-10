
productos = {
    1: ("Pizza", 18000, 20),
    2: ("Cafe", 5000, 15),
    3: ("Sandwich", 6000, 10),
    4: ("Arepa", 3500, 25),
    5: ("Te", 2000, 8)
}

def mostrar_productos(productos):
    print("\n========== CATALOGO DE PRODUCTOS ==========")
    print("Codigo | Producto       | Precio | Cantidad")

    for codigo, datos in productos.items():
        nombre, precio, cantidad = datos

        print(codigo, "|", nombre, "|", precio, "|", cantidad)

def registrar_producto(productos, pedido, codigo, cantidad_solicitada):

    if codigo not in productos:
        print("Producto no encontrado.")
        return

    if cantidad_solicitada <= 0:
        print("Cantidad no valida.")
        return

    nombre, precio, cantidad_disponible = productos[codigo]

    if cantidad_solicitada > cantidad_disponible:
        print("No hay suficientes unidades disponibles.")
        print("Unidades disponibles:", cantidad_disponible)
        return

    subtotal = precio * cantidad_solicitada

    pedido.append((codigo, nombre, cantidad_solicitada, subtotal))

    productos[codigo] = (
        nombre,
        precio,
        cantidad_disponible - cantidad_solicitada
    )

    print("El producto fue agregado con exito")
    
def calcular_total(pedido):
    total = 0
    
    for producto in pedido:
        total += producto[3]
    return total

def mostrar_resumen(pedido):

    print("\n========== RESUMEN DEL PEDIDO ==========")
    print("Producto       Cantidad     Subtotal")
    print("-----------------------------------------")

    for producto in pedido:
        codigo, nombre, cantidad, subtotal = producto
        print(nombre, "       ", cantidad, "       ", subtotal)

    total = calcular_total(pedido)

    if total >= 50000:
        descuento = total * 0.10
    else:
        descuento = 0

    total_final = total - descuento

    print("-----------------------------------------")
    print("Total:", total)
    print("Descuento:", int(descuento))
    print("El total final a pagar es:", int(total_final))
pedido = []

while True:
    print("\n========== CAFETERIA ==========")
    print("1. Mostrar productos")
    print("2. Agregar producto al pedido")
    print("3. Finalizar pedido")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        mostrar_productos(productos)

    elif opcion == "2":

        mostrar_productos(productos)

        try:
            codigo = int(input("\nIngrese el codigo del producto: "))
            cantidad = int(input("Ingrese la cantidad: "))

            registrar_producto(productos, pedido, codigo, cantidad)

        except ValueError:
            print("Cantidad o codigo no valido.")

    elif opcion == "3":

        if len(pedido) > 0:
            mostrar_resumen(pedido)
        else:
            print("No se registraron productos en el pedido")

        print("\nGracias por comprar en nuestro restaurante de mala muerte ")
        break

    else:
        print("Error.")

