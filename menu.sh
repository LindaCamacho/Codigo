#!/bin/bash

script1() {
    bash ordenar.sh
}

script2() {
    bash mover
}

interprete() {
    bash interprete
}

mostrarMenu() {
    echo "1) Crear scrips" 
    echo "2) Mover scrips a carpetas" 
    echo "3) Interprete de comandos"
    echo "4) Salir"  
}

while true; do 
    mostrarMenu
    read -p "Ingresa una opción: " opcion 

    case $opcion in 
        1) script1 ;; 
        2) script2 ;; 
        3) interprete ;;
        4) echo "Saliendo del programa..."; break;;  

        *) echo "Opción no valida.." ;; 
        esac
done
            
