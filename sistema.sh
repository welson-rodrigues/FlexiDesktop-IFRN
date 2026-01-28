#!/bin/bash

# Configurações de Tela
export DISPLAY=:0
export XAUTHORITY=/home/aluno/.Xauthority

# Loop Infinito (Kiosk Mode)
while true; do

    # Login
    python3 /home/aluno/interface_ifrn.py
    
    if [ $? -eq 0 ]; then
        
        echo "Autenticado. Iniciando X2Go..."
        sleep 1
        
        # bre o X2Go
        /usr/bin/x2goclient --session="Servidor_Lindo" --thinclient --no-menu --hide > /tmp/x2go_log.txt 2>&1
        
        sudo reboot
        exit
        
        sleep 2
    fi

done
