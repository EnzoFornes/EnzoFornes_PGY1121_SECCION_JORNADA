#1Registrar datos vehiculo : Tpo, marca, patente, precio, fecha de ingreso, multas y nombre del deuño 
#2Buscar patente y datos almacenados 
#3Imprimir certificados de multa , por contaminacion. Valores entre 1500 y 3500
#4 Salir con mensaje mencionndo nombre.
import random as rs
print(" Que es lo que desea realizar")
print (" 1.- Registrar datos del vehiculo. ")
print (" 2.- Buscar datos del vehiculo. ")
print (" 3.- Obtener certificados del vehiculo. ")
print (" 4.- Salir. ")

while True:
    op = int(input())
    if op == 1:
        TipoVehiculo = (input(" Ingrese Tipo de vehiculo: "))
        marcaVehiculo = (input(" Ingrese Marca del vehiculo: "))
        PatenteVehiculo = (input(" Ingrese patente del vehiculo: "))
        PrecioVehiculo = print(input(" Ingrese el precio del vehiculo"))
        
        if PrecioVehiculo < 5000000:
            print(" El precio debe ser mayor a $5.000.000")
            print(" Ingresa otro monto ")
            PrecioVehiculo = int(input("Ingrese el precio del vehiculo :"))
        else:
            break
        Ingresovehiculo = (input(" Ingrese fecha de ingreso: "))
        DueñoVehiculo = (input(" Ingrese nombre del dueño: "))
        print(" ¿Posee multas?")
        print("1. SI ")
        print("2. NO ")
        multa = int(input())
        if multa == 1:
            type(input(" Ingrese el valor de la multa"))
        else:
            break

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehículo: ")
    for vehiculo in vehiculo:
        if vehiculo["patente"] == patente:
            print("Tipo: " + vehiculo["tipo"])
            print("Patente: " + vehiculo["patente"])
            print("Marca: " + vehiculo["marca"])
            print("Precio: $" + str(vehiculo["precio"]))
            print("Multas:")
            for multa in vehiculo["multas"]:
                print("- Monto: $" + str(multa[0]) + " Fecha: " + multa[1])
            print("Fecha de registro: " + vehiculo["fecha_registro"])
            print("Dueño: " + vehiculo["nombre_dueño"])
            return
    print("No se encontró ningún vehículo con la patente ingresada.")

def imprimir_certificados():
    for vehiculo in vehiculo:
        print("Certificado de emisión de contaminantes")
        print("Patente: " + vehiculo["patente"])
        print("Dueño: " + vehiculo["nombre_dueño"])
        print("Valor: $" + rs(1500, 3500))
        print()
        print("Certificado de anotaciones vigentes")
        print("Patente: " + vehiculo["patente"])
        print("Dueño: " + vehiculo["nombre_dueño"])
        print("Valor: $" + rs(1500, 3500))
        print()
        print("Certificado de multas")
        print("Patente: " + vehiculo["patente"])
        print("Dueño: " + vehiculo["nombre_dueño"])
        print("Valor: $" + rs(1500, 3500))
        print()
        
def salir():
    print("Gracias por utilizar el programa de Auto Seguro.")
    print("Desarrollado por [Nombre y Apellido]. Versión 1.0.")
    exit()