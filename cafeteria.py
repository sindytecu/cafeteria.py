import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pedidos"
)



def crear():
    customerName = input("Nombre del cliente: ")
    productName = input("Producto: ")
    quantity = int(input("Cantidad: "))
    orderType = input("Tipo (Regular, Student, Teacher): ")

  
    if orderType == "Student":
        discount = 10
    elif orderType == "Teacher":
        discount = 15
    else: 
        discount = 0

    precio = 15
    total = (quantity * precio) - (quantity * precio * discount / 100)
    if conexion.is_connected():
       cursor = conexion.cursor()
       query = "INSERT INTO orders (customerName, productName, quantity, orderType, discount, total) VALUES (%s, %s, %s, %s, %s, %s)"
       cursor.execute(query, (customerName, productName, quantity, orderType, discount, total))
       conexion.commit()
       print(f"Pedido guardado. Descuento aplicado: {discount}%")

print("============================")


def mostrar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM orders")
    for f in cursor.fetchall():
        print(f)

print("===========================")


def actualizar():
    id_actualizar = input("ID para actualizar: ")
    customerName = input("Nuevo nombre cliente: ")
    productName = input("Nuevo producto: ")
    quantity = int(input("Nueva cantidad: "))
    orderType = input("Nuevo tipo (Regular, Student, Teacher): ")

    if orderType == "Student":
        discount = 10
    elif orderType == "Teacher":
        discount = 15
    else:
        discount = 0

    precio = 15
    total = (quantity * precio) - (quantity * precio * discount / 100)
    if conexion.is_connected():
       cursor = conexion.cursor()
       query = "UPDATE orders SET customerName=%s, productName=%s, quantity=%s, orderType=%s, discount=%s, total=%s WHERE id=%s"
       cursor.execute(query, (customerName, productName, quantity, orderType, discount, total, id_actualizar))
       conexion.commit()
       print("Pedido actualizado correctamente")




def eliminar():
    id_eliminar = int(input("ID para borrar: "))
    cursor = conexion.cursor()
    query = "DELETE FROM orders WHERE id=%s"
    cursor.execute(query, (id_eliminar,))
    conexion.commit()
    print("Pedido eliminado")



def menu():
    while True:
        print("1. CREAR PEDIDO")
        print("2. VER PEDIDOS")
        print("3. ACTUALIZAR PEDIDO")
        print("4. ELIMINAR PEDIDO")
        print("5. SALIR")

        try:
            desi = int(input("INGRESE LA OPCION: "))

            if desi == 1:
                crear()
            elif desi == 2:
                mostrar()
            elif desi == 3:
                actualizar()
            elif desi == 4:
                eliminar()
            elif desi == 5:
                print("Saliendo...")
                break
            else:
                print("INTENTE DE NUEVO")
        except ValueError:
            print("SOLO NUMEROS, NO LETRAS, VUELVE A INTENTARLO")

menu()