# Clasificación Automática de Presión Arterial
# Propósito: Clasificar la presión arterial de múltiples pacientes según rangos clínicos

# Pedir cantidad de pacientes a evaluar
cantidad_pacientes = int(input("Ingrese la cantidad de pacientes a evaluar: "))

# Bucle for para procesar cada paciente
for i in range(1, cantidad_pacientes + 1):
    print(f"\n--- Paciente {i} de {cantidad_pacientes} ---")
    
    # Entrada de valores de presión
    sistolica = float(input("Ingrese presión sistólica (mmHg): "))
    diastolica = float(input("Ingrese presión diastólica (mmHg): "))

    # Clasificación según rangos clínicos
    if sistolica < 120 and diastolica < 80:
        categoria = "Normal"
    elif (120 <= sistolica <= 139) or (80 <= diastolica <= 89):
        categoria = "Prehipertensión"
    else:
        categoria = "Hipertensión"

    # Mostrar resultado de la clasificación
    print(f"Clasificación: {categoria}")