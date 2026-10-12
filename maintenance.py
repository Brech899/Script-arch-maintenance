import os
import json

while True:
    print("\n=== Opciones ===")
    print("1. Actualizar el sistema")
    print("2. Quitar paquetes innecesarios")
    print("3. Limpiar Cache de pacman")
    print("4. Limpiar Cache del Navegador")
    print("5 Salir")

    opcion = input("Seleccione una opción (1-5): ")
    match opcion:
        case "1":
            print("1.Yay 2.Paru")
            choice = input("Seleccione una opción (1-2): ")
            if choice == "1":
                os.system("yay && flatpak update")
            elif choice == "2":
                os.system("paru && flatpak update")
        case "2":
            os.system("sudo pacman -Rns $(pacman -Qtdq)")
        case "3":
            os.system("sudo paccache -r")
        case "4":
            print("1.Brave 2.Firefox")
            choice = input("Seleccione una opción (1-2): ")
            if choice == "1":
                os.system("rm -rf ~/.cache/BraveSoftware")
            elif choice == "2":
                os.system("rm -rf ~/.cache/Mozilla/Firefox")
        case "5":
            break
