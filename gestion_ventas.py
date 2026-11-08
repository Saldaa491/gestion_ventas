# ============================================================
# SISTEMA DE GESTIÓN DE VENTAS POR SUCURSAL
# Curso: Fundamentos de Algoritmia y Programación - UNAD
# Código: 553308627
# Estudiante: Adrián Saldaña
# ============================================================

# ------------------------------------------------------------
# 1. FUNCIÓN PARA LEER Y VALIDAR NÚMEROS DECIMALES
# ------------------------------------------------------------

def leer_float(mensaje, minimo=0.0, estricto=False):
    """Solicita un número decimal y valida que sea correcto."""

    while True:
        try:
            valor = float(input(mensaje))

            if not (valor >= float("-inf") and valor <= float("inf")):
                print("[!] Ingrese un número válido.")
                continue

            if estricto:
                if valor <= minimo:
                    print(f"[!] El valor debe ser mayor que {minimo}.")
                    continue
            else:
                if valor < minimo:
                    print(f"[!] El valor debe ser mayor o igual a {minimo}.")
                    continue

            return valor

        except ValueError:
            print("[!] Entrada inválida. Ingrese un número.")


# ------------------------------------------------------------
# 2. FUNCIÓN PARA LEER Y VALIDAR NÚMEROS ENTEROS
# ------------------------------------------------------------

def leer_int(mensaje, minimo=1, maximo=365):
    """Solicita un número entero dentro de un rango permitido."""

    while True:
        try:
            valor = int(input(mensaje))

            if valor < minimo or valor > maximo:
                print(f"[!] Ingrese un número entre {minimo} y {maximo}.")
                continue

            return valor

        except ValueError:
            print("[!] Entrada inválida. Ingrese un número entero.")


# ------------------------------------------------------------
# 3. REGISTRO DE SUCURSAL Y VENTAS DIARIAS
# ------------------------------------------------------------

def registrar_sucursal(nombres, totales, promedios, metas, dias_list):

    print("\n========== REGISTRO DE SUCURSAL ==========")

    # Validación del nombre de la sucursal
    while True:
        nombre = input("Nombre de la sucursal: ").strip()

        if nombre:
            break
        else:
            print("[!] El nombre no puede estar vacío.")

    # Cantidad de días que se van a registrar
    dias = leer_int("Cantidad de días a registrar (1-365): ", 1, 365)

    # Inicialización del acumulador y contador
    total = 0.0
    contador = 0

    # Ciclo para registrar las ventas de cada día
    for i in range(dias):

        venta = leer_float(
            f"Venta del día {i + 1}: $",
            0.0
        )

        total += venta
        contador += 1

    # Solicitud de la meta diaria
    meta = leer_float("Meta diaria de ventas: $", 0.0, True)

    # Cálculo del promedio diario
    promedio = total / contador if contador > 0 else 0.0

    # Almacenamiento de la información en las listas
    nombres.append(nombre)
    totales.append(total)
    promedios.append(promedio)
    metas.append(meta)
    dias_list.append(dias)

    print("\n[SUCURSAL REGISTRADA EXITOSAMENTE]")
    print(f"Nombre: {nombre}")
    print(f"Total de ventas: ${total:,.2f}")
    print(f"Promedio diario: ${promedio:,.2f}")


# ------------------------------------------------------------
# 4. CONSULTAR TOTAL DE VENTAS POR SUCURSAL
# ------------------------------------------------------------

def consultar_totales(nombres, totales):

    print("\n========== TOTAL DE VENTAS ==========")

    if not nombres:
        print("No hay sucursales registradas.")
        return

    for i, nombre in enumerate(nombres):

        print(f"{i + 1}. {nombre}: ${totales[i]:,.2f}")


# ------------------------------------------------------------
# 5. CALCULAR PROMEDIOS DIARIOS
# ------------------------------------------------------------

