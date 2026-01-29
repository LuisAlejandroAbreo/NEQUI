def mostrar_menu():
    print("""\n--- Sistema de Gestión Nequi ---
    1. Cargar saldo
    2. Pagar
    3. Transferir dinero
    4. Mostrar saldo
    5. Salir""")

def validar_monto(monto):
    return monto > 0

def validar_saldo(monto, saldo):
    return monto <= saldo

def validar_celular(celular):
    return celular.isdigit() and len(celular) == 10

def cargar_saldo(saldo):
    try:
        monto = float(input("Ingrese el monto a cargar: "))
        if validar_monto(monto):
            saldo += monto
            print(f"Recarga exitosa. Nuevo saldo: ${saldo}")
        else:
            print("Error: El monto debe ser mayor que cero.")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
    return saldo

def pagar(saldo):
    try:
        monto = float(input("Ingrese el monto a pagar: "))
        if not validar_monto(monto):
            print("Error: El monto debe ser mayor que cero.")
        elif not validar_saldo(monto, saldo):
            print("Fondos insuficientes para realizar el pago.")
        else:
            saldo -= monto
            print(f"Pago realizado con éxito. Saldo restante: ${saldo}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
    return saldo

def transferir_dinero(saldo):
    celular = input("Ingrese el número de celular del destinatario: ")

    if not validar_celular(celular):
        print("Error: Número de celular inválido. Debe tener 10 dígitos.")
        return saldo

    try:
        monto = float(input("Ingrese el monto a transferir: "))
        if not validar_monto(monto):
            print("Error: El monto debe ser mayor que cero.")
        elif not validar_saldo(monto, saldo):
            print("Fondos insuficientes para realizar la transferencia.")
        else:
            saldo -= monto
            print(f"Transferencia exitosa al número {celular}.")
            print(f"Saldo restante: ${saldo}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

    return saldo

def mostrar_saldo(saldo):
    print(f"Saldo actual: ${saldo}")

def main():
    saldo = 0.0
    print("Bienvenido a Nequi")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            saldo = cargar_saldo(saldo)
        elif opcion == "2":
            saldo = pagar(saldo)
        elif opcion == "3":
            saldo = transferir_dinero(saldo)
        elif opcion == "4":
            mostrar_saldo(saldo)
        elif opcion == "5":
            print("Gracias por usar Nequi. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()