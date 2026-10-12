import os

while True:
    print("\n=== Opciones ===")
    print("1. Actualizar el sistema")
    print("2. Quitar paquetes innecesarios")
    print("3. Limpiar Cache de pacman")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
    match opcion:
        case "1":
            os.system("paru && flatpak update")
        case "2":
            os.system("sudo pacman -Rns $(pacman -Qtdq)")
        case "3":
            os.system("sudo paccache -r")
        case "4":
            break