def calcular_promedios(nombres, promedios, dias_list):

    print("\n========== PROMEDIOS DIARIOS ==========")

    if not nombres:
        print("No hay sucursales registradas.")
        return

    for i, nombre in enumerate(nombres):

        print(
            f"{nombre}: ${promedios[i]:,.2f} "
            f"(Promedio de {dias_list[i]} días)"
        )


# ------------------------------------------------------------
# 6. VERIFICACIÓN DEL CUMPLIMIENTO DE METAS
# ------------------------------------------------------------

def verificar_metas(nombres, promedios, metas):

    print("\n========== VERIFICACIÓN DE METAS ==========")

    if not nombres:
        print("No hay sucursales registradas.")
        return

    for i, nombre in enumerate(nombres):

        if promedios[i] >= metas[i]:
            estado = "META ALCANZADA"
        else:
            estado = "META NO ALCANZADA"

        print(f"\nSucursal: {nombre}")
        print(f"Promedio diario: ${promedios[i]:,.2f}")
        print(f"Meta diaria: ${metas[i]:,.2f}")
        print(f"Resultado: {estado}")


# ------------------------------------------------------------
# 7. GENERAR REPORTE GENERAL
# ------------------------------------------------------------

def reporte_general(nombres, totales, promedios, metas, dias_list):

    print("\n")
    print("==============================================")
    print("             REPORTE GENERAL")
    print("==============================================")

    if not nombres:
        print("No hay sucursales registradas.")
        return

    # Inicialización del gran total
    gran_total = 0.0

    # Recorrido de las sucursales registradas
    for i, nombre in enumerate(nombres):

        if promedios[i] >= metas[i]:
            estado = "META ALCANZADA"
        else:
            estado = "META NO ALCANZADA"

        print(f"\nSucursal: {nombre}")
        print(f"Días registrados: {dias_list[i]}")
        print(f"Total de ventas: ${totales[i]:,.2f}")
        print(f"Promedio diario: ${promedios[i]:,.2f}")
        print(f"Meta diaria: ${metas[i]:,.2f}")
        print(f"Estado: {estado}")

        # Acumulación de las ventas de todas las sucursales
        gran_total += totales[i]

    print("\n----------------------------------------------")
    print(f"TOTAL GENERAL DE VENTAS: ${gran_total:,.2f}")
    print(f"TOTAL DE SUCURSALES REGISTRADAS: {len(nombres)}")
    print("==============================================")


# ------------------------------------------------------------
# 8. FUNCIÓN PRINCIPAL Y MENÚ INTERACTIVO
# ------------------------------------------------------------

def main():

    # Listas para almacenar la información de las sucursales
    nombres = []
    totales = []
    promedios = []
    metas = []
    dias_list = []

    opcion = 0

    # Ciclo principal del programa
    while opcion != 6:

        print("\n")
        print("============================================")
        print("       SISTEMA DE GESTIÓN DE VENTAS")
        print("============================================")
        print("1. Registrar sucursal y ventas diarias")
        print("2. Consultar total de ventas")
        print("3. Calcular promedios")
        print("4. Verificar metas")
        print("5. Mostrar reporte general")
        print("6. Salir")
        print("============================================")

        opcion = leer_int("Seleccione una opción (1-6): ", 1, 6)

        # Condicionales para ejecutar las opciones del menú

        if opcion == 1:

            registrar_sucursal(
                nombres, totales, promedios, metas, dias_list
            )

        elif opcion == 2:

            consultar_totales(nombres, totales)

        elif opcion == 3:

            calcular_promedios(nombres, promedios, dias_list)

        elif opcion == 4:

            verificar_metas(nombres, promedios, metas)

        elif opcion == 5:

            reporte_general(
                nombres, totales, promedios, metas, dias_list
            )

        elif opcion == 6:

            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado correctamente.")


# ------------------------------------------------------------
# 9. EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------

if __name__ == "__main__":
    main()