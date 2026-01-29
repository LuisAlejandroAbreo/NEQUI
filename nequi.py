def cargar_saldo(saldo):
    monto = float(input("Ingrese el monto a cargar: "))
    if monto > 0:
        saldo += monto
        print(f"Carga exitosa. Saldo actual: ${saldo}")
    else:
        print("Monto inválido. Debe ser mayor que cero.")
    return saldo

def pagar(saldo):
    monto = float(input("Ingrese el monto a pagar: "))
    if monto <= 0:
        print("Monto inválido.")
    elif monto > saldo:
        print("Fondos insuficientes. Operación cancelada.")
    else:
        saldo -= monto
        print(f"Pago realizado con éxito. Saldo restante: ${saldo}")
    return saldo


def transferir_dinero(saldo):
    celular = input("Ingrese el número de celular del destinatario: ")
    
    if not celular.isdigit() or len(celular) != 10:
        print("Número de celular inválido.")
        return celular

    monto = float(input("Ingrese el monto a transferir: "))
    
    if monto <= 0:
        print("Monto inválido.")
    elif monto > saldo:
        print("Saldo insuficiente para realizar la transferencia.")
    else:
        saldo -= monto
        print(f"Transferencia exitosa al número {celular}.")
        print(f"Saldo actual: ${saldo}")
    
    return saldo

def mostrar_saldo(saldo):
    print(f"Saldo actual: ${saldo}")

def main():
    saldo = 0
    opcion = 0

    while opcion != 5:
        print("\n--- Sistema de Gestión Nequi ---")
        print("1. Cargar saldo")
        print("2. Pagar")
        print("3. Transferir dinero")
        print("4. Mostrar saldo")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            saldo = cargar_saldo(saldo)
        elif opcion == 2:
            saldo = pagar(saldo)
        elif opcion == 3:
            saldo = transferir_dinero(saldo)
        elif opcion == 4:
            mostrar_saldo(saldo)
        elif opcion == 5:
            print("Gracias por usar Nequi. ¡Hasta pronto!")
        else:
            print("Opción inválida. Intente nuevamente.")

main()