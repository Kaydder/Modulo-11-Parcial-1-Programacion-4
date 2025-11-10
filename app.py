import json
import os

ARCHIVO = "articulos.json"

def cargar_articulos():
    """Carga los artículos desde el archivo JSON si existe."""
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_articulos(articulos):
    """Guarda los artículos en el archivo JSON."""
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(articulos, f, indent=4, ensure_ascii=False)

def mostrar_articulos(articulos):
    """Muestra todos los artículos en formato tabulado."""
    if not articulos:
        print("\nNo hay artículos registrados.\n")
        return
    print("\nLISTA DE ARTÍCULOS:")
    print("-" * 80)
    print(f"{'ID':<5}{'Nombre':<20}{'Categoría':<15}{'Cantidad':<10}{'Precio':<10}{'Total':<10}")
    print("-" * 80)
    for art in articulos:
        total = art['cantidad'] * art['precio_unitario']
        print(f"{art['id']:<5}{art['nombre']:<20}{art['categoria']:<15}{art['cantidad']:<10}{art['precio_unitario']:<10.2f}{total:<10.2f}")
    print("-" * 80)

def registrar_articulo(articulos):
    """Permite registrar un nuevo artículo."""
    print("\nREGISTRAR NUEVO ARTÍCULO")

    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("Error: cantidad y precio deben ser numéricos.")
        return

    descripcion = input("Descripción: ").strip()

    if not nombre or not categoria:
        print("Los campos nombre y categoría son obligatorios.")
        return

    nuevo_id = len(articulos) + 1
    articulo = {
        "id": nuevo_id,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio_unitario": precio,
        "descripcion": descripcion
    }
    articulos.append(articulo)
    guardar_articulos(articulos)
    print("Artículo registrado exitosamente.")

def buscar_articulo(articulos):
    """Permite buscar artículos por nombre o categoría."""
    print("\nBUSCAR ARTÍCULO")
    criterio = input("Buscar por nombre o categoría: ").strip().lower()
    resultados = [a for a in articulos if criterio in a['nombre'].lower() or criterio in a['categoria'].lower()]

    if resultados:
        mostrar_articulos(resultados)
    else:
        print("No se encontraron coincidencias.")

def editar_articulo(articulos):
    """Permite editar un artículo existente."""
    mostrar_articulos(articulos)
    try:
        id_articulo = int(input("Ingrese el ID del artículo a editar: "))
    except ValueError:
        print("ID inválido.")
        return

    for art in articulos:
        if art["id"] == id_articulo:
            print(f"\nEditando '{art['nombre']}' (deje en blanco para mantener el valor actual)")
            nuevo_nombre = input(f"Nuevo nombre [{art['nombre']}]: ").strip()
            nueva_categoria = input(f"Nueva categoría [{art['categoria']}]: ").strip()
            nueva_cantidad = input(f"Nueva cantidad [{art['cantidad']}]: ").strip()
            nuevo_precio = input(f"Nuevo precio unitario [{art['precio_unitario']}]: ").strip()

            if nuevo_nombre:
                art["nombre"] = nuevo_nombre
            if nueva_categoria:
                art["categoria"] = nueva_categoria
            if nueva_cantidad:
                try:
                    art["cantidad"] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad inválida, se mantiene el valor anterior.")
            if nuevo_precio:
                try:
                    art["precio_unitario"] = float(nuevo_precio)
                except ValueError:
                    print("Precio inválido, se mantiene el valor anterior.")

            guardar_articulos(articulos)
            print("Artículo actualizado correctamente.")
            return
    print("No se encontró el artículo con ese ID.")

def eliminar_articulo(articulos):
    """Permite eliminar un artículo del sistema."""
    mostrar_articulos(articulos)
    try:
        id_articulo = int(input("Ingrese el ID del artículo a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    for art in articulos:
        if art["id"] == id_articulo:
            articulos.remove(art)
            guardar_articulos(articulos)
            print("Artículo eliminado correctamente.")
            return
    print("No se encontró un artículo con ese ID.")

def menu():
    articulos = cargar_articulos()

    while True:
        print("\n=== SISTEMA DE REGISTRO DE PRESUPUESTO ===")
        print("1. Registrar artículo")
        print("2. Buscar artículo")
        print("3. Editar artículo")
        print("4. Eliminar artículo")
        print("5. Listar todos los artículos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_articulo(articulos)
        elif opcion == "2":
            buscar_articulo(articulos)
        elif opcion == "3":
            editar_articulo(articulos)
        elif opcion == "4":
            eliminar_articulo(articulos)
        elif opcion == "5":
            mostrar_articulos(articulos)
        elif opcion == "6":
            print("\nSaliendo del sistema. Hasta luego.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
