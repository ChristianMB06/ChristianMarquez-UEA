def calcular_precio_con_descuento():
    # Solicitar al usuario que ingrese el precio original (puede incluir decimales)
    precio_original = float(input("Ingresa el precio original: "))

    # Solicitar al usuario que ingrese el porcentaje de descuento (puede incluir decimales)
    descuento = float(input("Ingresa el porcentaje de descuento: "))

    # Estructura condicional if-else
    if descuento > 0:
        precio_final = precio_original - (precio_original * descuento / 100)
        print(f"El precio final con descuento es: {precio_final:.2f}")
    else:
        print("No se aplicó ningún descuento.")

def main():
    while True:
        calcular_precio_con_descuento()
        
        # Preguntar al usuario si desea continuar o salir
        continuar = input("¿Deseas continuar? (si/no): ").strip().lower()
        if continuar != 'si':
            print("Gracias por usar el programa. ¡Adiós!")
            break

# Ejecutar la función principal
if __name__ == "__main__":
    main()
