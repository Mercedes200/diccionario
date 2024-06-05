contactos = {}  # Diccionario para almacenar los contactos

def agregar_contacto():
  """Función para agregar un nuevo contacto."""
  nombre = input("Ingresa el nombre del contacto: ")
  telefono = input("Ingresa el número de teléfono: ")
  contactos[nombre] = telefono
  print("El contacto ha sido agregado correctamente.")

def buscar_contacto():
  """Función para buscar un contacto por su nombre."""
  nombre = input("Ingresa el nombre del contacto: ")
  if nombre in contactos:
    print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
  else:
    print(f"El contacto {nombre} no existe.")

def mostrar_contactos():
  """Función para mostrar todos los contactos."""
  if contactos:
    print("Contactos:")
    for nombre, telefono in contactos.items():
      print(f"- {nombre}: {telefono}")
  else:
    print("No hay contactos almacenados.")

def actualizar_telefono():
  """Función para actualizar el número de teléfono de un contacto."""
  nombre = input("Ingresa el nombre del contacto a actualizar: ")
  if nombre in contactos:
    nuevo_telefono = input("Ingresa el nuevo número de teléfono: ")
    contactos[nombre] = nuevo_telefono
    print(f"El número de teléfono de {nombre} ha sido actualizado correctamente.")
  else:
    print(f"El contacto {nombre} no existe.")

def eliminar_contacto():
  """Función para eliminar un contacto."""
  nombre = input("Ingresa el nombre del contacto a eliminar: ")
  if nombre in contactos:
    del contactos[nombre]
    print(f"El contacto {nombre} ha sido eliminado correctamente.")
  else:
    print(f"El contacto {nombre} no existe.")

def menu():
  """Función para mostrar el menú y solicitar la opción del usuario."""
  print("\nBienvenido a la gestión de contactos.")
  print("Opciones:")
  print("1. Agregar un contacto.")
  print("2. Buscar un contacto.")
  print("3. Mostrar todos los contactos.")
  print("4. Actualizar número de teléfono.")
  print("5. Eliminar un contacto.")
  print("6. Salir.")
  opcion = input("Ingresa tu opción: ")
  return opcion

while True:
  opcion = menu()

  if opcion == "1":
    agregar_contacto()
  elif opcion == "2":
    buscar_contacto()
  elif opcion == "3":
    mostrar_contactos()
  elif opcion == "4":
    actualizar_telefono()
  elif opcion == "5":
    eliminar_contacto()
  elif opcion == "6":
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida.")
