# Definir una lista vacía para almacenar los productos
inventario = []

# Creamos una función para agregar un producto al inventario
def agregar_producto(nombre, categoria, cantidad, precio):

  # vamos a verificar si el producto ya existe en el inventario para evitar tener duplicados

  # utilizaremos el ciclo FOR

  for producto in inventario:
    if producto["nombre"] == nombre:
      print("El producto ya existe en el inventario.")
      return

  # Si no existe el producto en el sistema, entonces vamos a crear un diccionario con los datos del producto

  producto = {
    "nombre": nombre,
    "categoria": categoria,
    "cantidad": cantidad,
    "precio": precio
  }

  # Agregaremos el diccionario a la lista del inventario
  inventario.append(producto)
  print("Nuestro producto se ha agregado al inventario exitosamente.")

# Crearemos una función para eliminar un producto del inventario

def eliminar_producto(nombre):

  # para buscar el producto por su nombre en el inventario utilizaremos el ciclo FOR

  for producto in inventario:
    if producto["nombre"] == nombre:

      # Para Eliminar el producto de la lista del inventario usaremos REMOVE

      inventario.remove(producto)

      print("Nuestro producto se ha eliminado del inventario exitosamente.")
      return

  # Si no se encuentra el producto, vamos a mostrar un mensaje

  print("El producto no se encuentra en el inventario.")



# Crearemos una función para mostrar el menú de opciones

def mostrar_menu():
  print("Sistema de Inventario Karibay")
  print("Por favor, ingrese el numero de la opción que desea realizar: ")
  print("1. Ingresar Producto")
  print("2. Eliminar Producto")
  print("3. Buscar Producto")
  print("4. Actualizar Producto")
  print("5. Mostrar Inventario")
  print("6. Salir")

# Definir una variable para controlar el ciclo principal
continuar = True

# Iniciar el ciclo principal
while continuar:
  # Mostrar el menú de opciones
  mostrar_menu()
  # Solicitar al usuario que ingrese una opción
  opcion = input("Ingrese una opción: ")
  # Verificar la opción ingresada
  if opcion == "1":
    # Solicitar los datos del producto a agregar
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    # Corregir el error de tipo de dato al convertir la entrada a entero
    cantidad = int(input("Ingrese la cantidad en stock del producto: "))
    # Corregir el error de tipo de dato al convertir la entrada a flotante
    precio = float(input("Ingrese el precio del producto: "))
    # Llamar a la función para agregar el producto
    agregar_producto(nombre, categoria, cantidad, precio)
  elif opcion == "2":
    # Solicitar el nombre del producto a eliminar
    nombre = input("Ingrese el nombre del producto: ")
    # Llamar a la función para eliminar el producto
    eliminar_producto(nombre)
  elif opcion == "3":
    # Solicitar el criterio de búsqueda
    criterio = input("Ingrese el nombre o la categoría del producto: ")
    # Llamar a la función para buscar el producto
    buscar_producto(criterio)
  elif opcion == "4":
    # Solicitar el nombre del producto a actualizar
    nombre = input("Ingrese el nombre del producto: ")
    # Solicitar la nueva cantidad y el nuevo precio
    cantidad = int(input("Ingrese la nueva cantidad en stock del producto: "))
    precio = float(input("Ingrese el nuevo precio del producto: "))
    # Llamar a la función para actualizar el producto
    actualizar_producto(nombre, cantidad, precio)
  elif opcion == "5":
    # Llamar a la función para mostrar el inventario
    mostrar_inventario()
  elif opcion == "6":
    # Terminar el ciclo principal
    continuar = False
    print("Gracias por usar el sistema de Karibay.")
  else:
    # Mostrar un mensaje de error si la opción no es válida
    print("Opción inválida. Por favor elije una opcion.")