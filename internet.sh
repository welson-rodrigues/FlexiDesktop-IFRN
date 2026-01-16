#!/bin/bash

# Configurações de Tela
export DISPLAY=:0
export XAUTHORITY=/home/aluno/.Xauthority

# Loop Infinito (Kiosk Mode)
while true; do

    # Abre o Python (Login)
    python3 /home/aluno/interface_ifrn.py

    # Se logou com sucesso (exit 0)...
    if [ $? -eq 0 ]; then
        
        echo "Autenticado. Iniciando X2Go..."
        sleep 1
        
        # Abre o X2Go
        # O nome da sessão deve ser igual ao salvo no x2goclient
        /usr/bin/x2goclient --session="Servidor_Lindo" --thinclient --no-menu --hide > /tmp/x2go_log.txt 2>&1
        
        # Quando o X2Go fecha, reinicia a TV Box (Limpeza)
        sudo reboot
        exit
    else
        # Se cancelou o login, espera e tenta de novo
        sleep 2
    fi

done
